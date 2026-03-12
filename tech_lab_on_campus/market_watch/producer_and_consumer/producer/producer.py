import pika
import os
from producer_interface import mqProducerInterface

class mqProducer(producerInterface):
    def __init__(self, routing_key,exchange_name):
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        self.setupRMQConnection(routing_key, exchange_name)
        


