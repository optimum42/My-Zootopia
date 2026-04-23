import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def main():
    """
    reads the data from the JSON file prints all foxes that have name,
    diet, locations and type fields defined and ignores the other ones
    """
    loaded_data = load_data("animals_data.json")
    for item in loaded_data:
        complete_list = [
            item.get("name"),
            item.get("characteristics").get("diet"),
            item.get("locations"),
            item.get("characteristics").get("type"),
        ]
        if not None in complete_list: # only print if all fields are set
            print(f"Name: {complete_list[0]}")
            print(f"Diet: {complete_list[1]}")
            print(f"Location: ", end="")
            for location in complete_list[2][:-1]:
                print(f"{location}, ", end="")
            print(complete_list[2][-1])
            print(f"Type: {complete_list[3]}") # last one without ','
            print()


if __name__ == "__main__":
    main()
