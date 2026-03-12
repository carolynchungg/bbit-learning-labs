import pika
import os
from producer_interface import mqProducerInterface

class mqProducer(mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        # Save parameters to instance variable
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        self.setupRMQConnection()
        
        

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        # We'll first set up the connection and channel
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=con_params)

        # pika.ConnectionParameters(host='localhost')
        self.channel = self.connection.channel()

        # Create the exchange if not already present
        self.channel.exchange_declare(exchange=self.exchange_name)
    
    def publishOrder(self, message: str) -> None:
            
        # Basic Publish to Exchange
        # routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
        # message = ' '.join(sys.argv[2:]) or 'Hello World!'
        self.channel.basic_publish(
        exchange= self.exchange_name, routing_key=self.routing_key, body=message)
        print(f" [x] Sent {self.routing_key}:{message}")

        # Close Channel
        self.channel.close()

        # Close Connection
        self.connection.close()
            
        