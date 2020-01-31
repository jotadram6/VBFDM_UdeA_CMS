from os import system
from numpy.random import randint
from numpy import loadtxt

# paths
rcPath = "/home/santiago/Desktop/VBF_DMSimp_EWKExcluded/Cards/run_card.dat"
pcPath = "/home/santiago/Desktop/VBF_DMSimp_EWKExcluded/Cards/param_card.dat"
mlPath = "./massList.txt"
binPath = "/home/santiago/Desktop/VBF_DMSimp_EWKExcluded/bin/generate_events"

# Initial parameters for the param_card
couplingDic = {
                "gVXc":  "    1 0.000000e+00",
                "gVXd":  "    2 1.000000e+00",
                "gAXd":  "    3 0.000000e+00",
                "gVd11": "    4 2.500000e-01",
                "gVu11": "    5 2.500000e-01",
                "gVd22": "    6 0.000000e+00",
                "gVu22": "    7 0.000000e+00",
                "gVd33": "    8 0.000000e+00",
                "gVu33": "    9 0.000000e+00",
                "gVl11": "   10 0.000000e+00",
                "gVl22": "   11 0.000000e+00",
                "gVl33": "   12 0.000000e+00",
                "gAd11": "   13 0.000000e+00",
                "gAu11": "   14 0.000000e+00",
                "gAd22": "   15 0.000000e+00",
                "gAu22": "   16 0.000000e+00",
                "gAd33": "   17 0.000000e+00",
                "gAu33": "   18 0.000000e+00",
                "gAl11": "   19 0.000000e+00",
                "gAl22": "   20 0.000000e+00",
                "gAl33": "   21 0.000000e+00",
                "gnu11": "   22 0.000000e+00",
                "gnu22": "   23 0.000000e+00",
                "gnu33": "   24 0.000000e+00",
                "gVu31": "   25 0.000000e+00",
                "gAu31": "   26 0.000000e+00",
                "gVd31": "   27 0.000000e+00",
                "gAd31": "   28 0.000000e+00",
                "gVh":   "   29 0.000000e+00"
            }

def modRunCard():
    """
    Modifica la run_card 
    """
    tempPath = "temp.dat"
    system("cp " + rcPath + " " + tempPath)
    temp = open(tempPath)
    f = open(rcPath,"w")

    for l in temp:
        if "= iseed" in l:
            seed = randint(0,65000)
            l = "  {0} ".format(seed)+l[l.find("= iseed"):]
        f.write(l)

    f.close()
    temp.close()
    system("rm " + tempPath)


def modParamCard(mx, my):
    """
    Modifica la param_card
    """
    system("cp " + pcPath + " temp.dat")
    tempPath = "temp.dat"
    t = open(tempPath, "r")
    f = open(pcPath,"w")  

    for l in t:
        if " # MXd" in l:
            l = "  5000521 {0}".format(mx) + l[l.find(" # MXd"):]
        elif " # MY1" in l:
            l = "  5000001 {0}".format(my) + l[l.find(" # MY1"):]
        f.write(l)
    
    f.close()
    t.close()
    system("rm " + tempPath)

def initParamCard():
    """
    Inicializa los parámetros de la param_card
    """
    system("cp " + pcPath + " temp.dat")
    tempPath = "temp.dat"

    t = open(tempPath,"r")
    f = open(pcPath,"w")
    for l in t:
        for d in couplingDic:
            if d in l:
                l = couplingDic[d] + l[l.find(" # " + d):]
        f.write(l)

    f.close()
    t.close()
    system("rm " + tempPath)

initParamCard()
ml = loadtxt(mlPath)

for i in range(ml.shape[0]):
    modRunCard()
    modParamCard(ml[i,0], ml[i,1])

    #test
    #system("cp " + pcPath + " ./test/test{0}.dat".format(i) )
    system(binPath)