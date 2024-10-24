# item = {
#         1:
#             {"name": "Product A", "price": 25.99},
#         2:
#             {"name": "Product B", "price": 15.50},
#         3:
#             {"name": "Product C", "price": 45.00},
#         4:
#             {"name": "Product D", "price": 10.25}
#     }
# print(item.get(1))
# # for item in itemss:
# #     for key, value in item.items():
# #         print(f'{key}, {value}')

# item = {
#         1:
#             {"name": "Product A", "price": 25.99},
#         2:
#             {"name": "Product B", "price": 15.50},
#         3:
#             {"name": "Product C", "price": 45.00},
#         4:
#             {"name": "Product D", "price": 10.25}
#     }
# for i, b in item.get(1).items():
#     print(b)

# item = {
#         1:
#             {"name": "Product A", "price": 25.99},
#         2:
#             {"name": "Product B", "price": 15.50},
#         3:
#             {"name": "Product C", "price": 45.00},
#         4:
#             {"name": "Product D", "price": 10.25}
#     }
# items = item.get(1)
# for b in item.get(1).items():
#     items = b
# print(items)

items = None
item = {
        1:
            {"name": "Product A", "price": 25.99},
        2:
            {"name": "Product B", "price": 15.50},
        3:
            {"name": "Product C", "price": 45.00},
        4:
            {"name": "Product D", "price": 10.25}
    }
for i, b in item.get(1).items():
    items = b


