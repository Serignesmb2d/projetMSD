import turtle as turtle
#fonction  de cercle
def cercle(r): 
    turtle.circle(r)
    
#fonction demi cercle
def demi_cercle(r): 
    turtle.circle(r, 180)

#fonction triangle
def triangle(longueur_cote):
    turtle.forward(longueur_cote)
    turtle.left(60)
    turtle.forward(longueur_cote)
    turtle.left(60)
    turtle.forward(longueur_cote)
#fonction de carre
def carre(longueur_cote):
    for i in range(4):
        turtle.forward(longueur_cote)
        turtle.left(90)

#fonction de rectangle
def rectangle(longueur, largeur):
    for i in range(2):
        turtle.forward(longueur)
        turtle.left(90)
        turtle.forward(largeur)
        turtle.left(90)
#fonction polygone
def polygone(n, cote):
    ang = 360/n
    for i in range(n):
        turtle.forward(cote)
        turtle.left(90)

def losange(longueur_cote):

    turtle.left(30)
    turtle.forward(longueur_cote)
    turtle.left(120)
    turtle.forward(longueur_cote)
    turtle.left(60)
    turtle.forward(longueur_cote)
    turtle.left(120)
    turtle.forward(longueur_cote)

def trapeze(longueur, largeur, hauteur):
    turtle.forward(longueur)
    turtle.left(120)
    turtle.forward(largeur)
    turtle.left(60)
    turtle.forward(hauteur)
    turtle.left(60)
    turtle.forward(largeur)

def elipse(x, y, z):
    turtle.shape("circle")
    turtle.fillcolor("white")
    turtle.shapesize(x, y, z)


    