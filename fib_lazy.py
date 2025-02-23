# explanations for member functions are provided in requirements.py
from __future__ import annotations

class FibNode:
    def __init__(self, val: int):
        self.val = val
        self.parent = None
        self.children = []
        self.flag = False

    def get_value_in_node(self):
        return self.val

    def get_children(self):
        return self.children

    def get_flag(self):
        return self.flag

    def __eq__(self, other: FibNode):
        return self.val == other.val

class FibHeap:
    def __init__(self):
        # you may define any additional member variables you need
        self.roots = []
        self.min = None
        self.deleted = False

    def get_roots(self) -> list:
        return self.roots

    def insert(self, val: int) -> FibNode:
        node = FibNode(val)
        self.roots.append(node)
        if self.min is None or node.val < self.min.val:
            self.min = node
        return node
        
    def delete_min(self) -> None:
        if not self.min:
            return
        self.deleted = True
        if self.min in self.roots:
            self.roots.remove(self.min)
        if not self.roots:
            self.min = None
        else:
            self.merge()

    def find_min(self) -> FibNode:
        if not self.roots:
            if self.min and self.deleted:
                for child in self.min.children:
                    child.parent = None
                    self.roots.append(child)
                self.merge()
                self.min = self.find_min()
                self.deleted = False 
        else:
            return self.min

    def decrease_priority(self, node: FibNode, new_val: int) -> None:
        node.val = new_val
        
        if node.parent and node.val < node.parent.val:
            self.cut(node)
        
        if node.val < self.min.val:
            self.min = node

    def cut(self, node: FibNode):
        parent = node.parent
        if parent:
            parent.children.remove(node)
            node.parent = None
            self.roots.append(node)
            node.flag = False

    def merge(self):
        degree_table = {}
        
        while self.roots:
            node = self.roots.pop()
            degree = len(node.children)
            
            while degree in degree_table:
                other = degree_table.pop(degree)
                if node.val > other.val:
                    node, other = other, node
                node.children.append(other)
                other.parent = node
                degree += 1
            
            degree_table[degree] = node
        
        self.roots = list(degree_table.values())
        self.min = min(self.roots, key=lambda node: node.val)

    # feel free to define new methods in addition to the above
    # fill in the definitions of each required member function (above),
    # and for any additional member functions you define
