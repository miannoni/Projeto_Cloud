class globaldict():

    def __init__(self):
        self.dict = {}
        self.last_id = 0

    def add_coisa(self, coisa):
        self.dict[self.last_id] = coisa
        self.last_id += 1

    def get_coisa(self, id):
        if (int(id) < self.last_id):
            return self.dict[int(id)]
        else:
            return False

    def update_coisa(self, id, coisa):
        if (int(id) < self.last_id):
            self.dict[int(id)] = coisa
            return True
        else:
            return False


    def deleta_coisa(self, id):
        if (int(id) < self.last_id):
            del self.dict[int(id)]
        else:
            return False

class Tarefas():

    def __init__(self):
        attr1 = 0
        attr2 = 0
