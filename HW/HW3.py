# Task#1
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2])
# Task#2
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# # result = sum(filter(lambda x: isinstance(x, int), list_1))
# # print(result)
# print([x for x in list_1 if isinstance(x, str) and 'a' in x])
# Task 3
# list1 = ['cat', 'dog', 'horse', 'cow']
# print(tuple(list1))
# family1 = tuple(input('Please enter family members ') .split(','))
# family2 = tuple(input('Please enter family members for the second family ') .split(','))
# if len(family1) == len(family2):
#     print('Equal')
# elif len(family1) > len(family2):
#     print(family1)
# else:
#     print(family2)

# Task#5
# film = {'title': 'gossipgirl', 'director':'cameron','year': 2010,'budget': 1000000,
#         'mainActor': 'Blair', 'slogan':'XOXO'}
# print(film.keys())
# print(film.values())
# print(film.items())
# Task 6
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37,'num4': 21}
# print(list(my_dictionary.values()))
# print(sum(my_dictionary.values()))
# # TAsk7
# lis1 = set([1, 2, 3, 4, 5, 3, 2, 1])
# print(lis1)
# TAsk8.3
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set1.issubset(set2))
print(set2.issubset(set1))

# task8.1
print(set1.intersection(set2))

# task8.2
print(set1.difference(set2))
print(set2.difference(set1))