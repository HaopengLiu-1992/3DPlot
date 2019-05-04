from data_import import DataImport
from build_coordinates import BuildCoordinates



# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
a = DataImport("data/centerline.csv")
b = BuildCoordinates(a.get_xs(), a.get_ys(), a.get_zs())
b.plot('red', 'o')