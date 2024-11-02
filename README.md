# PI2
Código, dados e relatórios para o PI2, 2024, UNIVESP.




Referente ao Projeto Integrador II
2024 - UNIVESP - Campus São Bernardo do Campo/SP
"Monitoramento Inteligente de Vegetais: Uso de IoT e Eletrofisiologia para Cuidado Sustentável"

Este repositório contém os arquivos:
write_to_csv_plus_sensor.py -> Código para coletar os dados do leitor de sinais bioelétricos conectado às plantas e escrever os resultados em formato .csv
report_maker5.py -> Código para fazer a interpolação dos dados entre os resultados da coleta de dados das plantas e as planilhas do sensor de temperatura e umidade

E as pastas:
Coletas -> Contém os arquivos de coleta de dados das plantas (inclusive anteriores ao início do Projeto)
Relatorios -> Contém os relatórios completos, já com os dados interpolados
Sensor -> Contém os arquivos das planilhas geradas pelo aplicativo android do fabricante do sensor de temperatura e umidade (disponível em https://play.google.com/store/apps/details?id=com.tuya.smartlife&hl=pt_BR)

Na criação deste repositório, foram omitidos os arquivos que faziam leitura dos dados do sensor de temperatura e umidade através de API e os preenchia diretamente no relatório, devido o fato da API ter sido bloqueada pelo fabricante. Desse modo, os respectivos arquivos tornaram-se obsoletos e sem função além de poluir as pastas.
