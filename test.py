# myList = ['str1', 'str2', 'str3']
# mySing = ', '.join(myList) # ', '
# print(mySing)

# python test.py

dictionary = [{'персона': 'человек',
              'марафон': 'гонка бегунов длиной около 26 миль',
              'противостоять': 'оставаться сильным, несмотря на давление',
              'бежать': 'двигаться со скоростью'}]


result = '; '.join([f'{key}: {value}' for key, value in dictionary[0].items()])

print(result)

