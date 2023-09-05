from blockchain import Blockchain


if __name__ == '__main__':
    blockchain = Blockchain(difficulty=4)

    blockchain.add_new_block('REDES DE COMPUTADORES!')
    blockchain.add_new_block('PYTHON É BRABO!')
    blockchain.add_new_block('D3TEC')

    print(blockchain.get_all())