from appium import webdriver
from time import sleep
desired_req={
    "appium:deviceName": "Pixel 5 API 29",
    "platformName": "Android",
    "appium:app": "D:\\appium_apk\\Flipkart-7.18.apk"
}
# desired_req2={
#     "appium:deviceName": "Nexus 5X API 29",
#     "platformName": "Android",
#     "appium:app": "D:\\appium_apk\\com.dunzo.user_2022-05-04.apk"
# }
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_req)
# driver2=webdriver.Remote("http://localhost:4723/wd/hub", desired_req2)
sleep(30)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[6]/android.widget.RelativeLayout").click()
driver.find_element_by_id("com.flipkart.android:id/select_btn").click()
sleep(15)
driver.find_element_by_id("com.flipkart.android:id/custom_back_icon").click()
sleep(15)
driver.find_element_by_id("com.flipkart.android:id/search_widget_textbox").click()
sleep(5)
driver.find_element_by_id("com.flipkart.android:id/search_autoCompleteTextView").send_keys("iphone12 \@")