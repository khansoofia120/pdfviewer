from tkinter import *
from tkinter import filedialog

from tkPDFViewer import tkPDFViewer as pdf
import os
 #initializing tk
root=Tk()
root.geometry("630x700+400+100")
root.title("PDF Viewer")
root.configure(bg="white")
def browseFiles():
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="select pdf file",filetypes=(("PDF File",".pdf"),("PDF File",".PDF"),("All File",".txt")))
    
    v1=pdf.ShowPdf()
    v2 = v1.pdf_view(root, pdf_location=filename, width=77, height=100)

    v2.pack(pady=(0,0))
    
Button(root,text="open",command=browseFiles,width=40,font="arial 20",bd=4).pack()
root.mainloop()

