class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    _file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self._file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ''

    def add(self, *products):
        exis_products = self.get_products().splitlines()
        exis_names = {product.split(', ')[0] for product in exis_products}

        for product in products:
            if product.name in exis_names:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                with open(self._file_name, 'a') as file:
                    file.write(f'{str(product)}\n')
                    file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
