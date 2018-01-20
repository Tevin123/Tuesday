import numpy as np 
import matplotlib.pyplot as pl 

data1 = np.loadtxt("testdata.csv",delimiter=",",skiprows=1)
pl.plot(data1[:,0],data1[:,1],"r--*")
pl.xlabel("time:")
pl.ylabel("${}^0C$")
pl.subplot(3,1,2)
xx = np.arange(0,100,0.5)
yy = np.sin(xx/100*np.pi)*20+10 
pl.plot(xx,yy,"g-")
pl.legend(["temp","sinwave"]) 
pl.xlim(xmax=150,xmin=0) 
pl.title("My graph!!!") 
pl.figure(2)
pl.subplot(1,2,2) 
pl.plot(data1[:,0],data1[:,3],"y.-")
pl.show()


