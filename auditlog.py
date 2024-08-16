import os, sys, re, pprint, json

log_example_file = None

class Dissect(object):

    def dissect(self, log_example_file = log_example_file ):

        if not (log_example_file or os.path.isfile(log_example_file)):
            sys.exit("Nothing to dissect. Quitting...")

        with open(log_example_file, "r") as file:
            content = file.readlines()

        rexFields = re.compile(r"\[(\d+):\s+(.*)\]\s+(.*)")

        for line in content:
            if line.startswith("#"):
                print("\n")
                print((line.lstrip("#").rstrip("\n") + " ").center(100,"#"))
                print("=" * 100)



            mo = rexFields.search(line)
            if mo:
                logId = mo.group(1)
                date = mo.group(2)
                otherFieldsString = mo.group(3).rstrip("\n")

                otherFieldsDict = json.loads(otherFieldsString)

                print("Original event:")
                print(line)
                print("-" * 100)
                
                print("Dissected event:")
                print(logId, " // Event Id")
                print(date)
                pprint.pprint(otherFieldsDict)

                print("=" * 100)
    
    
if __name__ == "__main__":
    
    log_example_file = os.path.join(os.getcwd(), "log_examples", "cifs_file")
    dissector = Dissect()
    dissector.dissect(log_example_file = log_example_file)





        



        