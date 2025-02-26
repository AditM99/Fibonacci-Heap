from __future__ import  annotations
class FibNode:
    def __init__(self, val: int):
        self.val = val
        self.parent = None
        self.children = []
        self.flag = False
        self.is_vacant = False

    def get_value_in_node(self):
        return self.val

    def get_children(self):
        return self.children

    def get_flag(self):
        return self.flag

    def __eq__(self, other: FibNode):
        return self.val == other.val

class FibHeapLazy:
    def __init__(self):
        # you may define any additional member variables you need
        self.roots = []
        self.min = None

    def get_roots(self) -> list:
        return self.roots

    def insert(self, val: int) -> FibNode:
        node = FibNode(val)
        self.roots.append(node)
        if self.min is None or node.val < self.min.val:
            self.min = node
        return node

    def delete_min_lazy(self) -> None:
        if self.min is None:
            return

        if self.min.is_vacant:
            self.merge()
            self.min.is_vacant = True

        else:
            self.min.is_vacant = True
            # self.find_min_lazy()



    def find_min_lazy(self) -> FibNode:
        if self.min is None or self.min.is_vacant == True:
            self.merge()
            return self.min
        else:
            return self.min

    def decrease_priority(self, node: FibNode, new_val: int) -> None:
        node.val = new_val

        if node.parent and node.val < node.parent.val:
            self.cut(node)
            parent = node.parent
            while parent and parent.flag:
                self.cut(parent)
                parent = parent.parent
            if parent:
                parent.flag = True

        if self.min is None or node.val < self.min.val:
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
        new_roots = []

        while self.roots:
            node = self.roots.pop()
            if node.is_vacant:
                for child in node.children:
                    child.parent = None
                    new_roots.append(child)
            else:
                new_roots.append(node)
        while new_roots:
            node = new_roots.pop()
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
        self.min = None
        for node in self.roots:
            if self.min is None or node.val < self.min.val:
                self.min = node

    # feel free to define new methods in addition to the above
    # fill in the definitions of each required member function (above),
    # and for any additional member functions you define
