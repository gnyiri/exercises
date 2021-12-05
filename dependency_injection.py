class AbstractDatabase:
    def __init__(self):
        self._url = None

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def connect(self):
        raise NotImplementedError

    def query(self) -> []:
        raise NotImplementedError


class ConcreteDatabase(AbstractDatabase):
    def __init__(self):
        super().__init__()

    def connect(self):
        print("Connect to {}".format(self.url))

    def query(self) -> []:
        return [1, 2, 3, 4]


class Application:
    def __init__(self, p_database: AbstractDatabase):
        self._database = p_database

    def run(self):
        q = self._database.query()
        print("Query: {}".format(q))


if __name__ == '__main__':
    database = ConcreteDatabase()
    database.url = "localhost"
    database.connect()
    app = Application(database)
    app.run()
