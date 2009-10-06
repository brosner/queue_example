from carrot.backends.queue import Backend as PyQueueBackend
from carrot.connection import BrokerConnection
from carrot.messaging import Publisher


# setting up RabbitMQ:
# see http://www.rabbitmq.com/debian.html#apt
# rabbitmqctl add_user test password
# rabbitmqctl add_vhost test.com
# rabbitmqctl set_permissions -p test.com test "" ".*" ".*"


def main():
    connection = BrokerConnection(
        hostname = "localhost",
        port = 5672,
        userid = "test",
        password = "password",
        virtual_host = "test.com",
    )
    
    publisher = Publisher(
        connection = connection,
        exchange = "messages",
        routing_key = "awesome",
    )
    
    for i in xrange(100):
        publisher.send({"a": i})
    
    publisher.close()


if __name__ == "__main__":
    main()