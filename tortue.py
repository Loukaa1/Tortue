import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.speed(0) # max

def equilateral(longueur):
    polygone(longueur, 3)
        
def carre(longueur):
    polygone(longueur, 4)
    
def polygone(longueur, nb_cotes):
    for _ in range(nb_cotes):
        t.forward(longueur)
        t.left (360/nb_cotes)
        
        
        
equilateral (200)
        
        
# carre(300)        
# equilateral(300) # appel de la fonction

turtle.exitonclick()