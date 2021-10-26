# -*- coding: utf-8 -*-
# @Author   : zhulilan
# @FILE     : test_addrole.py
# @Time     : 2021/10/22 16:10
from time import sleep

from selenium import webdriver


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
        #点击新增角色按钮
        self.driver.find_element_by_css_selector("button.jy-button.table-operation-item.jy-button--primary").click()
        sleep(2)
        #输入角色名称
        self.driver.find_elements_by_class_name("el-input__inner")[1].send_keys("zll自动化新增角色")
        sleep(2)
        # checkboxs=self.driver.find_element_by_css_selector('input[type=checkbox]')
        # for checkbox in checkboxs:
        #     checkbox.click()
        #     sleep(2)
        #勾选所有菜单
        self.driver.find_element_by_css_selector(".el-table__row:nth-child(1) .el-checkbox__inner").click()
        self.driver.find_element_by_css_selector(".el-table__row:nth-child(3) .el-checkbox__inner").click()
        self.driver.find_element_by_css_selector(".el-table__row:nth-child(5) .el-checkbox__inner").click()
        self.driver.find_element_by_css_selector( ".el-table__row:nth-child(7) .el-checkbox__inner").click()
        self.driver.find_element_by_css_selector(".el-table__row:nth-child(36) .el-checkbox__inner").click()
        self.driver.find_element_by_css_selector( ".el-table__row:nth-child(38) .el-checkbox__inner").click()
        self.driver.find_element_by_css_selector( ".el-table__row:nth-child(66) .el-checkbox__inner").click()
        self.driver.find_element_by_css_selector( ".el-table__row:nth-child(79) .el-checkbox__inner").click()
        self.driver.find_element_by_css_selector( ".el-table__row:nth-child(127) .el-checkbox__inner").click()
        self.driver.find_element_by_css_selector(".el-table__row:nth-child(171) .el-checkbox__inner").click()
        self.driver.find_element_by_css_selector( ".el-table__row:nth-child(232) .el-checkbox__inner").click()
        self.driver.find_element_by_css_selector( ".el-table__row:nth-child(259) .el-checkbox__inner").click()
        self.driver.find_element_by_css_selector( ".el-table__row:nth-child(289) .el-checkbox__inner").click()
        self.driver.find_element_by_css_selector( ".el-table__row:nth-child(291) .el-checkbox__inner").click()
        self.driver.find_element_by_css_selector( ".el-table__row:nth-child(305) .el-checkbox__inner").click()
        self.driver.find_element_by_css_selector( ".el-table__row:nth-child(307) .el-checkbox__inner").click()
        self.driver.find_element_by_css_selector( ".el-table__row:nth-child(309) .el-checkbox__inner").click()
        self.driver.find_element_by_css_selector( ".el-table__row:nth-child(388) .el-checkbox__inner").click()
        self.driver.find_element_by_css_selector( ".el-table__row:nth-child(399) .el-checkbox__inner").click()
        self.driver.find_element_by_css_selector(".el-table__row:nth-child(423) .el-checkbox__inner").click()
        #点击下一步
        self.driver.find_element_by_css_selector(".btn_right.btn.button_primary").click()
        sleep(2)
        #菜单权限设置全部权限
        for i in range(1,335):
            x=str(i)
            self.driver.find_element_by_css_selector(".el-table__row:nth-child("+x+") .codeclick:nth-child(1)").click()
        #点击保存
        self.driver.find_element_by_css_selector(".btn_right.btn.button_primary").click()

