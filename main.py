import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Drink Water!",
            message = "Drink Water Now From Your Bottle",
            app_icon = "G:/Software Development/Python/Drink-Water-Notification/assets/icon.ico",
            timeout = 8
        )
        time.sleep(60*60)