class Cola:
    def __init__(self,tam=4):
        self.lista = []
        self.size = tam
        self.top = 0

    def push(self,dato):
        if self.top < self.size:
            self.lista = self.lista + [dato]
            self.top += 1
            return True
        else:
            return False

    def pop(self):
        if self.empty():
            return None
        else:
            top = self.lista[0]
            self.lista = self.lista[1:]
            self.top -= 1
            return top
        def show(self):
        for top in range(self.top):
            print("[{}]".format(self.lista[top]))

    def longitud(self):
        return self.top 

    def empty(self):
        if self.top == 0:
            return True
        else:
            return False