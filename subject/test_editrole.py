# -*- coding: utf-8 -*-
# @Author   : zhulilan
# @FILE     : test_ar.py
# @Time     : 2021/10/28 18:56

from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains


class TestAddrole():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass
    def test_role(self):
        self.driver.get("https://precrm.joyobpo.com")
        self.driver.find_elements_by_class_name("el-input__inner")[0].send_keys("15267096796")
        self.driver.find_elements_by_class_name("el-input__inner")[1].send_keys("1q2w33")
        self.driver.find_elements_by_class_name("el-form-item__content")[2].click()

        #点击基础设置
        self.driver.find_element_by_xpath("//a[contains(@href,'/basicsetting/basicinfo')]").click()
        sleep(2)
        #点击权限管理
        self.driver.find_elements_by_class_name("el-submenu")[1].click()
        sleep(2)
        #点击角色管理
        self.driver.find_element_by_xpath("//a[contains(@href,'/basicsetting/role-management')]").click()
        sleep(2)
        self.driver.find_elements_by_class_name("el-input__inner")[0].send_keys("测试权限")
        sleep(2)
        self.driver.find_element_by_css_selector(".btn-primary").click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/section/div/div/div[2]/div[2]/div[1]/div[5]/div[2]/table/tbody/tr/td[7]/div/div/div[1]').click()
        sleep(2)
        #将没有全选的模块去勾选,需要双击
        isindeterminates = self.driver.find_elements_by_css_selector(".el-table__row--level-0 .el-checkbox__input.is-indeterminate")
        action = ActionChains(self.driver)
        for isindeterminate in isindeterminates:
            # isindeterminate.click()
            action.double_click(isindeterminate).perform()


        #将模块全选的去勾选
        ischecks=self.driver.find_elements_by_css_selector(".el-table__row--level-0 .el-checkbox__input.is-checked")
        for checke in ischecks:
            checke.click()
            # sleep(2)

        # 将所有菜单都重新勾选
        checkboxs = self.driver.find_elements_by_css_selector('.el-table__row--level-0 .el-checkbox__input')
        for checkbox in checkboxs:
            checkbox.click()
            # sleep(2)

        #点击下一步
        self.driver.find_element_by_css_selector(".btn_right.btn.button_primary").click()
        sleep(2)
        # 菜单权限设置全部权限
        codes = self.driver.find_elements_by_css_selector(".codeclick:nth-child(1)")
        for code in codes:
            code.click()
        #点击保存
        self.driver.find_element_by_css_selector(".btn_right.btn.button_primary").click()
        sleep(2)
        #选择所有用户生效
        self.driver.find_elements_by_class_name("el-radio__inner")[1].click()
        sleep(2)
        #点击保存
        self.driver.find_element_by_css_selector(".btn.sure").click()