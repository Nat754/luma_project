"""This section contains Training page tests"""
from data.data_urls import TRAINING_PAGE_URL, VIDEO_DOWNLOAD_PAGE_URL
from pages.training_page import TrainingPage
import allure


@allure.epic("Training Page")
class TestMainPage:
    @allure.feature("Testing Training Page Sidebar")
    class TestTrainingSidebar:

        @allure.title("TC 16.01.01 Verify Sidebar panel title Shop By is visible and contains text 'Shop By'")
        def test_tc_16_01_01_check_sidebar_shop_by_title(self, driver):
            """Check Sidebar Shop By title has correct text and is visible"""
            page = TrainingPage(driver, TRAINING_PAGE_URL)
            page.open()
            title = page.check_sidebar_panel_shop_by()
            assert title == "Shop By", f"Expected title: 'Shop By', Actual title: {title}"

        @allure.title("TC 16.01.02 Verify Sidebar panel title Category is visible and contains text 'Category'")
        def test_tc_16_01_02_check_sidebar_category_title(self, driver):
            """Check Sidebar Category title has correct text and is visible"""
            page = TrainingPage(driver, TRAINING_PAGE_URL)
            page.open()
            title = page.check_sidebar_panel_category()
            assert title == "Category", f"Expected title: 'Category', Actual title: {title}"

        @allure.title("TC 16.01.03 Verify Sidebar title Video Download is visible and contains text 'Video Download'")
        def test_tc_16_01_03_check_sidebar_video_download_title(self, driver):
            """Check Sidebar Video Download title has correct text and is visible"""
            page = TrainingPage(driver, TRAINING_PAGE_URL)
            page.open()
            title = page.check_sidebar_panel_video_download()
            assert title == "Video Download", f"Expected title: 'Video Download', Actual title: {title}"

        @allure.title("TC 16.01.04 Verify Sidebar panel title Video Download contains URL")
        def test_tc_16_01_04_check_sidebar_video_download_href(self, driver):
            """Check Sidebar Video Download contains URL"""
            page = TrainingPage(driver, TRAINING_PAGE_URL)
            page.open()
            href = page.check_sidebar_panel_video_download_href()
            assert href == VIDEO_DOWNLOAD_PAGE_URL, f"Incorrect URL in Video Download"

        @allure.title("TC 16.01.05 Verify Sidebar panel title Compare Products is visible and contains text 'Compare Products'")
        def test_tc_16_01_05_check_sidebar_compare_products(self, driver):
            """Check Sidebar Category title has correct text and is visible"""
            page = TrainingPage(driver, TRAINING_PAGE_URL)
            page.open()
            title = page.check_sidebar_panel_compare_products()
            assert title == "Compare Products", f"Expected title: 'Compare Products', Actual title: {title}"

        @allure.title("TC 16.01.06 Verify Sidebar panel title My Wish List is visible and contains text 'My Wish List'")
        def test_tc_16_01_06_check_sidebar_my_wish_list(self, driver):
            """Check Sidebar Category title has correct text and is visible"""
            page = TrainingPage(driver, TRAINING_PAGE_URL)
            page.open()
            title = page.check_sidebar_panel_my_wish_list()
            assert title == "My Wish List", f"Expected title: 'My Wish List', Actual title: {title}"