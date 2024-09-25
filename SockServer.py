import socket

try:
    s=socket.socket()
    print('Socket Created')
    s.bind(('localhost',9998))
    s.listen(3)

    while True:
        c,addr=s.accept()
        name = c.recv(1024).decode()
        print("Connected with ",addr,name)
        c.send(bytes('Welcome to socket programming','utf-8'))
        c.close()
except KeyboardInterrupt:
    s.close()
finally:
    s.close()
