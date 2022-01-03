import stddraw
import color

stddraw.setCanvasSize(1500,600)
stddraw.setXscale(0,250)
stddraw.setYscale(-40,100)

x=-70
left = True
right = False
c=0
y=0
stuck=True
up = False

while True==True:
    stddraw.clear()
    ##### static
    stddraw.setPenColor(color.Color(20,200,250)) #blue
    stddraw.filledSquare(0,0,250)
    stddraw.setPenColor(color.Color(50,200,100)) #green
    stddraw.filledRectangle(0,0,120,15)
    stddraw.filledPolygon([120,120,125],[0,15,3])
    stddraw.setPenColor(color.Color(150,100,50)) #brown
    stddraw.filledRectangle(0,-40,125,43)
    #####

    ##### moving
    stddraw.setPenColor(color.WHITE)
    stddraw.filledCircle(50+x,35+y,10)
    stddraw.filledRectangle(57+x,35+y,3,15)
    stddraw.filledCircle(60+x,50+y,4)

    stddraw.setPenColor(color.YELLOW)
    stddraw.filledPolygon([63+x,63+x,66+x],[48.5+y,50.5+y,49.5+y])

    stddraw.setPenColor(color.RED)
    stddraw.filledPolygon([58+x,59+x,60+x,61+x,62+x,61+x,59+x],[56+y,55+y,56+y,55+y,56+y,54+y,54+y])

    stddraw.setPenColor(color.BLACK)
    stddraw.filledCircle(61.2+x,51.2+y,0.8)

    if left == True and right == False and x<115:
        c+=0.5
        right=False
        stddraw.filledPolygon([46 + x, 46.8 + x, 46.8 + x, 46 + x], [26+y, 25.6+y, 18+y, 18+y])
        stddraw.filledPolygon([46.4 + x, 48.4 + x, 48.4 + x, 46.4 + x], [17.5+y, 17+y, 18+y, 18.5+y])
        stddraw.filledPolygon([46.4 + x, 45.4 + x, 45.4 + x, 46.4 + x], [17.5+y, 17+y, 18+y, 18.5+y])
        stddraw.filledPolygon([50 + x, 50.8 + x, 50.8 + x, 50 + x], [25+y, 25.1+y, 16+y, 16+y])
        stddraw.filledPolygon([50.4 + x, 52.4 + x, 52.4 + x, 50.4 + x], [15.5+y, 15+y, 16+y, 16.5+y])
        stddraw.filledPolygon([50.4 + x, 49.4 + x, 49.4 + x, 50.4 + x], [15.5+y, 15+y, 16+y, 16.5+y])
        if c>=10:
            left=False
            right=True
            c=0
    if right == True and left == False and x<115:
        c+=0.5
        left=False
        stddraw.filledPolygon([46 + x, 46.8 + x, 46.8 + x, 46 + x], [26+y, 25.6+y, 16+y, 16+y])
        stddraw.filledPolygon([46.4 + x, 48.4 + x, 48.4 + x, 46.4 + x], [15.5+y, 15+y, 16+y, 16.5+y])
        stddraw.filledPolygon([46.4 + x, 45.4 + x, 45.4 + x, 46.4 + x], [15.5+y, 15+y, 16+y, 16.5+y])
        stddraw.filledPolygon([50 + x, 50.8 + x, 50.8 + x, 50 + x], [25+y, 25.1+y, 18+y, 18+y])
        stddraw.filledPolygon([50.4 + x, 52.4 + x, 52.4 + x, 50.4 + x], [17.5+y, 17+y, 18+y, 18.5+y])
        stddraw.filledPolygon([50.4 + x, 49.4 + x, 49.4 + x, 50.4 + x], [17.5+y, 17+y, 18+y, 18.5+y])
        if c>=10:
            left=True
            right=False
            c=0
    if right == True and left == False and x>115:
        c+=0.5
        left=False
        stddraw.filledPolygon([46 + x, 46.8 + x, 46.8 + x, 46 + x], [26+y, 25.6+y, 16+y, 16+y])
        stddraw.filledPolygon([46.4 + x, 48.4 + x, 48.4 + x, 46.4 + x], [15.5+y, 15+y, 16+y, 16.5+y])
        stddraw.filledPolygon([46.4 + x, 45.4 + x, 45.4 + x, 46.4 + x], [15.5+y, 15+y, 16+y, 16.5+y])
        stddraw.filledPolygon([50 + x, 50.8 + x, 50.8 + x, 50 + x], [25+y, 25.1+y, 16+y, 16+y])
        stddraw.filledPolygon([50.4 + x, 52.4 + x, 52.4 + x, 50.4 + x], [15.5+y, 15+y, 16+y, 16.5+y])
        stddraw.filledPolygon([50.4 + x, 49.4 + x, 49.4 + x, 50.4 + x], [15.5+y, 15+y, 16+y, 16.5+y])
        if c>=10:
            left=True
            right=False
            c=0
    if right == False and left == True and x>115:
        c+=0.5
        left=False
        stddraw.filledPolygon([46 + x, 46.8 + x, 46.8 + x, 46 + x], [26+y, 25.6+y, 16+y, 16+y])
        stddraw.filledPolygon([46.4 + x, 48.4 + x, 48.4 + x, 46.4 + x], [15.5+y, 15+y, 16+y, 16.5+y])
        stddraw.filledPolygon([46.4 + x, 45.4 + x, 45.4 + x, 46.4 + x], [15.5+y, 15+y, 16+y, 16.5+y])
        stddraw.filledPolygon([50 + x, 50.8 + x, 50.8 + x, 50 + x], [25+y, 25.1+y, 16+y, 16+y])
        stddraw.filledPolygon([50.4 + x, 52.4 + x, 52.4 + x, 50.4 + x], [15.5+y, 15+y, 16+y, 16.5+y])
        stddraw.filledPolygon([50.4 + x, 49.4 + x, 49.4 + x, 50.4 + x], [15.5+y, 15+y, 16+y, 16.5+y])
        if c>=10:
            left=False
            right=True
            c=0


    x+=0.1
    if x>=88.7 and x<114.8:
        if stuck == True:
            stuck = False
            stddraw.show(500)
        y=y-2.5
    if x>=115:
        if up == False:
            up = True
            y=-80
        y=y+0.17
    #####
    stddraw.show(1)

