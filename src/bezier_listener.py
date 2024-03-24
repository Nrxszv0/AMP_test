import rpyc
import time
import cv2
import numpy as np
rpyc.core.protocol.DEFAULT_CONFIG['allow_pickle'] = True
if __name__ == "__main__":
    c = rpyc.connect("localhost", 9001)
    print("Listener Connected")
    while True:
        # img, curve = c.root.get_bezier()
        img, curve = c.root.get_bezier()
        # img2 = np.array(img)
        # img = np.array(img)
        if img is not None:
            # print(img)
            img = np.copy(np.array(img))
            # np.savetxt('test.out', img)
            # print(img)
            # arr = np.loadtxt('test.out')
            print(img)
            cv2.imshow("listener img", img)

        """
        if img2 is not None:
            print("Got image")
            # do something with the image
            print(img)
            cv2.imshow('Image', img2)
        """
        # if curve is not None:
            # print("Got curve")
            # do something with the curve
            # print(curve)
        time.sleep(1)