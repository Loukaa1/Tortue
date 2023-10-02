import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.speed(0) # max

def equilateral(longueur):
    for _ in range(3):
        t.forward(longueur)
        t.left(120)
        
        
def carre(longueur):
    for _ in range(4):
        t.forward(longueur)
        t.left(90)
        
        
def polygone(longueur, nb_cotes):
    for _ in range(nb_cotes):
        t.forward(longueur)
        t.left (360/nb_cotes)
        
        
        
polygone (100, 7)       
# carre(300)        
# equilateral(300) # appel de la fonction

turtle.exitonclick()