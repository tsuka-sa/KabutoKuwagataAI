import sys
from PIL import Image
from keras.models import load_model
import numpy as np

def main():
    name = sys.argv[1]
    #print(name)
    image = Image.open(name)
    image = image.resize((64, 64))
    image.show()
    model = load_model("model.h5")
    np_image = np.array(image)
    np_image = np_image / 255
    np_image = np_image[np.newaxis, :, :, :]
    result = model.predict(np_image)
    #print(result)
    if result[0][0] > result[0][1]:
        print("カブトムシ")
    else:
        print("クワガタムシ")


if __name__ == "__main__":
    main()