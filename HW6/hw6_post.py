import cv2
import os

dir = os.listdir('./')

c = 1
for file in dir:
  try:
    img = cv2.imread(file)
    for k in range(8):
      for j in range(8):
        img_sub = img[2+k*130:2+k*130+128, 2+j*130:2+j*130+128, :]
        img_sub = cv2.resize(img_sub, (64, 64))
        cv2.imwrite('./sub/'+str(c)+'.jpg', img_sub, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
        c = c + 1
        if c==1001:
          break
      if c==1001:
        break
    if c==1001:
      break
  except:
    continue

#os.system("cd sub")
#os.system("tar -zcf ../submission.tgz *.jpg")
