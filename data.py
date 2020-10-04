#! /usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
import time

print(dir(datetime.datetime))
da = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S %s")
print(da)

# 1601809091

da = datetime.datetime.now().timestamp()
print(int(da))

# 1601809091

da = time.strftime("%Y-%m-%d %H-%M-%S %s")
print(da)

# 1601809091
s = 1599350400;
da = time.ctime(s)
print(da)