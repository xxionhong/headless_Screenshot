from Screen_shot import Screen_shot as ss

a = ss()
b = a.Full_screenshot(url='https://udn.com/news/story/7001/5066660?from=udn_ch2_menu_v2_main_cate',save_path='F:/new_pr_app/',image_name='test.png')
a.End_selenium()
