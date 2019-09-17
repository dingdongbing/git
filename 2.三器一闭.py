# class MyList(object):
#     """自定义的一个可迭代对象"""
#     def __init__(self):
#         self.items = []
#
#     def add(self, val):
#         self.items.append(val)
#
#     def __iter__(self):
#         myiterator = MyIterator(self)
#         return myiterator
#
#
# class MyIterator(object):
#     """自定义的供上面可迭代对象使用的一个迭代器"""
#     def __init__(self, mylist):
#         self.mylist = mylist
#         # current用来记录当前访问到的位置
#         self.current = 0
#
#     def __next__(self):
#         if self.current < len(self.mylist.items):
#             item = self.mylist.items[self.current]
#             self.current += 1
#             return item
#         else:
#             raise StopIteration
#
#     def __iter__(self):
#         return self
#
#
# if __name__ == '__main__':
#     mylist = MyList()
#     mylist.add(1)
#     mylist.add(2)
#     mylist.add(3)
#     mylist.add(4)
#     mylist.add(5)
#     for num in mylist:
#         print(num)


# -------------------------------------------------
# nums = [x for x in range(5)]
# print(type(nums))
# print(nums)
#
# nums2 = (x for x in range(5))
# print(type(nums2))
# print(nums2)

# num1 = next(nums2)
# print(num1)
#
# num2 = next(nums2)
# print(num2)

# for num in nums2:
#     print(num)


# --------------------------------------
# 使用迭代器实现斐波那契数列
# class Num(object):
#     def __init__(self):
#         self.num1 = 1
#         self.num2 = 1
#
#     def __next__(self):
#         temp_num = self.num1
#         self.num1, self.num2 = self.num2, self.num1+self.num2
#         return temp_num
#
#     def __iter__(self):
#         return self
#
#
# num = Num()
#
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))


# -------------------------------------------------
# 使用生成器实现斐波那契数列
# def num():
#     num1 = 1
#     num2 = 1
#     while True:
#         temp_num = num1
#         num1, num2 = num2, num1+num2
#         yield temp_num
#
#
# num = num()
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))


# ---------------------------------
# 闭包
# def test(number):
#     def test_in(number_in):
#         print("in test_in 函数, number_in is %d" % number_in)
#         return number+number_in
#     return test_in
#
#
# # 给test函数赋值
# ret = test(20)
#
# # 注意这里的100其实给参数number_in
# print(ret(100))
#
# # 注意这里的200其实给参数number_in
# print(ret(200))


# -------------------------------------------------------
