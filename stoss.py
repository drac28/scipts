import matplotlib.pyplot as plt
import PySimpleGUI as sg

# GUI 1
layout = [
    [sg.Text("Anzahl Graphen:"), sg.Spin(list(range(5)))],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window("Stoßtheorie - Simulation", layout)
event, values = window.read()
window.close()

graphnum = values[0]

# GUI 2
layout_sub = []
for i in range(graphnum):
    frame = [
        [sg.Spin(list(range(50)), key="-"+str(i)+"-")]
    ]
    layout_sub.append(sg.Frame(str(i+1)+". Graph:", frame))
layout = [
    [sg.Text("Wie viele Teilchen sollen pro Graph simuliert werden?")],
    layout_sub,
    [sg.Submit(), sg.Cancel()],
]
window = sg.Window("Stoßtheorie - Simulation", layout)
event, values = window.read()
window.close()

xnums = []
ynums = []

for i in range(graphnum):
    xnums.append(values["-"+str(i)+"-"])
    ynums.append(2)


# Stoss
def plot(xnum, ynum):
    pointsold = []
    for x in range(0, xnum):
        pointsold.append([x, 0])
        pointsold.append([x, ynum-1])

    for y in range(0, ynum):
        pointsold.append([0, y])
        pointsold.append([xnum-1,y])

    points = []
    for point in pointsold:
        if point not in points:
            points.append(point)

    plt.scatter(*zip(*points))
    for point1 in points:
        for point2 in points:
            if point1[0] != point2[0] and point1[1] != point2[1]:
                x = [point1[0], point2[0]]
                y = [point1[1], point2[1]]
                plt.plot(x, y, color="gray")

for i in range(len(xnums)):
    print(i)
    plt.subplot(len(xnums),1,i+1)
    plot(xnums[i], ynums[i])

plt.show()
