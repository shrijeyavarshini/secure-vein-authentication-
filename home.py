import datetime
import os
import shutil
from skimage.io import imread
from tkinter.ttk import Treeview
import time
import cv2
from tkinter import Tk, messagebox, ttk
from tkinter import *
from scipy.fftpack import dct, idct
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import numpy as np
import ar_master
from m_bpnn import BPNNetwork
import tkinter.simpledialog
mm= ar_master.master_flask_code()
class ar_vein():
    image=''
    path=''
    gray=''
    fname=''
    feature_value=0
    username=''
    def __init__(self):
        self.master = 'ar_master'
        self.title = 'Vein Authentication'
        self.titlec = 'VEIN AUTHENTICATION'
        self.backround_color = '#2F4F4F	'
        self.text_color = '#FFF'
        self.backround_image = 'images/background_hd.jpg'
        self.account_no=''
    def get_title(self):
        return self.title
    def get_titlec(self):
        return self.titlec
    def get_backround_color(self):
        return self.backround_color
    def get_text_color(self):
        return self.text_color
    def get_backround_image(self):
        return self.backround_image
    def get_account_no(self):
        return self.account_no
    def set_account_no(self,acc):
        self.account_no=acc
    def home_window(self):
        home_window_root=Tk()
        w = 950
        h = 600
        ws = home_window_root.winfo_screenwidth()
        hs = home_window_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        home_window_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        home_window_root.title(self.title)
        home_window_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=self.backround_image)
        canvas = Canvas(home_window_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(470, 40, text=self.titlec, font=("Times New Roman", 24), fill=self.text_color)
        def clickHandler(event):
            tt = ar_vein
            tt.user_login(event)
        image = Image.open('images/admin.png')
        img = image.resize((150, 150))
        my_img = ImageTk.PhotoImage(img)
        image_id = canvas.create_image(350, 170, image=my_img)
        canvas.tag_bind(image_id, "<1>", clickHandler)
        ###
        def clickHandler1(event):
            tt = ar_vein
            tt.user_registration(event)
        image1 = Image.open('images/users1.png')
        img1 = image1.resize((150, 150))
        my_img1 = ImageTk.PhotoImage(img1)
        image_id1 = canvas.create_image(350, 370, image=my_img1)
        canvas.tag_bind(image_id1, "<1>", clickHandler1)
        ###
        admin_id = canvas.create_text(570, 170, text="LOGIN", font=("Times New Roman", 24), fill=self.text_color)
        canvas.tag_bind(admin_id, "<1>", clickHandler)
        ###
        admin_id1 = canvas.create_text(570, 370, text="REGISTRATION", font=("Times New Roman", 24), fill=self.text_color)
        canvas.tag_bind(admin_id1, "<1>", clickHandler1)
        home_window_root.mainloop()
    def user_registration(self):
        user_registration_root = Toplevel()
        user_registration_root.attributes('-topmost', 'true')
        get_data = ar_vein()
        w = 950
        h = 600
        ws = user_registration_root.winfo_screenwidth()
        hs = user_registration_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_registration_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        user_registration_root.title(get_data.get_title())
        user_registration_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        canvas = Canvas(user_registration_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        admin_id2 = canvas.create_text(500, 70, text="USER REGISTRATION", font=("Times New Roman", 24), fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(200, 200, text="PATH", font=("Times New Roman", 24), fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(200, 325, text="FILE", font=("Times New Roman", 24), fill=get_data.get_text_color())
        e1 = Entry(user_registration_root, font=('times', 15, ' bold '),width=40)
        canvas.create_window(480, 200, window=e1)
        e2 = Entry(user_registration_root, font=('times', 15, ' bold '),width=40)
        canvas.create_window(480, 325, window=e2)
        def select_image():
            dir = r'data'
            if not os.path.exists(dir):
                os.mkdir(dir)
            for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))
            if not os.path.exists(dir):
                os.makedirs(dir)
            csv_file_path = askopenfilename( parent=user_registration_root)
            fpath = os.path.dirname(os.path.abspath(csv_file_path))
            fname = (os.path.basename(csv_file_path))
            fsize = os.path.getsize(csv_file_path)
            e1.delete(0, END)
            e1.insert(0, fpath)
            e2.insert(0, fname)
            get_data.path=os.path.abspath(csv_file_path)
            destination=os.path.join("data","input.png")
            print(destination)
            shutil.copy(os.path.abspath(csv_file_path), destination)
        def next_image():
            user_registration_root.destroy()
            tt = ar_vein()
            tt.image_grayscale()
        b1 = Button(user_registration_root,text='Select Image',command=select_image ,font=('times', 15, ' bold '), width=20)
        canvas.create_window(300, 425, window=b1)
        b2 = Button(user_registration_root, text='Next',command=next_image ,font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 425, window=b2)
        user_registration_root.mainloop()
    def image_grayscale(self):
        image_grayscale_root = Toplevel()
        image_grayscale_root.attributes('-topmost', 'true')
        get_data = ar_vein()
        w = 950
        h = 600
        ws = image_grayscale_root.winfo_screenwidth()
        hs = image_grayscale_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        image_grayscale_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        image_grayscale_root.title(get_data.get_title())
        image_grayscale_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        canvas = Canvas(image_grayscale_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        admin_id2 = canvas.create_text(500, 70, text="IMAGE GRAYSCALE", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(250, 195, text="RGB IMAGE", font=("Times New Roman", 15),
                                       fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(580, 195, text="GRAYSCALE IMGE", font=("Times New Roman", 15),
                                       fill=get_data.get_text_color())
        filapath = 'data\input.png'
        img = Image.open(filapath).convert('L')
        img.save('data\greyscale.png')
        def select_image():
            canvas.itemconfig(image_id2, state='normal')
            canvas.update()
            time.sleep(1)
        def next_image():
            image_grayscale_root.destroy()
            tt = ar_vein()
            tt.median_filter()
        image1 = Image.open('data/input.png')
        img1 = image1.resize((250, 250))
        my_img = ImageTk.PhotoImage(img1)
        image_id1 = canvas.create_image(300, 350, image=my_img)
        image1 = Image.open('data/greyscale.png')
        img1 = image1.resize((250, 250))
        my_img1 = ImageTk.PhotoImage(img1)
        global image_id2
        image_id2 = canvas.create_image(600, 350,  image=my_img1, state='hidden')
        b1 = Button(image_grayscale_root, text='Grayscale', command=lambda:select_image(), font=('times', 15, ' bold '),width=20)
        b1.pack()
        canvas.create_window(300, 525, window=b1)
        b2 = Button(image_grayscale_root, text='Next', command=next_image, font=('times', 15, ' bold '), width=20)
        canvas.create_window(600, 525, window=b2)
        image_grayscale_root.mainloop()
    def median_filter(self):
        median_filter_root = Toplevel()
        median_filter_root.attributes('-topmost', 'true')
        get_data = ar_vein()
        w = 950
        h = 600
        ws = median_filter_root.winfo_screenwidth()
        hs = median_filter_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        median_filter_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        median_filter_root.title(get_data.get_title())
        median_filter_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        canvas = Canvas(median_filter_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        admin_id2 = canvas.create_text(500, 70, text="NOISE REMOVE", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(200, 195, text="GRAYSCALE IMAGE", font=("Times New Roman", 15),
                                       fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(500, 195, text="DCT FILTER", font=("Times New Roman", 15),
                                       fill=get_data.get_text_color())
        def select_image():
            canvas.itemconfig(image_id2, state='normal')
            canvas.update()
            time.sleep(1)
        def next_image():
            median_filter_root.destroy()
            tt = ar_vein()
            tt.boundary_detection()
        image1 = Image.open('data/greyscale.png')
        img1 = image1.resize((250, 250))
        my_img = ImageTk.PhotoImage(img1)
        image_id1 = canvas.create_image(300, 350, image=my_img)
        def dct2(a):
            return dct(dct(a.T, norm='ortho').T, norm='ortho')
        def dct1(a):
            return idct(idct(a.T, norm='ortho').T, norm='ortho')
        im = (imread(r'data/input.png'))
        imF = dct2(im)
        im1 = dct1(imF)
        dd = np.allclose(im, im1)
        np.allclose(im, im1)
        path=('data\dct.png')
        cv2.imwrite(path, im1)
        image1 = Image.open('data/dct.png')
        img1 = image1.resize((250, 250))
        my_img1 = ImageTk.PhotoImage(img1)
        global image_id2
        image_id2 = canvas.create_image(600, 350, image=my_img1, state='hidden')
        b1 = Button(median_filter_root, text='DCT Filter', command=lambda: select_image(),
                    font=('times', 15, ' bold '), width=20)
        b1.pack()
        canvas.create_window(300, 525, window=b1)
        b2 = Button(median_filter_root, text='Next', command=next_image, font=('times', 15, ' bold '), width=20)
        canvas.create_window(600, 525, window=b2)
        median_filter_root.mainloop()
    def boundary_detection(self):
        boundary_detection_root = Toplevel()
        boundary_detection_root.attributes('-topmost', 'true')
        get_data = ar_vein()
        w = 950
        h = 600
        ws = boundary_detection_root.winfo_screenwidth()
        hs = boundary_detection_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        boundary_detection_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        boundary_detection_root.title(get_data.get_title())
        boundary_detection_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        canvas = Canvas(boundary_detection_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        # canvas.create_text(390, 20, text=get_data.get_title(), font=("Times New Roman", 24), fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(500, 70, text="BOUNDARY DETECTION", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(250, 195, text="DCT FILTER", font=("Times New Roman", 15),
                                       fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(550, 195, text="DETECTION", font=("Times New Roman", 15),
                                       fill=get_data.get_text_color())
        def select_image():
            canvas.itemconfig(image_id2, state='normal')
            canvas.update()
            time.sleep(1)
        def next_image():
            boundary_detection_root.destroy()
            tt = ar_vein()
            tt.morphological_processing()
        image1 = Image.open('data/dct.png')
        img1 = image1.resize((250, 250))
        my_img = ImageTk.PhotoImage(img1)
        image_id1 = canvas.create_image(300, 350, image=my_img)
        im = (imread(r'data/input.png'))
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 20, 30)
        edges_high_thresh = cv2.Canny(gray, 60, 120)
        im1 = np.hstack((gray, edges, edges_high_thresh))
        path = ('data\\boundary.png')
        cv2.imwrite(path, edges_high_thresh)
        image1 = Image.open('data/boundary.png')
        img1 = image1.resize((250, 250))
        my_img1 = ImageTk.PhotoImage(img1)
        global image_id2
        image_id2 = canvas.create_image(600, 350, image=my_img1, state='hidden')
        b1 = Button(boundary_detection_root, text='BOUNDARY DETECTION', command=lambda: select_image(),
                    font=('times', 15, ' bold '), width=20)
        b1.pack()
        canvas.create_window(300, 525, window=b1)
        b2 = Button(boundary_detection_root, text='Next', command=next_image, font=('times', 15, ' bold '), width=20)
        canvas.create_window(600, 525, window=b2)
        boundary_detection_root.mainloop()
    def morphological_processing(self):
        morphological_processing_root = Toplevel()
        morphological_processing_root.attributes('-topmost', 'true')
        get_data = ar_vein()
        w = 950
        h = 600
        ws = morphological_processing_root.winfo_screenwidth()
        hs = morphological_processing_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        morphological_processing_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        morphological_processing_root.title(get_data.get_title())
        morphological_processing_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        canvas = Canvas(morphological_processing_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        admin_id2 = canvas.create_text(500, 70, text="MORPHOLOGICAL PROCESS", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(250, 195, text="DETECTION", font=("Times New Roman", 15),
                                       fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(550, 195, text="MORPHOLOGICAL", font=("Times New Roman", 15),
                                       fill=get_data.get_text_color())
        def select_image():
            canvas.itemconfig(image_id2, state='normal')
            canvas.update()
            time.sleep(1)
        def next_image():
            morphological_processing_root.destroy()
            tt = ar_vein()
            tt.feature_extraction()
        image1 = Image.open('data/boundary.png')
        img1 = image1.resize((250, 250))
        my_img = ImageTk.PhotoImage(img1)
        image_id1 = canvas.create_image(300, 350, image=my_img)
        img = (imread(r'data/boundary.png'))
        binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        kernel = np.ones((5, 5), np.uint8)
        invert = cv2.bitwise_not(binr)
        erosion = cv2.erode(invert, kernel,
                            iterations=1)
        path='data/morphological.png'
        cv2.imwrite(path, erosion)
        image1 = Image.open('data/morphological.png')
        img1 = image1.resize((250, 250))
        my_img1 = ImageTk.PhotoImage(img1)
        global image_id2
        image_id2 = canvas.create_image(600, 350, image=my_img1, state='hidden')
        b1 = Button(morphological_processing_root, text='MORPHOLOGICAL', command=lambda: select_image(),
                    font=('times', 15, ' bold '), width=20)
        b1.pack()
        canvas.create_window(300, 525, window=b1)
        b2 = Button(morphological_processing_root, text='Next', command=next_image, font=('times', 15, ' bold '), width=20)
        canvas.create_window(600, 525, window=b2)
        morphological_processing_root.mainloop()
    def feature_extraction(self):
        feature_extraction_root = Toplevel()
        feature_extraction_root.attributes('-topmost', 'true')
        get_data = ar_vein()
        w = 950
        h = 600
        ws = feature_extraction_root.winfo_screenwidth()
        hs = feature_extraction_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        feature_extraction_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        feature_extraction_root.title(get_data.get_title())
        feature_extraction_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        canvas = Canvas(feature_extraction_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        admin_id2 = canvas.create_text(500, 70, text="FEATURE EXTRACTION", font=("Times New Roman", 24),
                                       fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(150, 195, text="MORPHOLOGICAL", font=("Times New Roman", 15),
                                       fill=get_data.get_text_color())
        global txt,txt2
        txt = canvas.create_text(500, 120, text="FEATURE EXTRACTION", font=("Times New Roman", 15),
                                       fill=get_data.get_text_color())
        txt2 = canvas.create_text(500, 170, text="ACCOUNT NO", font=("Times New Roman", 15),
                                 fill=get_data.get_text_color())
        def select_image():
            img = cv2.imread('data\\morphological.png', 0)
            from numpy import asarray
            numpydata = asarray(img)
            z = []
            for x in numpydata:
                for y in x:
                    z.append(int(y))
            nn = BPNNetwork([2, 2, 1])
            nn.auto_extract(z)
            feature_value = nn.result()
            get_data.feature_value=feature_value
            canvas.itemconfig(txt, text="Feature Value : "+str(feature_value))
        def next_image():
            acno = e11.get()
            name = e1.get()
            contact = e2.get()
            email = e3.get()
            address = e4.get()
            username = e5.get()
            password = e6.get()
            dd=0
            if "@" in email:
                dd=0
            else:
                dd=1


            if (acno == ""):
                messagebox.showinfo(title="Alert", message="Enter Account No", parent=feature_extraction_root)
            elif (name == ""):
                messagebox.showinfo(title="Alert", message="Enter Name", parent=feature_extraction_root)
            elif (contact == ""):
                messagebox.showinfo(title="Alert", message="Enter Contact", parent=feature_extraction_root)
            elif (email == ""):
                messagebox.showinfo(title="Alert", message="Enter Email", parent=feature_extraction_root)
            elif (dd==1):
                messagebox.showinfo(title="Alert", message="Enter Valid Email", parent=feature_extraction_root)
            elif (address == ""):
                messagebox.showinfo(title="Alert", message="Enter Address", parent=feature_extraction_root)
            elif (username == ""):
                messagebox.showinfo(title="Alert", message="Enter Username", parent=feature_extraction_root)
            elif (password == ""):
                messagebox.showinfo(title="Alert", message="Enter Password", parent=feature_extraction_root)
            else:
                maxin = mm.find_max_id("user_details")
                qry = ("insert into user_details values('" + str(maxin) + "','" + str(acno) + "','" + str(name) + "','" + str(
                    contact) + "','" + str(email) + "','" + str(address) + "','" + str(username) + "','" + str(
                    password) + "','0','"+str(get_data.feature_value)+"')")
                result = mm.insert_query(qry)
                messagebox.showinfo(title="Alert", message="Registration Success", parent=feature_extraction_root)
                feature_extraction_root.destroy()
        image1 = Image.open('data/morphological.png')
        img1 = image1.resize((250, 250))
        my_img = ImageTk.PhotoImage(img1)
        image_id1 = canvas.create_image(200, 350, image=my_img)
        admin_id2 = canvas.create_text(500, 220, text="Name", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(500, 270, text="Contact", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(500, 320, text="Email", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(500, 370, text="Address", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(500, 420, text="Username", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(500, 470, text="Password", font=("Times New Roman", 24),
                                        fill=get_data.get_text_color())
        e11 = Entry(canvas, font=('times', 15, ' bold '))
        canvas.create_window(680, 170, window=e11)
        e1 = Entry(canvas, font=('times', 15, ' bold '))
        canvas.create_window(680, 220, window=e1)
        e2 = Entry(canvas, font=('times', 15, ' bold '))
        canvas.create_window(680, 270, window=e2)
        e3 = Entry(canvas, font=('times', 15, ' bold '))
        canvas.create_window(680, 320, window=e3)
        e4 = Entry(canvas, font=('times', 15, ' bold '))
        canvas.create_window(680, 370, window=e4)
        e5 = Entry(canvas, font=('times', 15, ' bold '))
        canvas.create_window(680, 420, window=e5)
        e6 = Entry(canvas, font=('times', 15, ' bold '))
        canvas.create_window(680, 470, window=e6)
        b1 = Button(feature_extraction_root, text='feature_extraction', command=lambda: select_image(),font=('times', 15, ' bold '), width=20)
        b1.pack()
        canvas.create_window(200, 525, window=b1)
        b2 = Button(feature_extraction_root, text='Register', command=next_image, font=('times', 15, ' bold '),
                    width=20)
        canvas.create_window(700, 525, window=b2)
        feature_extraction_root.mainloop()
    def user_login(self):
        user_login_root = Toplevel()
        user_login_root.attributes('-topmost', 'true')
        get_data = ar_vein()
        w = 950
        h = 600
        ws = user_login_root.winfo_screenwidth()
        hs = user_login_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_login_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        user_login_root.title(get_data.get_title())
        user_login_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        canvas = Canvas(user_login_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        admin_id2 = canvas.create_text(500, 70, text="USER LOGIN", font=("Times New Roman", 24), fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(200, 200, text="PATH", font=("Times New Roman", 24), fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(200, 325, text="FILE", font=("Times New Roman", 24), fill=get_data.get_text_color())
        e1 = Entry(user_login_root, font=('times', 15, ' bold '),width=40)
        canvas.create_window(480, 200, window=e1)
        e2 = Entry(user_login_root, font=('times', 15, ' bold '),width=40)
        canvas.create_window(480, 325, window=e2)
        def select_image():
            dir = r'data'
            if not os.path.exists(dir):
                os.mkdir(dir)
            for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))
            if not os.path.exists(dir):
                os.makedirs(dir)
            csv_file_path = askopenfilename( parent=user_login_root)
            fpath = os.path.dirname(os.path.abspath(csv_file_path))
            fname = (os.path.basename(csv_file_path))
            fsize = os.path.getsize(csv_file_path)
            e1.delete(0, END)
            e1.insert(0, fpath)
            e2.insert(0, fname)
            get_data.path=os.path.abspath(csv_file_path)
            destination=os.path.join("data","input.png")
            print(destination)
            shutil.copy(os.path.abspath(csv_file_path), destination)
        def next_image():
            filapath = 'data\input.png'
            img = Image.open(filapath).convert('L')
            img.save('data\greyscale.png')
            ###############################
            def dct2(a):
                return dct(dct(a.T, norm='ortho').T, norm='ortho')
            def dct1(a):
                return idct(idct(a.T, norm='ortho').T, norm='ortho')
            im = (imread(r'data/input.png'))
            imF = dct2(im)
            im1 = dct1(imF)
            dd = np.allclose(im, im1)
            np.allclose(im, im1)
            path = ('data\dct.png')
            cv2.imwrite(path, im1)
            ##############################
            im = (imread(r'data/input.png'))
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 20, 30)
            edges_high_thresh = cv2.Canny(gray, 60, 120)
            im1 = np.hstack((gray, edges, edges_high_thresh))
            path = ('data\\boundary.png')
            cv2.imwrite(path, edges_high_thresh)
            ################################
            img = (imread(r'data/boundary.png'))
            binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            kernel = np.ones((5, 5), np.uint8)
            invert = cv2.bitwise_not(binr)
            erosion = cv2.erode(invert, kernel,iterations=1)
            path = 'data/morphological.png'
            cv2.imwrite(path, erosion)
            ####################################
            img = cv2.imread('data\\morphological.png', 0)
            from numpy import asarray
            numpydata = asarray(img)
            z = []
            for x in numpydata:
                for y in x:
                    z.append(int(y))
            nn = BPNNetwork([2, 2, 1])
            nn.auto_extract(z)
            feature_value = nn.result()
            get_data.feature_value = feature_value
            ###########################################
            qry="select * from user_details where report='"+str(feature_value)+"'"
            data=mm.select_direct_query(qry)
            if len(data)==0:
                messagebox.showerror("Result","Login Failed",parent=user_login_root)
            else:
                account_no=data[0][1]
                password1=data[0][7]
                get_data.set_account_no(account_no)
                password = tkinter.simpledialog.askstring("Password", "Enter password:", show='*',parent=user_login_root)
                if password==password1:
                    messagebox.showinfo("Result", "Login Success", parent=user_login_root)
                    user_login_root.destroy()
                    tt = ar_vein()
                    tt.user_home(account_no)
                else:
                    messagebox.showerror("Result", "Login Failed", parent=user_login_root)
        b1 = Button(user_login_root,text='Select Image',command=select_image ,font=('times', 15, ' bold '), width=20)
        canvas.create_window(300, 425, window=b1)
        b2 = Button(user_login_root, text='Next',command=next_image ,font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 425, window=b2)
        user_login_root.mainloop()
    def user_home(self,account_no):
        user_home_root =Toplevel()
        w = 950
        h = 600
        ws = user_home_root.winfo_screenwidth()
        hs = user_home_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_home_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        user_home_root.title(self.title)
        user_home_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=self.backround_image)
        canvas = Canvas(user_home_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(470, 40, text=self.titlec, font=("Times New Roman", 24), fill=self.text_color)
        def deposit(event):
            tt = ar_vein
            tt.user_deposit(event,account_no)
        image = Image.open('images/deposit.png')
        img = image.resize((100, 100))
        my_img = ImageTk.PhotoImage(img)
        image_id = canvas.create_image(350, 170, image=my_img)
        canvas.tag_bind(image_id, "<1>", deposit)
        admin_id = canvas.create_text(520, 170, text="DEPOSIT", font=("Times New Roman", 15), fill=self.text_color)
        canvas.tag_bind(admin_id, "<1>", deposit)

        def withdraw(event):
            tt = ar_vein
            tt.user_withdraw(event,account_no)
        image2 = Image.open('images/withdrw.png')
        img2 = image2.resize((100, 100))
        my_img2 = ImageTk.PhotoImage(img2)
        image_id2 = canvas.create_image(350, 270, image=my_img2)
        canvas.tag_bind(image_id2, "<1>", withdraw)

        admin_id1 = canvas.create_text(520, 270, text="WITHDRAW", font=("Times New Roman", 15),fill=self.text_color)
        canvas.tag_bind(admin_id1, "<1>", withdraw)
        ###########################
        def transaction(event):
            tt = ar_vein
            tt.user_transaction(event,account_no)

        image1 = Image.open('images/transaction.png')
        img1 = image1.resize((100, 100))
        my_img1 = ImageTk.PhotoImage(img1)
        image_id1 = canvas.create_image(350, 370, image=my_img1)
        canvas.tag_bind(image_id1, "<1>", transaction)
        admin_id = canvas.create_text(520, 370, text="TRANSACTION", font=("Times New Roman", 15), fill=self.text_color)
        canvas.tag_bind(admin_id, "<1>", transaction)
        # ################################
        def mini(event):
            tt = ar_vein
            tt.user_ministatement(event,account_no)
        admin_id1 = canvas.create_text(520, 470, text="MINI STATEMENT", font=("Times New Roman", 15),fill=self.text_color)
        canvas.tag_bind(admin_id1, "<1>", mini)
        image3 = Image.open('images/mini.png')
        img3 = image3.resize((100, 100))
        my_img3 = ImageTk.PhotoImage(img3)
        image_id3 = canvas.create_image(350, 480, image=my_img3)
        canvas.tag_bind(image_id3, "<1>", mini)
        user_home_root.mainloop()
    def user_deposit(self,account_no):
        user_deposit_root = Toplevel()
        get_data = ar_vein()
        user_deposit_root.attributes('-topmost', 'true')
        w = 550
        h = 350
        ws = user_deposit_root.winfo_screenwidth()
        hs = user_deposit_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_deposit_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        user_deposit_root.title(get_data.get_title())
        user_deposit_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        canvas = Canvas(user_deposit_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        admin_id2 = canvas.create_text(280, 70, text="DEPOSIT", font=("Times New Roman", 24),fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(180, 140, text="Amount", font=("Times New Roman", 24),fill=get_data.get_text_color())
        e1 = Entry(user_deposit_root, font=('times', 15, ' bold '), width=10)
        canvas.create_window(320, 140, window=e1)
        def select_image():
            amount=int(e1.get())
            qry="select balance from user_details where account_no='" + str(account_no) + "'"
            data=mm.select_direct_query(qry)
            bal = int(data[0][0]) + int(amount)
            mm.insert_query("update user_details set balance='" + str(bal) + "' where account_no='" + str(account_no) + "'")
            process = "Deposit"
            date = datetime.datetime.today()
            time = date.strftime("%I:%M %p")
            mm.insert_query("insert into mini values('" + str(process) + "','" + str(amount) + "','-','" + str(date) + "','" + str(time) + "','" + str(account_no) + "')")
            messagebox.showinfo(title='message', message='success',parent=user_deposit_root)
            user_deposit_root.destroy()
        b1 = Button(user_deposit_root, text='Deposit', command=select_image, font=('times', 15, ' bold '),width=20)
        canvas.create_window(280, 230, window=b1)
        user_deposit_root.mainloop()
    def user_withdraw(self,account_no):
        user_withdraw_root = Toplevel()
        get_data = ar_vein()
        user_withdraw_root.attributes('-topmost', 'true')
        w = 550
        h = 350
        ws = user_withdraw_root.winfo_screenwidth()
        hs = user_withdraw_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_withdraw_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        user_withdraw_root.title(get_data.get_title())
        user_withdraw_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        canvas = Canvas(user_withdraw_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        admin_id2 = canvas.create_text(280, 70, text="WITHDRAW", font=("Times New Roman", 24),fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(180, 140, text="Amount", font=("Times New Roman", 24),fill=get_data.get_text_color())
        e1 = Entry(user_withdraw_root, font=('times', 15, ' bold '), width=10)
        canvas.create_window(320, 140, window=e1)
        def select_image():
            amount=int(e1.get())
            qry="select balance from user_details where account_no='" + str(account_no) + "'"
            data=mm.select_direct_query(qry)
            xx=int(data[0][0])
            if amount<=xx:
                bal = int(data[0][0]) - int(amount)
                mm.insert_query(
                    "update user_details set balance='" + str(bal) + "' where account_no='" + str(account_no) + "'")
                process = "Withdraw"
                date = datetime.datetime.today()
                time = date.strftime("%I:%M %p")
                mm.insert_query("insert into mini values('" + str(process) + "','" + str(amount) + "','-','" + str(date) + "','" + str(time) + "','" + str(account_no) + "')")
                messagebox.showinfo(title='message', message='success', parent=user_withdraw_root)
                user_withdraw_root.destroy()
            else:
                messagebox.showinfo(title='message', message='Low Balance', parent=user_withdraw_root)
        b1 = Button(user_withdraw_root, text='Withdraw', command=select_image, font=('times', 15, ' bold '),width=20)
        canvas.create_window(280, 230, window=b1)
        user_withdraw_root.mainloop()
    def user_transaction(self,account_no):
        user_transaction_root = Toplevel()
        get_data = ar_vein()
        user_transaction_root.attributes('-topmost', 'true')
        w = 550
        h = 350
        ws = user_transaction_root.winfo_screenwidth()
        hs = user_transaction_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_transaction_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        user_transaction_root.title(get_data.get_title())
        user_transaction_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        canvas = Canvas(user_transaction_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        admin_id2 = canvas.create_text(280, 70, text="TRANSACTION", font=("Times New Roman", 24),fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(180, 140, text="Amount", font=("Times New Roman", 24),fill=get_data.get_text_color())
        admin_id2 = canvas.create_text(180, 180, text="Account No", font=("Times New Roman", 24),fill=get_data.get_text_color())
        e1 = Entry(user_transaction_root, font=('times', 15, ' bold '), width=10)
        canvas.create_window(320, 140, window=e1)
        e2 = Entry(user_transaction_root, font=('times', 15, ' bold '), width=10)
        canvas.create_window(320, 180, window=e2)
        def select_image():
            amount=int(e1.get())
            receiver=int(e2.get())
            qry="select balance from user_details where account_no='" + str(account_no) + "'"
            data=mm.select_direct_query(qry)
            xx=int(data[0][0])
            if amount<=xx:
                bal = int(data[0][0]) - int(amount)
                mm.insert_query(
                    "update user_details set balance='" + str(bal) + "' where account_no='" + str(account_no) + "'")
                process = "Debit"
                date = datetime.datetime.today()
                time = date.strftime("%I:%M %p")
                mm.insert_query("insert into mini values('" + str(process) + "','" + str(amount) + "','" + str(receiver) + "','" + str(date) + "','" + str(time) + "','" + str(account_no) + "')")
                #############
                qry = "select balance from user_details where account_no='" + str(receiver) + "'"
                data = mm.select_direct_query(qry)
                if len(data) >0:
                    bal = int(data[0][0]) + int(amount)
                    mm.insert_query(
                        "update user_details set balance='" + str(bal) + "' where account_no='" + str(receiver) + "'")
                    process = "Credit"
                    date = datetime.datetime.today()
                    time = date.strftime("%I:%M %p")
                    mm.insert_query("insert into mini values('" + str(process) + "','" + str(amount) + "','" + str(
                        account_no) + "','" + str(date) + "','" + str(time) + "','" + str(receiver) + "')")
                else:
                    messagebox.showinfo(title='message', message='Check Accont No', parent=user_transaction_root)
                ###############
                messagebox.showinfo(title='message', message='success', parent=user_transaction_root)
                user_transaction_root.destroy()
            else:
                messagebox.showinfo(title='message', message='Low Balance', parent=user_transaction_root)
        b1 = Button(user_transaction_root, text='Transfer', command=select_image, font=('times', 15, ' bold '),width=20)
        canvas.create_window(280, 230, window=b1)
        user_transaction_root.mainloop()
    def user_ministatement(self,account_no):
        user_transaction_root = Toplevel()
        get_data = ar_vein()
        user_transaction_root.attributes('-topmost', 'true')
        w = 650
        h = 350
        ws = user_transaction_root.winfo_screenwidth()
        hs = user_transaction_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_transaction_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        user_transaction_root.title(get_data.get_title())
        user_transaction_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        canvas = Canvas(user_transaction_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        admin_id2 = canvas.create_text(310, 70, text="MINI STATEMENT", font=("Times New Roman", 24),fill=get_data.get_text_color())
        fram = Frame(canvas)
        fram.place(x=60, y=100, width=550, height=230)
        scrollbarx = Scrollbar(fram, orient=HORIZONTAL)
        scrollbary = Scrollbar(fram, orient=VERTICAL)
        tree = Treeview(fram, columns=("process", "amount", "accnumber", "date", "time"), yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        tree.heading('process', text="process", anchor=W)
        tree.heading('amount', text="amount", anchor=W)
        tree.heading('accnumber', text="accnumber", anchor=W)
        tree.heading('date', text="date", anchor=W)
        tree.heading('time', text="time", anchor=W)
        tree.column('#0', width=0)
        tree.column('#1', width=100)
        tree.column('#2', width=100)
        tree.column('#3', width=100)
        tree.column('#4', width=100)
        tree.pack()
        d1=mm.select_direct_query("select * from mini where  my_account='" + str(account_no) + "'")
        for data in d1:
            tree.insert("", 0, values=data)
        bb = mm.select_direct_query("select balance from user_details where account_no='" + str(account_no) + "'")
        admin_id2 = canvas.create_text(510, 20, text="Balance : "+str(bb[0][0]), font=("Times New Roman", 18),
                                       fill=get_data.get_text_color())
        user_transaction_root.mainloop()


ar=ar_vein()
root=ar.home_window()
# ar.user_home()