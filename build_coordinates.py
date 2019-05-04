# Draw plot based on the x, y, z input

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class BuildCoordinates:

    def __init__(self, xs, ys, zs):
        self.xs = xs
        self.ys = ys
        self.zs = zs

    def plot(self, color, mark):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(self.xs, self.ys, self.zs, c = color, marker = mark)
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        plt.show()




