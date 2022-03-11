from socket import *
IP = '127.0.0.1'
PORT = 2333

BUFLEN = 512

listen = socket(AF_INET,SOCK_STREAM)
listen.bind((IP,PORT))
listen.listen(5)
print(f'服务端启动成功，在{PORT}端口监听客户端连接')

mySocket,addr = listen.accept()
print(f'接收到客户端连接：',addr)


while True:
    received = mySocket.recv(BUFLEN)
    if not received:
        break
    info = received.decode()
    print(f'收到对方信息：{info}')

    aboutToSend = input('发送的消息>> ')
    if aboutToSend =='':
        break
    mySocket.send(aboutToSend.encode())

mySocket.close()
listen.close()
