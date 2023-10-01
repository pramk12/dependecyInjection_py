from dependency_injector import containers,providers
from calcu import Calculator

class Container(containers.DeclarativeContainer):
    cal = providers.Singleton(Calculator)


def main():
    container = Container()
    calc = container.cal()
    n=5
    result = calc.sq(n)
    print(f"result: {result}")


if __name__ == "__main__":
    main()
