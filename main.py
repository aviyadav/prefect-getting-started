from prefect import flow, tags

@flow(log_prints=True)
def hello(name: str = "There") -> None:
    print(f"Hello, {name}!")


if __name__ == "__main__":
    with tags("test"):
        hello("World")

        crew = ["Alice", "Bob", "Charlie"]
        for name in crew:
            hello(name)