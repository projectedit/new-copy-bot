
from datetime import datetime, timedelta
import re
from robocorp.tasks import task
from RPA.Browser.Selenium import Selenium
from RPA.FileSystem import FileSystem
from RPA.Excel.Files import Files
from task.news_scraper import NewsScraperBot


browser = Selenium()
filesystem = FileSystem()
excel = Files()


@task
def main():

    bot = NewsScraperBot()
    bot.run()

