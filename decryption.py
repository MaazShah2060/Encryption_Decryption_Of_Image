fo = open('enc.jpg','rb')
image = fo.read()
fo.close()
image = bytearray(image)
key = 40
for index , value in enumerate(image):
    image[index] = value ^ key

fo = open("dec.jpg","wb")
fo.write(image)
fo.close()
