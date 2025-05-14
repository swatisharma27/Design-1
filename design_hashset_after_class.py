class MyHashSet:

    def __init__(self):
        self.bucket = 1000
        self.bucket_items = 1001
        self.storage = [None] * self.bucket

    def hash1(self, key): 
        return key % self.bucket

    def hash2(self, key): 
        return key // self.bucket

    def add(self, key: int) -> None:
        idx1 = self.hash1(key)
        idx2 = self.hash2(key)

        if self.storage[idx1] is None:
            self.storage[idx1] = [False] * (self.bucket_items)

        self.storage[idx1][idx2] = True

    def remove(self, key: int) -> None:
        idx1 = self.hash1(key)
        idx2 = self.hash2(key)

        if self.storage[idx1] is not None:
            self.storage[idx1][idx2] = False          

    def contains(self, key: int) -> bool:
        idx1 = self.hash1(key)
        idx2 = self.hash2(key)

        if self.storage[idx1] is not None:
            if self.storage[idx1][idx2]:
                return True
            else:
                return False
        else:
            return False   

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(6001)
obj.remove(7001)
param_3 = obj.contains(6001)
print(param_3)