money=int(input('Введите сумму вклада:'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
TKB=round((float(per_cent['ТКБ'])*money*0.01),2)
SKB=round((float(per_cent['СКБ'])*money*0.01),2)
VTB=round((float(per_cent['ВТБ'])*money*0.01),2)
SBER=round((float(per_cent['СБЕР'])*money*0.01),2)
deposit=[TKB,SKB,VTB,SBER]
print('Накопленные средства за год вклада в каждом из банков:',deposit)
print(f'Максимальная сумма, которую вы можете заработать - {max(deposit)}')