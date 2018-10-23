x=0
a=450
y=480
c=480
d=480
def setup():
    size(640,480)
def draw():
    global x 
    global a
    global y
    global c
    global d
    if x>=640:
        x=0
    x+=3
   
    if a<=0:
        a=640
    a-=3
    
    if c<=-200:
        c=750
    c-=3
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
    
    fill(224,17,95)     
    ellipse(15,y/2+15,20,30)    #BALLOON
    y -= 1
    line(15,y/2+15,20,30)
    
    fill("#C2D8B9")
    triangle(0,height, width, height, width/2, 200)
    fill (0,128,0)
    rect (0, height-50, width, 50)
    fill(255,255,0)
    ellipse(0, 0, 200, 200)
    
    fill(58, 95, 11)   #tree1
    ellipse(d-393,374,80,75)  
    fill("#663300")    
    rect(77,400,20,75)


    fill("#C0C0C0")
    rect(c,400,width/5,50) #CAR
    rect(c+40,375,50,50)
    fill(0,0,0)
    ellipse(c+25,450,35,35)
    ellipse(c+100,450,35,35)
    fill(145,168,209)
    rect(c+40,375,20,20)
    
    
    fill(58, 95, 11)   #tree2
    ellipse(d+8,374,80,75) 
    fill("#663300")    
    rect(477,400,20,75)
    
    
