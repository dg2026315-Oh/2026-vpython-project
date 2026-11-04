Web VPython 3.2
box(size = vec(80,38,0.1), texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWMjgYCO8lNv0o1IZAcitLuEgYpwcgb5vshy6B2Vud6CQiQc3OqFtIMSN9&s=10" )
cylinder(axis = vec(0,1,0), pos = vec(0, -18, 0.5), size = vec(16, 4, 5))
box(size = vec(1,1,0.1), pos = vec(0,0,0.5),texture = "https://png.pngtree.com/png-vector/20191022/ourlarge/pngtree-f-grade-vector-fail-exam-mark-isolated-flat-cartoon-illustration-png-image_1846214.jpg" )

c1 = sphere (pos = vec(0,0,0), size = vec(11,10,10), color = vec(247/255, 225/255, 162/255))
c2 = sphere (pos = vec(0,5.3,0), size = vec(2,2,2), color = vec(243/255, 213/255, 130/255))
c3 = sphere (pos = vec(-1.5,5.1,0), size = vec(2,2,2), color = vec(243/255, 213/255, 130/255))
c4 = sphere (pos = vec(1.5,5.1,0), size = vec(2,2,2), color  = vec(243/255, 213/255, 130/255))
c5 = sphere (pos = vec(-2,0.3,5), size = vec(1.2,1.3,1.3), color = color.black)
c6 = sphere (pos = vec(2,0.3,5), size = vec(1.2,1.3,1.3), color = color.black)


b6 = box(color = color.red, size = vec(0.1,1.2,1), pos=vec(1,0,5))
b7 = box(color = color.red, size = vec(2,0.1,1), pos=vec(0,0,5))
b8 = box(color = color.black, size = vec(1,0.1,1), pos=vec(0,-1.5,5))
b9 = box(color = color.black, size = vec(1,0.1,1), pos=vec(2.2,1.5,5))
b10 = box(color = color.black, size = vec(1,0.1,1), pos=vec(-2.2,1.5,5))

xx = []
xx.append(box(color = color.red, size = vec(0.1,1.2,1), pos=vec(-3,0,5)))
xx.append(box(color = color.red, size = vec(2,0,1.1), pos=vec(-2,-0.55,5)))
xx.append(box(color = color.red, size = vec(0.1,1.2,1), pos=vec(-1,0,5)))
xx.append(box(color = color.red, size = vec(0.1,1.2,1), pos=vec(3,0,5)))
xx.append(box(color = color.red, size = vec(2,0,1.1), pos=vec(2,-0.55,5)))


x = compound([c1, c2, c3, c4, c5, c6,b6, b7, b8, b9, b10])

    
while True : 
    rate(100)
    x.pos.x += 0.1
    for i in xx : 
        i.pos = x.pos
