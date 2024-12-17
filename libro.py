class Libro:
    def __init__(self, titulo: str, autor: str, num_paginas: int ):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def descripcion(self) -> str:
        return f"{self.titulo}, Autor: {self.autor}, Páginas: {self.num_paginas}"

    def es_largo(self) -> bool:
        return self.num_paginas > 300 

libro = Libro("cien años de soledad", "Gabriel García Márquez", 417)
print(libro.descripcion())         
print(libro.es_largo())