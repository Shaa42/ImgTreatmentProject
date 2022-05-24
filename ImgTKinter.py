from ImgMod import IMAGE_TREAT
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

def FenetreTkinter(image : str):
    global ImgCanvas, _classImage

    # Creer une fenetre
    window = Tk()
    _classImage = IMAGE_TREAT(image)

    # personnaliser la fenetre
    window.title("ShaFX - Image Treatment")
    window.geometry("720x420")
    window.resizable(width=False, height=False)
    window.config(bg='#d9d7cc')

    """
    Work Zone
    """
    #File function
    # FIXME : Permettre le changement de fichier
    def changeFile():
        global _classImage, my_Img, Img_resized, Img, ImgCanvas
        _nomFichier = askopenfilename()
        print(_nomFichier)
        _classImage = IMAGE_TREAT(_nomFichier)

        my_Img = Image.open(_nomFichier)
        Img_resized = my_Img.resize((400, 400), Image.ANTIALIAS)
        Img = ImageTk.PhotoImage(Img_resized)
        ImgCanvas.create_image(1, 1, anchor='nw', image=Img)

    # Grille pour bouton en général
    Button_grid = Frame(window, bg='#d9d7cc')
    Button_grid.pack(ipadx=420 // 5, ipady=720, side='left')

    # Bouton pour fichier
    Button_file = Button(Button_grid, text='Select File',bd = 5 ,bg='white', relief='groove', command=changeFile)
    Button_file.pack(ipady=10, padx=10, pady=5, fill='both')

    # Boutons De Traitement
    Button_Display = Frame(Button_grid, bg='#bfb495', bd=3, relief='groove')
    Button_Display.pack(padx=10, pady=5, fill='both', expand=True)

    Button1 = Button(Button_Display, text='Grayscale', bd=3, command=lambda:_classImage.grayscale())
    Button1.pack(fill='both', pady=2, padx=5, expand=True)

    Button2 = Button(Button_Display, text='Random Substract', bd=3, command=lambda:_classImage.randomSubstract())
    Button2.pack(fill='both', pady=2, padx=5, expand=True)

    Button3 = Button(Button_Display, text='Random Index', bd=3, command=lambda:_classImage.randomIndex())
    Button3.pack(fill='both', pady=2, padx=5, expand=True)

    Button4 = Button(Button_Display, text='Rotate 90', bd=3, command=lambda:_classImage.rotate())
    Button4.pack(fill='both', pady=2, padx=5, expand=True)

    Button5 = Button(Button_Display, text='Negative', bd=3, command=lambda:_classImage.negative())
    Button5.pack(fill='both', pady=2, padx=5, expand=True)

    Button6 = Button(Button_Display, text='Show', bd=3, command=lambda:_classImage.show())
    Button6.pack(fill='both', pady=2, padx=5, expand=True)

    # Image
    Image_Display = Frame(window, bg='#827f78', bd=3, relief='groove')
    Image_Display.pack(ipadx=100, ipady=100, padx=5, pady=5, side='right', fill='both', expand=True)

    ImgCanvas = Canvas(Image_Display, width=720, height=420)
    ImgCanvas.pack(padx=2, pady=2)

    my_Img = Image.open(image)
    Img_resized = my_Img.resize((400, 400), Image.ANTIALIAS)
    Img = ImageTk.PhotoImage(Img_resized)

    ImgCanvas.create_image(1, 1, anchor='nw', image=Img)

    # afficher la fenetre
    window.mainloop()
