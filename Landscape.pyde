x=0
a=450
y=480
def setup():
    size(640,480)
def draw():
    global x 
    global a
    global y
    if x>=640:
        x=0
    x+=3
   
    if a<=0:
        a=640
    a-=3
    background(135,206,235)
    fill(255)
    ellipse(x,height/6,50,50)
    ellipse(x+33,height/6,50,50)
    ellipse(x-33,height/6,50,50)
    ellipse(x-15,height/6+15,50,50)
    ellipse(x-15,height/6-15,50,50)
    ellipse(x+15,height/6-15,50,50)
    ellipse(x+15,height/6+15,50,50)
    
    ellipse(a,height/2,50,50)  #newcloud
    ellipse(a+33,height/2,50,50)
    ellipse(a-33,height/2,50,50)
    ellipse(a-15,height/2+15,50,50)
    ellipse(a-15,height/2-15,50,50)
    ellipse(a+15,height/2-15,50,50)
    ellipse(a+15,height/2+15,50,50)
    noStroke()
    
    ellipse(15,y/2+15,20,30)    #BALLOON
    y -= 1
    fill("#FF0000")
    
    fill("#C2D8B9")
    triangle(0,height, width, height, width/2, 200)
    fill (0,128,0)
    rect (0, height-50, width, 50)
    fill(255,255,0)
    ellipse(0, 0, 200, 200)
