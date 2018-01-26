import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n', .2)
pg.hotkey('winleft','up')
pg.typewrite('amazon.com\n', .2)

time.sleep(2)

pg.moveTo(269, 173, 1)
pg.click()

pg.typewrite('playstation 4\n', .2)
