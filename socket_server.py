# -*- coding:utf8 -*-

import socketserver
import threading

import OCR
import random
from OCR import OCRClASS


class RequestHandler(socketserver.StreamRequestHandler):
    def handle(self):

        # get socket request
        socket = self.request

        ocrStringArray= []
        ocrString=""

        # show client
        print('Connect with : ' + self.client_address[0])

        # set file name
        num = random.random() * 100000
        file_name = 'image_temp/file_' + str(int(num)) + '.png'
        file_name1='C:/OCR/img.jpg'
        print("1:"+file_name)
        ocr1=OCR.OCRClASS()
        ocr1.init(file_name)



        # get image file size from client
        file_size = socket.recv(1024) #이게 문제인듯?


        socket.sendall(file_size)
        print('set file size : ' + file_size.decode("utf-8")) # 이거 고침 ###

        # get image file byte stream from client
        # make empty image file
        with open(file_name, 'wb') as image_file:
            data_tmp = b''
            while True:
                # save image file from client stream
                data = socket.recv(1024)
                image_file.write(data)
                data_tmp += data
                if ((data_tmp.__len__())*100 == int(file_size)):
                    # check image file size
                    # print('received file size : {}'.format(data_tmp.__len__())*100)
                    break

        print('received & save image : ' + file_name)
        ocrStringArray=ocr1.getter()

        for i in range(0, len(ocrStringArray)):
            ocrString+=ocrStringArray[i]+" "
        print("stringOcr "+ocrString+" ")


        # tensorflow image classfication
        #connector_inst = connector_predict.Connect(file_name)
        #label = connector_inst.get_result()
        #label=
        socket.sendall(ocrString.encode())
        socket.close()

        
if __name__ == '__main__':
    HOST = '13.209.22.163'
    PORT = 8000

    server = socketserver.TCPServer((HOST, PORT), RequestHandler)

    print('Socket is now listening ...')
    server_thread = threading.Thread(target=server.serve_forever())
    server_thread.setDaemon(True)
    server_thread.start()
