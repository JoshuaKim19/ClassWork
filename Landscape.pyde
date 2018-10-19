x=0
def setup():
    size(640,480)
def draw():
    global x 
    if x>=640:
        x=0
    x+=3
    background(135,206,235)
    fill(255)
    ellipse(x,height/6,50,50)
    ellipse(x+33,height/6,50,50)
    ellipse(x-33,height/6,50,50)
    ellipse(x-15,height/6+15,50,50)
    ellipse(x-15,height/6-15,50,50)
    ellipse(x+15,height/6-15,50,50)
    ellipse(x+15,height/6+15,50,50)
    
    ellipse(x,height/2,50,50)  #newcloud
    ellipse(x+33,height/2,50,50)
    ellipse(x-33,height/2,50,50)
    ellipse(x-15,height/2+15,50,50)
    ellipse(x-15,height/2-15,50,50)
    ellipse(x+15,height/2-15,50,50)
    ellipse(x+15,height/2+15,50,50)
    noStroke()
    fill("#C2D8B9")
    triangle(0,height, width, height, width/2, 200)
    fill (0,128,0)
    rect (0, height-50, width, 50)
    fill(255,255,0)
    ellipse(0, 0, 200, 200)
