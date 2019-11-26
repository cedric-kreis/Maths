# -*- coding: utf-8 -#-
#-------------------------------------------------------------------------------
#
# Auteur        : Cédric Kreis
# Programme     : Additionne plus 42 et contrôle d'entrée
# Tkinter       : Programme avec interface graphique
# Fonctions     : L'utilisateur insère un chffire ou nombre dans la 'entry box'
#                 et la fonction ajoute 42 à celui-ci.
# Création      : 21.11.2019
# Modifié le    : 26.22.2019
# Version       : 1.3
#
# Modification  : 1.1 -> REGEX pour contrôle
#                 1.2 -> popup
#                 1.3 -> Alerte sonore
#
# OS            : MacOSX
# Python        : 2.7.10
#
#   Install pip for MACOSX && install playsound
#   1 -> curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
#   2 -> sudo python get-pip.py
#   3 -> pip install playsound
#
#-------------------------------------------------------------------------------

from Tkinter import *               # Module pour la fenêtre
from playsound import playsound     # Module pour le son
import tkMessageBox                 # Module pour les popup
import re                           # Module pour les REGEX

MyWindows = Tk()
MyWindows.title("Ajoute 42 à un entier")
MyWindows.geometry("230x150")
MyWindows.resizable(width=False, height=False)


def imprimer() :

    A = EA.get()

    if (re.search("^[0-9]+$", A)):
        B = int(A)
        C = B + 42
        L.config(text = C)

    else:
        playsound('SF.mp3')
        tkMessageBox.showerror("Error", "Entrer un chiffre ou un nombre!")


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

