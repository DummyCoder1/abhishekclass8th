l1 = [10,20,30,40,50,60,70,80,90,100,110,120]
l2 = ["red","blue","pink","green","yellow","cyan","black","orange","grey","purple"]
import turtle,random
def draw_lines(a,b):
    for value in a:
        turtle.forward(value)
        turtle.pencolor(random.choice(b))
        turtle.stamp()
        turtle.backward(value)
        turtle.right(30)
draw_lines(l1,l2)
        