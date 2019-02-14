#!/usr/bin/env python
import pika
import time

# START SERVER
self.connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
self.channel = connection.channel()


self.channel.queue_declare(queue='server')

channel.basic_consume(callback,
                      queue='server',
                      no_ack=True)

channel.start_consuming()

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
# END SERVER


def send(msg):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
    channel = connection.channel()


    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=msg)
    print(" [x] '{}'".format(msg))
    connection.close()

def receive():
    connection = pika.BlockingConnection()
    channel = connection.channel()
    method_frame, header_frame, body = channel.basic_get('hello')
    if method_frame:
        print(method_frame, header_frame, body)
        channel.basic_ack(method_frame.delivery_tag)
        return str(body, 'utf-8')
    else:
        print('No message returned')


def run():
    global client_num
    if client_num == 1:
        send("first")

    while True:
        msg = receive()

        if msg == "first":
            send("ping")
        elif msg == "ping":
            send("pong")
        elif msg == "pong":
            send("ping")
        else:
            print("something went wrong")

        time.sleep(1)

client_num = input("Enter client #: ")

try:
    client_num = int(client_num)
except:
    print("Error: Client # must be a numebr.")

run()
