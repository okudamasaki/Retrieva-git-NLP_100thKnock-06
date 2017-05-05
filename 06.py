#!/usr/bin/env python
# -*- coding: utf-8 -*-


str1 = "paraparaparadise"
str2 = "paragraph"

def ngram(input, n):
	last = len(input) - n + 1
	ret = []
	for i in range(0, last):
		ret.append(input[i:i+n])
	return ret


x = set(ngram(str1, 2))
y = set(ngram(str2, 2))


print(x.union(y))
print(x.intersection(y))
print(x.difference(y))

print("se" in x)
print("se" in y)