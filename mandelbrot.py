import numpy as np
import matplotlib.pyplot as plt

_ITERATIONS = 20
_CENTER = (-0.5, 0.)
_WIDTH = 1.

#_ITERATIONS = 50
#_CENTER = (-0.551, -0.62)
#_WIDTH = 0.05

def mandelbrot(c):
    z = 0
    for _ in range(_ITERATIONS):
        z = z**2 + c
    return abs(z) < 2.
    #return ~np.isnan(z)

def complex_matrix(xmin, xmax, ymin, ymax):
    re = np.linspace(xmin, xmax, 2048)
    im = np.linspace(ymin, ymax, 2048)
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

def main():
    c = complex_matrix(_CENTER[0] - _WIDTH,
                       _CENTER[0] + _WIDTH,
                       _CENTER[1] + _WIDTH,
                       _CENTER[1] - _WIDTH,)
    in_set = mandelbrot(c)
    plt.imshow(in_set, cmap="binary")
    plt.gca().set_aspect("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
