from hashlib import sha256
from datetime import datetime

class Blockchain:

    def __init__(self, difficulty=4):
        self.blocks = []
        self.difficulty= difficulty
        self.set_genesis_block()
        
# Cria o bloco gênesis, que é o primeiro bloco na cadeia de blocos.
    def set_genesis_block(self):
        data = 'Hello, World!' 
        timestamp = datetime.utcnow().timestamp()
        prev_hash = 0
        index = 0
        self.hash_block(
            data, timestamp, prev_hash, index
        )
    #  Cria o hash de um bloco
    def hash_block(self, data, timestamp, prev_hash, index):
        hash = ''
        nonce = 0
        while not self.is_hash_valid(hash):
            nonce += 1
            block = '{}:{}:{}:{}:{}'.format(
                data, timestamp, prev_hash, index, nonce
            )
            hash = sha256(block.encode()).hexdigest()
            #nonce += 1
        print('[TENTATIVAS]', nonce)
        self.blocks.append(hash)
    #Retorna o hash do último bloco adicionado
    def get_last_hash(self):
        return self.blocks[-1]
   
    #Verifica se um hash começa com um número de zeros 
    def is_hash_valid(self, hash):
        return hash.startswith('0' * self.difficulty)
#Adiciona um novo bloco à lista
    def add_new_block(self, data):
        index = len(self.blocks)
        prev_hash = self.get_last_hash()
        timestamp = datetime.utcnow().timestamp()
        self.hash_block(
            data, timestamp, prev_hash, index
        )
    
    # Retorna uma cópia da lista
    def get_all(self):
        return self.blocks[:]