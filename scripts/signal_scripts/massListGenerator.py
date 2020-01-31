
mx = [10., 50., 100., 200., 400., 600., 800., 1000.]
my = [100., 200., 500., 800., 1000., 2000., 3000., 4000., 5000.]

f = open("massList.txt","w")
f.write("#m_x\tm_y\r\n")
for x in mx:
    for y in my:
        if 2*x <= y:
            f.write("{0}\t{1}\r\n".format(x,y))

f.close()