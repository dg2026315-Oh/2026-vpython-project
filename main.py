Web VPython 3.2
box(size = vec(80,38,0.1), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWMjgYCO8lNv0o1IZAcitLuEgYpwcgb5vshy6B2Vud6CQiQc3OqFtIMSN9&s=10" )
cylinder(axis = vec(0,1,0), pos = vec(0, -18, 0.5), size = vec(16, 4, 5))
ball = box(size = vec(6,6,0.1), pos = vec(-25,-15,0.5),texture = "https://png.pngtree.com/png-vector/20191022/ourlarge/pngtree-f-grade-vector-fail-exam-mark-isolated-flat-cartoon-illustration-png-image_1846214.jpg" )

    
c1 = sphere (pos = vec(0,0,0), size = vec(11,10,10), color = vec(247/255, 225/255, 162/255))
c2 = sphere (pos = vec(0,5.3,0), size = vec(2,2,2), color = vec(243/255, 213/255, 130/255))
c3 = sphere (pos = vec(-1.5,5.1,0), size = vec(2,2,2), color = vec(243/255, 213/255, 130/255))
c4 = sphere (pos = vec(1.5,5.1,0), size = vec(2,2,2), color  = vec(243/255, 213/255, 130/255))
c5 = sphere (pos = vec(-2,0.3,5), size = vec(1.2,1.3,1.3), color = color.black)
c6 = sphere (pos = vec(2,0.3,5), size = vec(1.2,1.3,1.3), color = color.black)


b8 = box(color = color.black, size = vec(1,0.1,1), pos=vec(0,-1.5,5))
b9 = box(color = color.black, size = vec(1,0.1,1), pos=vec(2.2,1.5,5))
b10 = box(color = color.black, size = vec(1,0.1,1), pos=vec(-2.2,1.5,5))

ball.v = vec(10,25,0)

x = compound([c1, c2, c3, c4, c5, c6, b8, b9, b10])
x.pos = vec(25,-13,0)
    
while True : 
    rate(100)
    ball.pos = ball.pos + ball.v * 0.01
    ball.v.y = ball.v.y + -9.8 * 0.01
    if ball.pos.y < -20 : 
        ball.v.y = -ball.v.y
        ball.v.x = -ball.v.x
        
        
a1 = sphere (pos = vec(0,0,0), size = vec(11,10,10), color = vec(247/255, 225/255, 162/255))
a2 = sphere (pos = vec(0,5.3,0), size = vec(2,2,2), color = vec(243/255, 213/255, 130/255))
a3 = sphere (pos = vec(-1.5,5.1,0), size = vec(2,2,2), color = vec(243/255, 213/255, 130/255))
a4 = sphere (pos = vec(1.5,5.1,0), size = vec(2,2,2), color  = vec(243/255, 213/255, 130/255))
a5 = sphere (pos = vec(-2,0.3,5), size = vec(1.2,1.3,1.3), color = color.black)
a6 = sphere (pos = vec(2,0.3,5), size = vec(1.2,1.3,1.3), color = color.black)


d8 = box(color = color.black, size = vec(1,0.1,1), pos=vec(0,-1.5,5))
d9 = box(color = color.black, size = vec(1,0.1,1), pos=vec(2.2,1.5,5))
d10 = box(color = color.black, size = vec(1,0.1,1), pos=vec(-2.2,1.5,5))

y = compound([a1, a2, a3, a4, a5, a6, d8, d9, d10])
y.pos = vec(25,-13,0)
