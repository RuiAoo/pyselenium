# pyselenium
 pyselenium $x is not defined的解决办法

查找了一些资料，一种说法是$x本身是Chrome js方法的缩写，因此pyselenium在执行js语句的时候如果包含了$x，会报以上的错误信息。
解决办法见main.py，亲测可以正常使用。
