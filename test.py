import numpy as np
import matplotlib.pyplot as plt
print("Julia set fractal generator")
custom = int(input("Do you want a custom set? Yes(1); No(0): "))
match custom:
    case 0:
        c = -0.8 + 0.156j
    case 2:
        c= complex(-0.7269,0.1889)
    case 3:
        c =  complex(0.285,0.01)
    case 1:
        a = float(input("Real?: "))
        b = float(input("Imaginary?: "))
        c = complex(a,b)
customP = int(input("Do you want a custom center point? Yes(1); No(0): "))
if customP == 0:
    x=0
    y=0
else:
    x = float(input("X?: "))
    y = float(input("Y?: "))
zoom = float(input("Select the zoom level: "))
def julia_set(c, x, y, zoom):
    height=800
    width=1000
    max_iterations=100
    xWidth = 1.5
    yHeight = 1.5*height/width
    x_from = x - xWidth/zoom
    x_to = x + xWidth/zoom
    y_from = y - yHeight/zoom
    y_to = y + yHeight/zoom

    x = np.linspace(x_from, x_to, width).reshape((1, width))
    y = np.linspace(y_from, y_to, height).reshape((height, 1))
    z = x + 1j * y

    
    c = np.full(z.shape, c)

    
    div_time = np.zeros(z.shape, dtype=int)
    
    m = np.full(c.shape, True, dtype=bool)

    for i in range(max_iterations):
        z[m] = z[m]**2 + c[m]

        m[np.abs(z) > 2] = False

        div_time[m] = i
    return div_time


plt.imshow(julia_set(c,x,y,zoom), cmap='magma')
plt.show()