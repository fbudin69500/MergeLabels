#!/usr/bin/python
import sys
import SimpleITK as sitk
if len(sys.argv) < 5:
  print "Usage: "+sys.argv[0]+" InputFileNAme OutputFileName label0 ... labelN"
  exit(-1)
inputImg=sitk.ReadImage(sys.argv[1])


if len(inputImg.GetSize()) != 3:
  print "Image must be 3D"
  exit(-1)
labels=[]
labelzero=int(sys.argv[3])
for v in range( 4 , len(sys.argv) ):
  a=sys.argv[v]
  if not a.isdigit():
    print "Labels must be numbers"
    exit(-1)
  labels.append( int(sys.argv[v]) )

ysize=inputImg.GetSize()[1]
xsize=inputImg.GetSize()[0]
for z in range( 0, inputImg.GetSize()[2] ):
  for y in range( 0, ysize ):
    for x in range( 0, xsize ):
      voxel=inputImg.GetPixel( x, y, z )
      for v in labels:
        if voxel == v:
          inputImg.SetPixel( x, y, z, labelzero )
          break
          

sitk.WriteImage(inputImg, sys.argv[2])
