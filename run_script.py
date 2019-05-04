from data_import import DataImport
from build_coordinates import BuildCoordinates

a = DataImport("data/centerline.csv")
b = BuildCoordinates(a.get_xs(), a.get_ys(), a.get_zs())
b.plot('red', 'o')
