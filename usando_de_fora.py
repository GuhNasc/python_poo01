from packages.teste2 import CsvProcessor


arquivo_csv = './exemplo.csv'

filtro = 'estado'
limite = 'SP'

csv_processor = CsvProcessor(arquivo_csv)
csv_processor.carregar_csv()
print(CsvProcessor.filtrar_csv(filtro, limite))