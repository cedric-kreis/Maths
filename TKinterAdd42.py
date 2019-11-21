# -*- coding: utf-8 -#-
#-------------------------------------------------------------------------------
#
# Auteur        : Cédric Kreis
# Programme     : Additionne plus 42
# Tkinter       : Programme avec interface graphique
# Fonctions     : L'utilisateur insère un chffire ou nombre dans la 'entry box'
#                 et la fonction ajoute 42 à celui-ci.
# Création      : 21.11.2019
# Modifié le    :
# Version       : 1
# OS            : MacOSX
# Python        : 2.7.10
#
#-------------------------------------------------------------------------------
from Tkinter import *

MyWindows = Tk()
MyWindows.title("Ajoute 42 à un entier")
MyWindows.geometry("230x150")
MyWindows.resizable(width=False, height=False)

def imprimer() :

    A = EA.get()
    B = int(A)
    C = B + 42
    L.config(text = C)



L0 = Label(MyWindows, text = "Entrez une valeur :")

LA = Label(MyWindows, text = "Entier :")
EA = Entry(MyWindows, width = 3)


B = Button(MyWindows, text="Calculer", command = imprimer)

Lres = Label(MyWindows, text = "Résultat : ")
L = Label(MyWindows)


EA.place(x = 80, y = 40)

L0.place(x = 10, y = 10)
LA.place(x = 10, y = 40)


B.place(x = 80, y = 70)
Lres.place(x = 10, y = 100)
L.place(x = 80, y = 100)

MyWindows.mainloop()
