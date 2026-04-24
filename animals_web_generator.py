import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def load_html(file_path):
  """ Loads an HTML file """
  with open(file_path, "r") as handle:
      return handle.read()


def write_html(html, file_path):
  """ Writes an HTML file """
  with open(file_path, "w") as handle:
      handle.write(html)


def print_animal_data(data):
    """ prints the animal data to the screen"""
    for item in data:
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


def animal_data_to_str(data):
    """ writes the animal data to a string and returns it """
    output = ""
    for item in data:
        complete_list = [
            item.get("name"),
            item.get("characteristics").get("diet"),
            item.get("locations"),
            item.get("characteristics").get("type"),
        ]
        if not None in complete_list: # only print if all fields are set
            output += (f"Name: {complete_list[0]}\n")
            output += (f"Diet: {complete_list[1]}\n")
            output += (f"Location: ")
            for location in complete_list[2][:-1]:
                output += (f"{location}, ")
            output += (complete_list[2][-1])
            output += (f"\nType: {complete_list[3]}\n\n") # last one without ','
    return output


def animal_data_to_html(data):
    """ writes the animal data to a string and returns it """
    output = "<ul class='cards'>"
    for item in data:
        complete_list = [
            item.get("name"),
            item.get("characteristics").get("diet"),
            item.get("locations"),
            item.get("characteristics").get("type"),
        ]
        if not None in complete_list:
            output += "<li class='cards__item'>"
            output += (f"Name: {complete_list[0]}<br/>")
            output += (f"Diet: {complete_list[1]}<br/>")
            output += (f"Location: ")
            for location in complete_list[2][:-1]:
                output += (f"{location}, ")
            output += (complete_list[2][-1])
            output += "<br/>"
            output += (f"Type: {complete_list[3]}") # last one without ','
            output += "</li>"
    output += "</ul>"
    return output


def main():
    loaded_data = load_data("animals_data.json")
    animals_html = animal_data_to_html(loaded_data)

    html_template = load_html("animals_template.html")
    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    file_name = "animals.html"
    write_html(html_output, file_name)
    print(f"Animals written successfully to file '{file_name}'")


if __name__ == "__main__":
    main()
