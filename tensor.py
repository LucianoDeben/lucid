import numpy as np  


class Tensor:
    """
    Creating a n-dimensional tensor with given shape using vectorization.
    """
    def __init__(self, shape=0):
        self.shape = shape
        self.ndim = len(shape) 
        self.data = [] if 0 in shape else self._initialize_data(shape)
        self._size()

    def _initialize_data(self, shape):
        if len(shape) == 0:
            return 0  # Base case: scalar (0-dimensional tensor)

        data = [0] * shape[-1]
        for dim in reversed(shape[:-1]):
            data = [data[:] for _ in range(dim)]
        return data
    
    def _size(self):
        size = 1
        if self.shape:
            for dim in self.shape:
                size *= dim
            self.size = size
        else:
            self.size = 0
    
    def flatten(self):
        flattened = []
        stack = [self.data]

        while stack:
            item = stack.pop()
            if isinstance(item, list):
                stack.extend(reversed(item))
            else:
                flattened.append(item)

        return flattened

if __name__ == "__main__":
    t = Tensor([3,3,3])




