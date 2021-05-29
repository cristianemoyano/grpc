from __future__ import print_function
import logging

import grpc

import hello_pb2
import hello_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = hello_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(hello_pb2.HelloRequest(name='Action 1'))
    print("Greeter client received: " + response.message)
    response = stub.SayHelloAgain(hello_pb2.HelloRequest(name='Action 2'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()