import json 
import os

class JsonEditor:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def write_json(self, data: dict) -> None:
        with open(self.filename , "w") as file:
            json.dump(data, file, indent=6)

    def read_json(self) -> dict:
        if(not os.path.exists(self.filename)):
            self.write_json({})

        with open(self.filename, "r+") as file:
            return json.load(file)

    def printer(self):
        print(json.dumps(self.read_json(), indent=6))

if __name__ == "__main__":
    id = input("id : ")
    path = input("path : ")
    options = input("options : ")
    test_file: JsonEditor = JsonEditor("modules_metadata_base.json")
    test_file.write_json({"id":id , "path":path ,})
    
    test_file.printer()