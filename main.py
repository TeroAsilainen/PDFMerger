from tkinter import *
from tkinter import filedialog
from pypdf import PdfWriter

root = Tk()
root.title("PDFM - PDF Merger")
root.iconbitmap("PDFM.ico")

# Keep track of files selected
file1selected = False
file2selected = False

pdflist = []
file2namee = ""
file1namee = ""


# File selector
def file1selector():
    global entry1, file1selected, file2selected, file1namee, file2namee
    root.file1name = filedialog.askopenfilename(initialdir="/", title="Select File 1", filetypes=(("PDF Files", "*.pdf"),))
    entry1.config(text=str(root.file1name))
    if root.file1name != "":
        file1selected = True
        file1namee = str(root.file1name)
    if root.file1name == "":
        file1selected = False
        btnM.config(state="disabled")

    if file1selected and file2selected:
        btnM.config(state="normal")


def file2selector():
    global entry1, file1selected, file2selected, file1namee, file2namee
    root.file2name = filedialog.askopenfilename(initialdir="/", title="Select File 2", filetypes=(("PDF Files", "*.pdf"),))
    entry2.config(text=str(root.file2name))
    if root.file2name != "":
        file2selected = True
        file2namee = str(root.file2name)
    if root.file2name == "":
        file2selected = False
        btnM.config(state="disabled")

    if file1selected and file2selected:
        btnM.config(state="normal")


# Define a function to handle merging
def mergerfunction():
    global file1namee, file2namee, pdflist, mergelabel
    merger = PdfWriter()
    # Empty pdflist before updating
    pdflist = []
    # Update the pdflist with latest filenames, to only add two files
    pdflist.insert(0, str(file1namee))
    pdflist.insert(1, str(file2namee))
    for pdf in pdflist:
        merger.append(pdf)
    root.savefile = filedialog.asksaveasfilename(initialfile="Untitled.pdf",defaultextension=".pdf", initialdir="/", title="Save as...", filetypes=(("PDF Files", "*.pdf"),))

    merger.write(root.savefile)
    merger.close()
    mergelabel.config(text="Files merged\nsuccesfully!")


# Intro Label above everything
introlabel = Label(root, text="Select two PDF Files to merge them.", padx=10, pady=10)
introlabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Create Labels for file numbers
file1label = Label(root, text="File 1: ")
file2label = Label(root, text="File 2: ")
file1label.grid(row=1, column=0, pady=10, padx=5)
file2label.grid(row=2, column=0, pady=10, padx=5)

# Entry labels for file paths
entry1 = Label(root, width=25, relief="groove", background="#ffffff")
entry1.grid(row=1, column=1)
entry2 = Label(root, width=25, relief="groove", background="#ffffff")
entry2.grid(row=2, column=1)

# Browse buttons for files
btn1 = Button(root, text="Browse...", padx=5, command=file1selector)
btn1.grid(row=1, column=2, padx=10, pady=5)
btn2 = Button(root, text="Browse...", padx=5, command=file2selector)
btn2.grid(row=2, column=2, padx=10, pady=5)

# Button for Merge
btnM = Button(root, text="Merge Files", state="disabled", padx=25, command=mergerfunction)
btnM.grid(row=3, column=1, pady=10)

# Label for File merged message
mergelabel = Label(root, text="", width=10, padx=5)
mergelabel.grid(row=3, column=2)

# Status Bar with some info
statusBar = Label(root, text="PDF Merger by Tero Asilainen.\nMade with tkinter and pypdf.", relief="sunken")
statusBar.grid(row=4, column=0, columnspan=3, sticky=W+E)

if __name__ == "__main__":
    root.mainloop()
