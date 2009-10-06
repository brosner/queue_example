import time

from carrot.connection import BrokerConnection
from carrot.messaging import Consumer


def worker_callback(message_data, message):
    message.ack()
    print repr(message_data)
    time.sleep(1)


def main():
    connection = BrokerConnection(
        hostname = "localhost",
        port = 5672,
        userid = "test",
        password = "password",
        virtual_host = "test.com",
    )
    consumer = Consumer(
        connection = connection,
        queue = "messages",
        exchange = "messages",
        routing_key = "awesome",
    )
    
    consumer.register_callback(worker_callback)
    
    try:
        consumer.wait()
    except KeyboardInterrupt:
        consumer.close()


if __name__ == "__main__":
    main()