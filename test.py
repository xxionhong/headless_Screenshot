from Screen_shot import Screen_shot as ss

a = ss()
b = a.Full_screenshot(url='https://tw.yahoo.com/',save_path='.',image_name='test.png')
a.End_selenium()
