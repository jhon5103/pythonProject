import psycopg2


class AppBD:
    def __init__(self):
        print('Método Construtor')

    # Joubert Lima Correa de Oliveira - 202102283388,
    # Jhonata Goncalves Antunes - 202102212812
    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(user="postgres", password="1234", host="localhost", port="5432",
                                               database="postgres")
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print('Falha ao se conectar ao Bando de dados', error)


    # Joubert Lima Correa de Oliveira - 202102283388,
    # Jhonata Goncalves Antunes - 202102212812
    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            print('Selecionando todos os produtos')
            sql_select_query = """select * from public. "Agenda" """

            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print(registros)

        except (Exception, psycopg2.error) as error:
            print("Erro na operação de seleção", error)

        finally:
            # fechando a conexao com o banco de dados
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada")
        return registros

    # Inserir dados
    # Joubert Lima Correa de Oliveira - 202102283388,
    # Jhonata Goncalves Antunes - 202102212812
    def inserirDados(self, codigo, nome, preco, precoAdd):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_insert_query = """ INSERT INTO public. "Agenda" ("codigo", "nome", "preco", "precoAdd") VALUES (%s, %s, %s, %s)"""
            record_to_insert = (codigo, nome, preco, precoAdd)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro inserido com sucesso na tabela Agenda")
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Falha ao inserir registros na tabela Agenda", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada")

    # Atualizar dados
    # Joubert Lima Correa de Oliveira - 202102283388,
    # Jhonata Goncalves Antunes - 202102212812
    def atualizarDados(self, codigo, nome, preco, precoAdd):
        try:
            #codigo = self.codigo
            self.abrirConexao()
            cursor = self.connection.cursor()

            print("Registro Antes da Atualização")
            sql_select_query = """select * from public. "Agenda" where "codigo" = %s"""
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)

            sql_update_query = """UPDATE public. "Agenda" set "nome" = %s, "preco" = %s, "codigo" = %s, "precoAdd" = %s"""
            cursor.execute(sql_update_query, (nome, preco, codigo, precoAdd))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso")
            print("Registro depois da atualização")
            sql_select_query = """select * from public. "Agenda" where "codigo" = %s"""
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)
        except (Exception, psycopg2.Error) as error:
            print("Erro na atualização", error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada")

    # excluirDados
    # Joubert Lima Correa de Oliveira - 202102283388,
    # Jhonata Goncalves Antunes - 202102212812
    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            sql_delete_query = """DELETE FROM public. "Agenda" where "codigo" = %s"""
            cursor.execute(sql_delete_query, (codigo,))

            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluido com sucesso")
        except (Exception, psycopg2.Error) as error:
            print("Erro na exclusão", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada")
