#Code is for the purpose of reclassifying the n images contained...
#... in a folder into certain speciic classes of specific ranges
import os
import gdal
import numpy as np
import PIL
def reclass(path,path1):
    aa=gdal.Open(path)
    ra=aa.ReadAsArray()
    ra=np.array(ra,dtype=float)
#the line below ignore the null data value
    ab = np.ma.masked_array(ra, mask=(ra == -9999))
    shape=ab.shape
#flatten the image 2D array into 1D array
    rb=ab.flatten()
    x=rb.size
#Provide the all ranges in if and elif statement as per requirement
#Also provide the value to be assignment to each class
    for i in range(x):
        if rb[i]<=0:
            rb[i]=1
        elif rb[i]>0:
            rb[i]=9
        else:
            rb[i]=0
# In function reshape(row,column) provide the no of rows and column into which
# the earlier 2D array was ( Note it down from ArcGIS/QGIS
    arr2 = np.asarray(rb).reshape(332,139)
    gt=aa.GetGeoTransform()
    gp=aa.GetProjection()
    geotiff = gdal.GetDriverByName('GTiff')
    output = geotiff.Create(path1,aa.RasterXSize,aa.RasterYSize,1,gdal.GDT_Byte)
    output.SetGeoTransform(aa.GetGeoTransform())
    output.SetProjection(aa.GetProjection())
    output.GetRasterBand(1).WriteArray(arr2)
    xa=output.ReadAsArray()
    xa=np.array(xa,dtype=float)
    print xa
#prodive the source and destination folder
SourceDir=r'E:\inputfolder'
DestDir=r'E:\outputfolder'
fnames=os.listdir(SourceDir)
q=1
for name in fnames:
    if name.endswith('.img'):
        infile=SourceDir+'\\'+name
        outfile=DestDir+'\\'+name[0:-4]+'.tif'
        reclass(infile,outfile)
    elif name.endswith('.tif'):
        print q
        infile=SourceDir+'\\'+name
        outfile=DestDir+'\\'+name[0:-4]+'.tif'
        reclass(infile,outfile)
        q=q+1


