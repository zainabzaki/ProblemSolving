#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
# can use this too but the code isn't present so i created my class NODE
#
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insertNodeAtHead(llist, data):
    new_node = Node(data)
    if llist is None:
        return new_node
    new_node.next = llist
    return new_node
