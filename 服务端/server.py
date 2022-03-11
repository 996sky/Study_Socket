from socket import *
IP = '0.0.0.1'
PORT = 2333

BUFLEN = 512

listenSocket = socket(AF_INET,SOCK_STREAM)
listenSocket.bind((IP,PORT))
listenSocket.listen(5)
print(f'服务端启动成功，在{PORT}端口监听客户端连接')

dataSocket,addr = listenSocket.accept()
print(f'接收到客户端连接：',addr)


while True:
    received = dataSocket.recv(BUFLEN)
    if not received:
        break
    info = received.decode()
    print(f'收到对方信息：{info}')

    aboutToSend = input('发送的消息>> ')
    if aboutToSend =='':
        break
    dataSocket.send(aboutToSend.encode())

dataSocket.close()
listenSocket.close()
