x=10
y=20
Verx=1
Very=1
raggio=50
xr=25


def setup ():
     size(600,400)
     
     
def draw():
    global x,y,Verx,Very,raggio,xr
    background(210, 0, 0)
    ellipse (x,y,30,30)
    x=x+(4*Verx)
    y=y+(4*Very)
    raggio=raggio+(1*Verx)
    if  y<0:
        Very*=-1
        fill (random(255),random(255),random(255))
    if y+25>height-25 and x>xr and x<=xr+80:
        Very*=-1
    if x>width or x<0:
        Verx*=-1   
        fill (random(255),random(255),random(255))
    rect(xr,height-25,80,25)
    if y>height:
        print ("hai perso")
        
def keyPressed():
    global xr
    if keyCode == LEFT:
        xr=xr-25
    if xr<=0-25:
        xr=0    
    if keyCode == RIGHT:
        xr=xr+25
    if xr>=width-80:
        xr=600-80
