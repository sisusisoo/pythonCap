from PIL import Image
import pytesseract



class OCRClASS: #클래스화 다른 클래스에서 객체화 하려면 이과정이 필요합니다!
    #이거 지워야함
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    imgPath1=""
    text=None
    #img = Image.open('img.jpg')
    def imageNorm(self):
        img= Image.open(self.imgPath1)
        img = img.resize((900, 900))
        self.text = pytesseract.image_to_string(img, lang='kor')
        print("---OCR를 사용하여 이미지의 내용 처리----")
        print(self.text)
        print("--------------------------------------------------")



    def init(self,imgPath):
        self.imgPath1=imgPath

    def text_process(self,input):
        list = []
        asicc = [chr(num) for num in range(33, 127)]
        asicc.append("\n")
        for i in range(0, len(input)):
            for t in range(0, len(asicc)):
                if input[i] == asicc[t] or (input[i] == "원" and input[i - 1] == asicc[t]):
                    list.append(" ")
                    list.append(" ")
                    break
                elif t == len(asicc) - 1 and asicc[t] != input[i]:
                    list.append(input[i])
                else:
                    continue
        return list


    def out_process(self,out): #out 은 list

        output = []
        word = ''
        i = 0
        while i < len(out):
            if out[i] != ' ':
                word += out[i]
            elif i < (len(out) - 2) and out[i] == ' ' and out[i - 1] != ' ':
                if out[i + 1] != ' ':
                    word += out[i]
                    i += 1
                    word += out[i]

                elif out[i + 1] == ' ' and word != '':
                    output.append(word)
                    word = ""
            i += 1
        return output

    def getter(self):
        print(self.imgPath1)
        self.imageNorm()
        l = self.text_process(self.text)#이게 문제
        print("debuging",l)
        output = self.out_process(l)

        print('-----츨력 데스트 처리-----')
        for i in range(0, len(output)):
            print(output[i])
        return output