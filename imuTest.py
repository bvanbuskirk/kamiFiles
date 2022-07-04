import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import collections
import board
import adafruit_fxos8700
import adafruit_fxas21002c
i2c = board.I2C()
fxos = adafruit_fxos8700.FXOS8700(i2c)
fxas = adafruit_fxas21002c.FXAS21002C(i2c)



# function to update the data
def my_function(i):
    # get data
    # acc.popleft()
    aX, aY, aZ = fxos.accelerometer
    accX.popleft()
    accX.append(aX)
    accY.popleft()
    accY.append(aY)
    accZ.popleft()
    accZ.append(aZ)
    # gyro.popleft()
    gX, gY, gZ = fxas.gyroscope
    gyroX.popleft()
    gyroX.append(gX)
    gyroY.popleft()
    gyroY.append(gY)
    gyroZ.popleft()
    gyroZ.append(gZ)    
    # # kal.popleft()
    # kal.append(kal.popleft() + 10)
    # clear axis
    figx.cla()
    figy.cla()
    figz.cla()
    # ======plot X dimension======
    # plot accelerometer
    figx.plot(accX)
    figx.scatter(len(accX)-1, accX[-1])
    figx.text(len(accX)-1, accX[-1]+2, "{}%".format(accX[-1]))
    # plot gyroscope
    figx.plot(gyroX)
    figx.scatter(len(gyroX)-1, gyroX[-1])
    figx.text(len(gyroX)-1, gyroX[-1]+2, "{}%".format(gyroX[-1]))
    # # plot kalman filter
    # figx.plot(kalX)
    # figx.scatter(len(kalX)-1, kalX[-1])
    # figx.text(len(kalX)-1, kalX[-1]+2, "{}%".format(kalX[-1]))

    figx.set_ylim(0,100)

    # ======plot Y dimension======
    # plot accelerometer
    figy.plot(accY)
    figy.scatter(len(accY)-1, accY[-1])
    figy.text(len(accY)-1, accY[-1]+2, "{}%".format(accY[-1]))
    # plot gyroscope
    figy.plot(gyroY)
    figy.scatter(len(gyroY)-1, gyroY[-1])
    figy.text(len(gyroY)-1, gyroY[-1]+2, "{}%".format(gyroY[-1]))
    # # plot kalman filter
    # figy.plot(kalY)
    # figy.scatter(len(kalY)-1, kalY[-1])
    # figy.text(len(kalY)-1, kalY[-1]+2, "{}%".format(kalY[-1]))
    
    figy.set_ylim(0,100)

    # ======plot Z dimension======
    # plot accelerometer
    figz.plot(accZ)
    figz.scatter(len(accZ)-1, accZ[-1])
    figz.text(len(accZ)-1, accZ[-1]+2, "{}%".format(accZ[-1]))
    # plot gyroscope
    figz.plot(gyroZ)
    figz.scatter(len(gyroZ)-1, gyroZ[-1])
    figz.text(len(gyroZ)-1, gyroZ[-1]+2, "{}%".format(gyroZ[-1]))
    # # plot kalman filter
    # figz.plot(kalZ)
    # figz.scatter(len(kalZ)-1, kalZ[-1])
    # figz.text(len(kalZ)-1, kalZ[-1]+2, "{}%".format(kalZ[-1]))
    
    figz.set_ylim(0,100)

# start collections with zeros
accX, accY, accZ = collections.deque(np.zeros(10))
gyroX, gyroY, gyroZ = collections.deque(np.zeros(10))
# kalX, kalY, kalZ = collections.deque(np.zeros(10))
# define and adjust figure
fig = plt.figure(figsize=(12,6), facecolor='#DEDEDE')
figx = plt.subplot(311)
figy = plt.subplot(312)
figz = plt.subplot(313)
figx.set_facecolor('#DEDEDE')
figy.set_facecolor('#DEDEDE')
figz.set_facecolor('#DEDEDE')
# animate
ani = FuncAnimation(fig, my_function, interval=10)
plt.show()