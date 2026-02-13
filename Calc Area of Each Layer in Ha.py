#Calculate area of selected Layer in Q GIS (one liner)
print('\n'.join([f"{layer.name()}: {sum([f.geometry().area() for f in layer.getFeatures()]) / 10000:.2f} ha" for layer in iface.layerTreeView().selectedLayers()]))
