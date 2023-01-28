#Python Image Stegangraphy project
import tkinter as tk
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import os
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
import base64
import webbrowser




class IMG_Stegno():
    #main frame or start page
    def main(self, root):
        root.title('Project : Science of Steganography')
        root.geometry('500x600')
        root.resizable(width =True,height=True)
        root.config()
        frame = Frame(root)
        frame.grid()
           
        title = Label(frame,text='Science of Steganography ')
        title.config(font=('Times new roman',27, 'bold'))
        title.grid(pady=30)
        title.grid(row=1)

        title1 = Label(frame,text='Hidden text inside Image')
        title1.config(font=('Times new roman',23, 'bold'))
        title1.grid(pady=20)
        title1.grid(row=2)

        title2 = Label(frame,text='choose an option :')
        title2.config(font=('Times new roman',18))
        title2.grid(pady=20)
        title2.grid(row=3)
     
        encode = Button(frame,text="Encode",command= lambda :self.encode_frame1(frame), padx=18)
        encode.config(font=('Helvetica',20))
        encode.grid(pady=5)
        encode.grid(row=4)
       
        decode = Button(frame, text="Decode",command=lambda :self.decode_frame1(frame), padx=18)
        decode.config(font=('Helvetica',20))
        decode.grid(pady = 5)
        decode.grid(row=5)

        
        
        url="https://github.com/ZakariaHibaoui/Science_Stegano"
        
        github=Button(frame,text="Repository Github",command=lambda: webbrowser.open(url),padx=18)
        github.config(font=('Helvetica',20))
        github.grid(pady = 5)
        github.grid(row=7)

        


     
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)   

#Back function to loop back to main screen
    def back(self,frame):
        frame.destroy()
        self.main(root)





#frame for encode page
    def encode_frame1(self,F):
         F.destroy()
         F2 = Frame(root)
         label1= Label(F2,text='Select the Image in which \n you want to hide text :')
         label1.config(font=('Times new roman',25, 'bold'))
         label1.grid(pady=120)
     
         button_bws = Button(F2,text='Select',command=lambda : self.encode_frame2(F2))
         button_bws.config(font=('Helvetica',18))
         button_bws.grid()
         button_back = Button(F2, text='Cancel', command=lambda : IMG_Stegno.back(self,F2))
         button_back.config(font=('Helvetica',18))
         button_back.grid(pady=15)
         button_back.grid()
         F2.grid()
     
#frame for decode page
    def decode_frame1(self,F):
         F.destroy()
         d_f2 = Frame(root)
         label1 = Label(d_f2, text='Select Image with Hidden text:')
         label1.config(font=('Times new roman',25,'bold'))
         label1.grid(pady=120)
         label1.config()
         button_bws = Button(d_f2, text='Select', command=lambda :self.decode_frame2(d_f2))
         button_bws.config(font=('Helvetica',18))
         button_bws.grid()
         button_back = Button(d_f2, text='Cancel', command=lambda : IMG_Stegno.back(self,d_f2))
         button_back.config(font=('Helvetica',18))
         button_back.grid(pady=15)
         button_back.grid()
         d_f2.grid()

# function to encode image
    def encode_frame2(self,e_F2):
         e_pg= Frame(root)
         myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
         if not myfile:
             messagebox.showerror("Error","You have selected nothing !")
         else:
             my_img = Image.open(myfile)
             new_image = my_img.resize((300,200))
             img = ImageTk.PhotoImage(new_image)
             label3= Label(e_pg,text='Selected Image')
             label3.config(font=('Helvetica',14,'bold'))
             label3.grid() 
             board = Label(e_pg, image=img)
             board.image = img
             self.output_image_size = os.stat(myfile)
             self.o_image_w, self.o_image_h = my_img.size
             board.grid()
             label2 = Label(e_pg, text='Enter the message')
             label2.config(font=('Helvetica',14,'bold'))
             label2.grid(pady=15)
             text_a = Text(e_pg, width=50, height=10)
             text_a.grid()
             encode_button = Button(e_pg, text='Cancel', command=lambda : IMG_Stegno.back(self,e_pg))
             encode_button.config(font=('Helvetica',14))
             data = text_a.get("1.0", "end-1c")
             button_back = Button(e_pg, text='Encode', command=lambda : [self.enc_fun(text_a,my_img),IMG_Stegno.back(self,e_pg)])
             button_back.config(font=('Helvetica',14))
             button_back.grid(pady=15)
             encode_button.grid()
             e_pg.grid(row=1)
             e_F2.destroy()

    def derive_key(self, pasw: bytes):
        keyDerivationFunction = Scrypt(
            salt=b'ABCDEF',
            length=32,
            n=2**14,
            r=8,
            p=1,
            backend=default_backend()
        )
        deriveKEY = keyDerivationFunction.derive(pasw)
        key = base64.urlsafe_b64encode(deriveKEY)
        return key

# function to decode image
    def decode_frame2(self,d_F2):
        #TODO: ADD PASSWORD FIELD!!!!!!!!!!
        password = "supersecret"

        d_F3 = Frame(root)
        myfiles = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfiles:
             messagebox.showerror("Error","You have selected nothing !")
        else:
            my_img = Image.open(myfiles, 'r')
            my_image = my_img.resize((300, 200))
            img = ImageTk.PhotoImage(my_image)
            label4= Label(d_F3,text='Selected Image :')
            label4.config(font=('Helvetica',14,'bold'))
            label4.grid()
            board = Label(d_F3, image=img)
            board.image = img
            board.grid()
            hidden_data = self.decode(my_img)

            dec = Fernet(self.derive_key(password.encode("utf-8")))
            try:
                dec_hidden_data = dec.decrypt(base64.b64decode(hidden_data))
            except InvalidToken:
                #TODO: INVALID PASSWORD DO SOMETHING!!!!!
                pass


            label2 = Label(d_F3, text='Hidden data is :')
            label2.config(font=('Helvetica',14,'bold'))
            label2.grid(pady=10)
            text_a = Text(d_F3, width=50, height=10)
            text_a.insert(INSERT, dec_hidden_data)
            text_a.configure(state='disabled')
            text_a.grid()
            button_back = Button(d_F3, text='Cancel', command= lambda :self.back(d_F3))
            button_back.config(font=('Helvetica',14))
            button_back.grid(pady=15)
            button_back.grid()
            d_F3.grid(row=1)
            d_F2.destroy()

#function to decode data
    def decode(self, image):
        image_data = iter(image.getdata())
        data = ''
     
        while (True):
            pixels = [value for value in image_data.__next__()[:3] +
                        image_data.__next__()[:3] +
                        image_data.__next__()[:3]]
            # string of binary data
            binary_str = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binary_str += '0'
                else:
                    binary_str += '1'
     
            data += chr(int(binary_str, 2))
            if pixels[-1] % 2 != 0:
                return data
     
#function to generate data
    def generate_Data(self,data):
        # list of binary codes of given data
        new_data = []
     
        for i in data:
            new_data.append(format(ord(i), '08b'))

        return new_data

#function to modify the pixels of image
    def modify_Pix(self,pix, data):
        dataList = self.generate_Data(data)
        dataLen = len(dataList)
        imgData = iter(pix)
        for i in range(dataLen):
            pix = [value for value in imgData.__next__()[:3] +
                    imgData.__next__()[:3] +
                    imgData.__next__()[:3]]
            for j in range(0, 8):
                if (dataList[i][j] == '0') and (pix[j] % 2 != 0):
                    pix[j] -= 1
                elif (dataList[i][j] == '1') and (pix[j] % 2 == 0):
                    if(pix[j] != 0):
                        pix[j] -= 1
                    else:
                        pix[j] += 1

            if (i == dataLen - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1
 
            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

#function to enter the data pixels in image
    def encode_enc(self,newImg, data):
        w = newImg.size[0]
        (x, y) = (0, 0)
     
        for pixel in self.modify_Pix(newImg.getdata(), data):
     
            # Putting modified pixels in the new image
            newImg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

# function to enter hidden text
    def enc_fun(self,text_a,myImg):
        #TODO: ADD PASSWORD BOX!!!!!
        password = "supersecret"

        data = text_a.get("1.0", "end-1c")
        if (len(data) == 0):
            messagebox.showinfo("Alert","Kindly enter text in TextBox")
        else:
            enc = Fernet(self.derive_key(password.encode("utf-8")))

            newImg = myImg.copy()

            base64data = base64.b64encode(enc.encrypt(data.encode("utf-8"))).decode("ascii")
            self.encode_enc(newImg, base64data)
            my_file = BytesIO()
            temp=os.path.splitext(os.path.basename(myImg.filename))[0]
            newImg.save(tkinter.filedialog.asksaveasfilename (initialfile=temp, filetypes = ([('png', '*.png')]), defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w,self.d_image_h = newImg.size
            messagebox.showinfo("Success","Encoding Successful\nFile successfully saved")
     
    def frame_3(self,frame):
        frame.destroy()
        self.main(root)



#GUI loop
root = Tk()
o = IMG_Stegno()
o.main(root)
root.mainloop()
