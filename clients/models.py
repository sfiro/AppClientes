import uuid   #permite generar códigos unicos 


class Client:
    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4()   #uuid4 es el estandar de la industria para generar id unicos

    def to_dict(self):
        return vars(self)     #retorna nuestro objeto en forma de diccionario
    
    @staticmethod       #permite declarar metodos estaticos (permite declarar metodos sin una instancia de clase)
    def schema():     #notar que este metodo no se encuentra instanciado dentro del objeto
        return ['name', 'company', 'email', 'position', 'uid']  #representación de los encabezados de las columnas