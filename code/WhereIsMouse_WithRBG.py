#! python
import pyautogui
print('Press Ctrl-C to quit.')
try:
    while True:
        # TODO: Get and print the mouse coordinates.
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ', Y: ' + str(y).rjust(4)
        # Add Code Here!!!!!
        # pixelColor = pyautogui.pixel(x, y)
        # pixelColor = pyautogui.screenshot().getpixel((x, y))
        positionStr += ', RGB: (' + str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
        # Add Code Here!!!!!
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.')