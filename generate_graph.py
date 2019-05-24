import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time, csv

style.use('seaborn-paper')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

def animate(i): #function to be animated
    x = [] #date time list
    y = [] #room temp list
    z = [] #temp in list
    a = [] #temp out list
    b = [] #env temp list
    c = [] #flow rate list
    format = "%Y-%m-%d %H:%M:%S" #defines format of date time for x-axis
    with open('test_data.txt', 'r') as csvfile: #opens the data text file
        toplot = csv.reader(csvfile, delimiter=',') #reads the text file recognizing values as comma separated
        toplot = list(toplot)
        if len(toplot) > 50: #appends updated values after 50 values have already been placed
            for row in toplot[len(toplot)-50:len(toplot)]:
                x.append(row[0])
                y.append(float(row[1]))
                z.append(float(row[2]))
                a.append(float(row[3]))
                b.append(float(row[4]))
                c.append(float(row[5]))            
        else: #adds values while the total number of current values is less than 50
            for row in toplot[1:]:
                x.append(row[0])
                y.append(float(row[1]))
                z.append(float(row[2]))
                a.append(float(row[3]))
                b.append(float(row[4]))
                c.append(float(row[5]))
    ax.clear() #clears the plot prior to drawing a new plot
    ax.plot(x,y,label="Room Temperature")
    ax.plot(x,z,label="Inlet Temperature")
    ax.plot(x,a,label="Outlet Temperature")
    ax.plot(x,b,label="Environmental Temperature")
    ax.plot(x,c,label="Flow Rate")

    maxlist=[max(y), max(z), max(a), max(b), max(c)]
    maxval=int(max(maxlist))
    plt.yticks(range(0,maxval+5,5)) #defines the y-axis tick mark range according to the maximum data value

    plt.gcf().autofmt_xdate() #formats the x-axis for datse
    plt.xlabel("TIME (YYYY-MM-DD HH:MM:SS)")
    plt.ylabel("Temperature (F) / Flow Rate (GPM)")
    plt.title("Temperature (F) / Flow Rate (GPM) v TIME (YYYY-MM-DD HH:MM:SS)")
    plt.legend()

    
ani = animation.FuncAnimation(fig, animate, interval=15000) #animates the figure on a 15sec interval
plt.show()
