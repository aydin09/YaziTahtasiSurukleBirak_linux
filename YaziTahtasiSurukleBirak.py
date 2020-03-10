from tkinter import *
from tkinter import font
import os

class DragManager():

    listeDrop = []

    def __init__(self,widget,drag=True,drop=True):

        self.widget = widget

        self.drag = drag

        self.drop = drop

        if drag:

            self.add_dragable(self.widget)

        if drop:

            DragManager.listeDrop.append(self.widget)

    def add_dragable(self, widget):

        self.widget = widget

        self.widget.bind("<ButtonPress-1>", self.on_start)

        self.widget.bind("<B1-Motion>", self.on_drag)

        self.widget.bind("<ButtonRelease-1>", self.on_drop)

        self.widget["cursor"] = "hand1"

    def on_start(self, event):

        self.memoire = self.widget.cget("text")

        widgetDeplace = Label(pencere, text=self.memoire,fg="yellow", bg="grey",font=appHighlightFont,height = 3, width=5)

        self.icone = widgetDeplace

    def on_drag(self, event):

        xd = event.x_root

        yd = event.y_root

        self.icone.place(x=xd,y=yd)

    def on_drop(self, event):

        x,y = event.widget.winfo_pointerxy()

        self.icone.destroy()

        target = event.widget.winfo_containing(x,y)

        if target in DragManager.listeDrop:

            try:

                target.configure(text=self.memoire)

            except:

                pass

pencere = Tk()

pencere.title("Yazı Tahtası")
img=PhotoImage(file='yazi.png')
pencere.tk.call('wm','iconphoto',pencere._w,img)
pencere.tk_setPalette("light blue")
gen=pencere.winfo_screenwidth()
yuks=pencere.winfo_screenheight()
pencere.geometry("%dx%d+0+0"%(gen,yuks))

appHighlightFont = font.Font(family='TTKB Dik Temel Abece', size=12,weight='bold')

label=Label(text="gokselgursu@gmail.com --- http://www.egitimhane.com/",fg="black")
label.place(x=1010,y=670)

def temiz():
    pencere.destroy()
    os.system("python3 YaziTahtasiSurukleBirak.py")

temizle=Button(text='Temizle',command=temiz,font=appHighlightFont,height = 2, width=10,bg="red").place(x=911,y=605)


choix1 = Label(pencere, text="A",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix2 = Label(pencere, text="a",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix3 = Label(pencere, text="B",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix4 = Label(pencere, text="b",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix5 = Label(pencere, text="C",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix6 = Label(pencere, text="c",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix7 = Label(pencere, text="Ç",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix8 = Label(pencere, text="ç",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix9 = Label(pencere, text="D",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix10 = Label(pencere, text="d",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix11 = Label(pencere, text="E",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix12 = Label(pencere, text="e",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix13 = Label(pencere, text="F",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix14 = Label(pencere, text="f",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix15 = Label(pencere, text="G",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix16 = Label(pencere, text="g",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix17 = Label(pencere, text="Ğ",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix18 = Label(pencere, text="ğ",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix19 = Label(pencere, text="H",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix20 = Label(pencere, text="h",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix21 = Label(pencere, text="I",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix22 = Label(pencere, text="ı",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix23 = Label(pencere, text="İ",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix24 = Label(pencere, text="i",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix25 = Label(pencere, text="J",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix26 = Label(pencere, text="j",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix27 = Label(pencere, text="K",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix28 = Label(pencere, text="k",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix29 = Label(pencere, text="L",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix30 = Label(pencere, text="l",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix31 = Label(pencere, text="M",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix32 = Label(pencere, text="m",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix33 = Label(pencere, text="N",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix34 = Label(pencere, text="n",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix35 = Label(pencere, text="O",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix36 = Label(pencere, text="o",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix37 = Label(pencere, text="Ö",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix38 = Label(pencere, text="ö",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix39 = Label(pencere, text="P",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix40 = Label(pencere, text="p",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix41 = Label(pencere, text="R",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix42 = Label(pencere, text="r",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix43 = Label(pencere, text="S",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix44 = Label(pencere, text="s",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix45 = Label(pencere, text="Ş",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix46 = Label(pencere, text="ş",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix47 = Label(pencere, text="T",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix48 = Label(pencere, text="t",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix49 = Label(pencere, text="U",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix50 = Label(pencere, text="u",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix51 = Label(pencere, text="Ü",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix52 = Label(pencere, text="ü",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix53 = Label(pencere, text="V",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix54 = Label(pencere, text="v",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix55 = Label(pencere, text="Y",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix56 = Label(pencere, text="y",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix57 = Label(pencere, text="Z",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix58 = Label(pencere, text="z",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix59 = Label(pencere, text=".",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix60 = Label(pencere, text=",",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix61 = Label(pencere, text="?",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix62 = Label(pencere, text="'",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix63 = Label(pencere, text="!",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix64 = Label(pencere, text="-",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

choix65 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)


choix1.place(x=10,y=450)

choix2.place(x=63,y=450)

choix3.place(x=116,y=450)

choix4.place(x=169,y=450)

choix5.place(x=222,y=450)

choix6.place(x=275,y=450)

choix7.place(x=328,y=450)

choix8.place(x=381,y=450)

choix9.place(x=434,y=450)

choix10.place(x=487,y=450)

choix11.place(x=540,y=450)

choix12.place(x=593,y=450)

choix13.place(x=646,y=450)

choix14.place(x=699,y=450)

choix15.place(x=752,y=450)

choix16.place(x=805,y=450)

choix17.place(x=858,y=450)

choix18.place(x=911,y=450)

choix19.place(x=964,y=450)

choix20.place(x=1017,y=450)

choix21.place(x=1070,y=450)

choix22.place(x=1123,y=450)

choix23.place(x=1176,y=450)

choix24.place(x=1229,y=450)

choix25.place(x=10,y=525)

choix26.place(x=63,y=525)

choix27.place(x=116,y=525)

choix28.place(x=169,y=525)

choix29.place(x=222,y=525)

choix30.place(x=275,y=525)

choix31.place(x=328,y=525)

choix32.place(x=381,y=525)

choix33.place(x=434,y=525)

choix34.place(x=487,y=525)

choix35.place(x=540,y=525)

choix36.place(x=593,y=525)

choix37.place(x=646,y=525)

choix38.place(x=699,y=525)

choix39.place(x=752,y=525)

choix40.place(x=805,y=525)

choix41.place(x=858,y=525)

choix42.place(x=911,y=525)

choix43.place(x=964,y=525)

choix44.place(x=1017,y=525)

choix45.place(x=1070,y=525)

choix46.place(x=1123,y=525)

choix47.place(x=1176,y=525)

choix48.place(x=1229,y=525)

choix49.place(x=10,y=600)

choix50.place(x=63,y=600)

choix51.place(x=116,y=600)

choix52.place(x=169,y=600)

choix53.place(x=222,y=600)

choix54.place(x=275,y=600)

choix55.place(x=328,y=600)

choix56.place(x=381,y=600)

choix57.place(x=434,y=600)

choix58.place(x=487,y=600)

choix59.place(x=540,y=600)

choix60.place(x=593,y=600)

choix61.place(x=646,y=600)

choix62.place(x=699,y=600)

choix63.place(x=752,y=600)

choix64.place(x=805,y=600)

choix65.place(x=858,y=600)


zoneDrop1 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop2 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop3 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop4 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop5 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop6 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop7 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop8 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop9 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop10 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop11 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop12 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop13 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop14 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop15 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop16 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop17 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop18 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop19 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop20 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop21 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop22 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop23 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop24 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop25 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop26 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop27 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop28 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop29 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop30 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop31 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop32 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop33 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop34 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop35 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop36 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop37 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop38 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop39 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop40 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop41 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop42 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop43 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop44 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop45 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop46 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop47 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop48 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop49 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop50 = Label(pencere, text="",fg="black", bg="white",font=appHighlightFont,height = 3, width=5)

zoneDrop1.place(x=10,y=250)

zoneDrop2.place(x=63,y=250)

zoneDrop3.place(x=116,y=250)

zoneDrop4.place(x=169,y=250)

zoneDrop5.place(x=222,y=250)

zoneDrop6.place(x=275,y=250)

zoneDrop7.place(x=328,y=250)

zoneDrop8.place(x=381,y=250)

zoneDrop9.place(x=434,y=250)

zoneDrop10.place(x=487,y=250)

zoneDrop11.place(x=540,y=250)

zoneDrop12.place(x=593,y=250)

zoneDrop13.place(x=646,y=250)

zoneDrop14.place(x=699,y=250)

zoneDrop15.place(x=752,y=250)

zoneDrop16.place(x=805,y=250)

zoneDrop17.place(x=858,y=250)

zoneDrop18.place(x=911,y=250)

zoneDrop19.place(x=964,y=250)

zoneDrop20.place(x=1017,y=250)

zoneDrop21.place(x=1070,y=250)

zoneDrop22.place(x=1123,y=250)

zoneDrop23.place(x=1176,y=250)

zoneDrop24.place(x=1229,y=250)

zoneDrop25.place(x=1282,y=250)

zoneDrop26.place(x=10,y=340)

zoneDrop27.place(x=63,y=340)

zoneDrop28.place(x=116,y=340)

zoneDrop29.place(x=169,y=340)

zoneDrop30.place(x=222,y=340)

zoneDrop31.place(x=275,y=340)

zoneDrop32.place(x=328,y=340)

zoneDrop33.place(x=381,y=340)

zoneDrop34.place(x=434,y=340)

zoneDrop35.place(x=487,y=340)

zoneDrop36.place(x=540,y=340)

zoneDrop37.place(x=593,y=340)

zoneDrop38.place(x=646,y=340)

zoneDrop39.place(x=699,y=340)

zoneDrop40.place(x=752,y=340)

zoneDrop41.place(x=805,y=340)

zoneDrop42.place(x=858,y=340)

zoneDrop43.place(x=911,y=340)

zoneDrop44.place(x=964,y=340)

zoneDrop45.place(x=1017,y=340)

zoneDrop46.place(x=1070,y=340)

zoneDrop47.place(x=1123,y=340)

zoneDrop48.place(x=1176,y=340)

zoneDrop49.place(x=1229,y=340)

zoneDrop50.place(x=1282,y=340)


drag1 = DragManager(choix1,drag=True,drop=False)

drag2 = DragManager(choix2,drag=True,drop=False)

drag3 = DragManager(choix3,drag=True,drop=False)

drag4 = DragManager(choix4,drag=True,drop=False)

drag5 = DragManager(choix5,drag=True,drop=False)

drag6 = DragManager(choix6,drag=True,drop=False)

drag7 = DragManager(choix7,drag=True,drop=False)

drag8 = DragManager(choix8,drag=True,drop=False)

drag9 = DragManager(choix9,drag=True,drop=False)

drag10 = DragManager(choix10,drag=True,drop=False)

drag11 = DragManager(choix11,drag=True,drop=False)

drag12 = DragManager(choix12,drag=True,drop=False)

drag13 = DragManager(choix13,drag=True,drop=False)

drag14 = DragManager(choix14,drag=True,drop=False)

drag15 = DragManager(choix15,drag=True,drop=False)

drag16 = DragManager(choix16,drag=True,drop=False)

drag17 = DragManager(choix17,drag=True,drop=False)

drag18 = DragManager(choix18,drag=True,drop=False)

drag19 = DragManager(choix19,drag=True,drop=False)

drag20 = DragManager(choix20,drag=True,drop=False)

drag21 = DragManager(choix21,drag=True,drop=False)

drag22 = DragManager(choix22,drag=True,drop=False)

drag23 = DragManager(choix23,drag=True,drop=False)

drag24 = DragManager(choix24,drag=True,drop=False)

drag25 = DragManager(choix25,drag=True,drop=False)

drag26 = DragManager(choix26,drag=True,drop=False)

drag27 = DragManager(choix27,drag=True,drop=False)

drag28 = DragManager(choix28,drag=True,drop=False)

drag29 = DragManager(choix29,drag=True,drop=False)

drag30 = DragManager(choix30,drag=True,drop=False)

drag31 = DragManager(choix31,drag=True,drop=False)

drag32 = DragManager(choix32,drag=True,drop=False)

drag33 = DragManager(choix33,drag=True,drop=False)

drag34 = DragManager(choix34,drag=True,drop=False)

drag35 = DragManager(choix35,drag=True,drop=False)

drag36 = DragManager(choix36,drag=True,drop=False)

drag37 = DragManager(choix37,drag=True,drop=False)

drag38 = DragManager(choix38,drag=True,drop=False)

drag39 = DragManager(choix39,drag=True,drop=False)

drag40 = DragManager(choix40,drag=True,drop=False)

drag41 = DragManager(choix41,drag=True,drop=False)

drag42 = DragManager(choix42,drag=True,drop=False)

drag43 = DragManager(choix43,drag=True,drop=False)

drag44 = DragManager(choix44,drag=True,drop=False)

drag45 = DragManager(choix45,drag=True,drop=False)

drag46 = DragManager(choix46,drag=True,drop=False)

drag47 = DragManager(choix47,drag=True,drop=False)

drag48 = DragManager(choix48,drag=True,drop=False)

drag49 = DragManager(choix49,drag=True,drop=False)

drag50 = DragManager(choix50,drag=True,drop=False)

drag51 = DragManager(choix51,drag=True,drop=False)

drag52 = DragManager(choix52,drag=True,drop=False)

drag53 = DragManager(choix53,drag=True,drop=False)

drag54 = DragManager(choix54,drag=True,drop=False)

drag55 = DragManager(choix55,drag=True,drop=False)

drag56 = DragManager(choix56,drag=True,drop=False)

drag57 = DragManager(choix57,drag=True,drop=False)

drag58 = DragManager(choix58,drag=True,drop=False)

drag59 = DragManager(choix59,drag=True,drop=False)

drag60 = DragManager(choix60,drag=True,drop=False)

drag61 = DragManager(choix61,drag=True,drop=False)

drag62 = DragManager(choix62,drag=True,drop=False)

drag63 = DragManager(choix63,drag=True,drop=False)

drag64 = DragManager(choix64,drag=True,drop=False)

drag65 = DragManager(choix65,drag=True,drop=False)


drop1 = DragManager(zoneDrop1,drag=False,drop=True)

drop2 = DragManager(zoneDrop2,drag=False,drop=True)

drop3 = DragManager(zoneDrop3,drag=False,drop=True)

drop4 = DragManager(zoneDrop4,drag=False,drop=True)

drop5 = DragManager(zoneDrop5,drag=False,drop=True)

drop6 = DragManager(zoneDrop6,drag=False,drop=True)

drop7 = DragManager(zoneDrop7,drag=False,drop=True)

drop8 = DragManager(zoneDrop8,drag=False,drop=True)

drop9 = DragManager(zoneDrop9,drag=False,drop=True)

drop10 = DragManager(zoneDrop10,drag=False,drop=True)

drop11 = DragManager(zoneDrop11,drag=False,drop=True)

drop12 = DragManager(zoneDrop12,drag=False,drop=True)

drop13 = DragManager(zoneDrop13,drag=False,drop=True)

drop14 = DragManager(zoneDrop14,drag=False,drop=True)

drop15 = DragManager(zoneDrop15,drag=False,drop=True)

drop16 = DragManager(zoneDrop16,drag=False,drop=True)

drop17 = DragManager(zoneDrop17,drag=False,drop=True)

drop18 = DragManager(zoneDrop18,drag=False,drop=True)

drop19 = DragManager(zoneDrop19,drag=False,drop=True)

drop20 = DragManager(zoneDrop20,drag=False,drop=True)

drop21 = DragManager(zoneDrop21,drag=False,drop=True)

drop22 = DragManager(zoneDrop22,drag=False,drop=True)

drop23 = DragManager(zoneDrop23,drag=False,drop=True)

drop24 = DragManager(zoneDrop24,drag=False,drop=True)

drop25 = DragManager(zoneDrop25,drag=False,drop=True)

drop26 = DragManager(zoneDrop26,drag=False,drop=True)

drop27 = DragManager(zoneDrop27,drag=False,drop=True)

drop28 = DragManager(zoneDrop28,drag=False,drop=True)

drop29 = DragManager(zoneDrop29,drag=False,drop=True)

drop30 = DragManager(zoneDrop30,drag=False,drop=True)

drop31 = DragManager(zoneDrop31,drag=False,drop=True)

drop32 = DragManager(zoneDrop32,drag=False,drop=True)

drop33 = DragManager(zoneDrop33,drag=False,drop=True)

drop34 = DragManager(zoneDrop34,drag=False,drop=True)

drop35 = DragManager(zoneDrop35,drag=False,drop=True)

drop36 = DragManager(zoneDrop36,drag=False,drop=True)

drop37 = DragManager(zoneDrop37,drag=False,drop=True)

drop38 = DragManager(zoneDrop38,drag=False,drop=True)

drop39 = DragManager(zoneDrop39,drag=False,drop=True)

drop40 = DragManager(zoneDrop40,drag=False,drop=True)

drop41 = DragManager(zoneDrop41,drag=False,drop=True)

drop42 = DragManager(zoneDrop42,drag=False,drop=True)

drop43 = DragManager(zoneDrop43,drag=False,drop=True)

drop44 = DragManager(zoneDrop44,drag=False,drop=True)

drop45 = DragManager(zoneDrop45,drag=False,drop=True)

drop46 = DragManager(zoneDrop46,drag=False,drop=True)

drop47 = DragManager(zoneDrop47,drag=False,drop=True)

drop48 = DragManager(zoneDrop48,drag=False,drop=True)

drop49 = DragManager(zoneDrop49,drag=False,drop=True)

drop50 = DragManager(zoneDrop50,drag=False,drop=True)

pencere.mainloop()
