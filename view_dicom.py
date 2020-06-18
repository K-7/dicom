import pydicom as dicom
import PIL # optional
import pandas as pd
import matplotlib.pyplot as plt

# specify your image path
image_path = './data/40642170'
ds = dicom.dcmread(image_path)
plt.imshow( ds.pixel_array)

plt.show()