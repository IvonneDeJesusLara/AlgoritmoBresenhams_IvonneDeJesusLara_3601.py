import matplotlib.pyplot as plt
def Graficar(x, y,x1, y1):
    dx= abs(x1 - x)
    dy =abs(y1 -y)
    p= (2 * dy) -dx
    for i in range(x,x1):
        plt.plot(round(x),round(y), marker="o", color="red")
        x= x + 1
        if p < 0:
            p= p + (2 * dy)
        else:
            p= p + (2 * dy) - (2 * dx)
            y= y + 1
        print(x,y)
    plt.show()
