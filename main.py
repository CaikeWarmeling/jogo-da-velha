import sqlite3 as lite

conexao = lite.connect('jogo_da_velha.db')

def edit_vitoria_x():

    with conexao:
        cur = conexao.cursor()
        querry = '''SELECT vitoria_x
                    FROM veia'''
                    
        cur.execute(querry)
        informacoes = cur.fetchall()
        
        i = [informacoes[0][0] + 1]
        querry = '''UPDATE veia 
                    SET vitoria_x=?  
                    WHERE id=1'''
        cur.execute(querry, i)
            
def edit_vitoria_o():
    
    with conexao:
        cur = conexao.cursor()
        querry = '''SELECT vitoria_o
                    FROM veia'''
                    
        cur.execute(querry)
        informacoes = cur.fetchall()
        
        i = [informacoes[0][0] + 1]
        querry = '''UPDATE veia 
                    SET vitoria_o=?  
                    WHERE id=1'''
        cur.execute(querry, i)    

        
def edit_empate():

    with conexao:
        cur = conexao.cursor()
        querry = '''SELECT empate
                    FROM veia'''
                    
        cur.execute(querry)
        informacoes = cur.fetchall()
        
        i = [informacoes[0][0] + 1]
        querry = '''UPDATE veia 
                    SET empate=?  
                    WHERE id=1'''
        cur.execute(querry, i)
        
def limpar():
    with conexao:
        cur = conexao.cursor()
        querry = '''UPDATE veia 
                    SET vitoria_x=0, vitoria_o=0, empate=0  
                    WHERE id=1'''
        cur.execute(querry)
        
def view_vitorias():
    
    view = []
    with conexao:
        cur = conexao.cursor()
        querry = '''SELECT vitoria_x, vitoria_o, empate
                    FROM veia'''
                    
        cur.execute(querry)
        informacoes = cur.fetchall()
        for i in informacoes:
            view.append(i)
            
    return view

print(view_vitorias())