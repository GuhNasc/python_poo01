import pandas as pd

class CsvProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)

    def filtrar_csv(self, coluna, atributo):
        return self.df[self.df[coluna] == atributo]

arquivo_csv = './exemplo.csv'

filtro = 'estado'
limite = 'SP'

csv_processor = CsvProcessor(arquivo_csv)
csv_processor.carregar_csv()
print(csv_processor.filtrar_csv(filtro, limite))
