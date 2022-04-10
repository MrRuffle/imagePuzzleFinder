
import random

a = random.randint(0,400)
b = random.randint(0,400)
diff = 6

def setup():
    size(533,800)
    

    
def draw():
    noCursor()
    global a,b,diff
    img = loadImage("flower.jpg")
    image(img, 0, 0)
    if dist(mouseX-50, mouseY-50, a,b) <= diff:
        a = random.randint(0,400)
        b = random.randint(0,400)
        diff-=1
    if diff < 2:
        diff = 2
    z = get(a,b,100,100)
    
        
    image(z,mouseX-50,mouseY-50)
    
