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
                
                print(logId, " // Event Id")
                print(date)
                pprint.pprint(otherFieldsDict)

                print("=" * 100)

    def dissect_protocol_event(self, log_example_file = log_example_file):
        
        if not (log_example_file or os.path.isfile(log_example_file)):
            sys.exit("Nothing to dissect. Quitting...")
        
        # [702: Tue Aug 13 13:51:31 2024] {"id":"9e7f2e2b-5959-11ef-9845-000c297aba6e","timestamp":1723542691787181,"payloadType":"c411a642-c139-4c7a-be58-93680bc20b41","payload":{"protocol":"SMB2","zoneID":2,"zoneName":"zone1","eventType":"create","detailType":"open-file-read","createResult":"DOES_NOT_EXIST","isDirectory":false,"desiredAccess":1179785,"clientIPAddr":"192.168.54.10","createDispo":1,"userSID":"S-1-5-21-590808809-419630438-3218851915-1605","userID":1000002,"fileName":"\\ifs\\data\\zone1\\smb\\share2\\folder1\\folder2\\desktop.ini","ntStatus":3221225524,"fsId":1,"partialPath":"folder1\\folder2\\desktop.ini","rootInode":4301587185}}


        rexFields = re.compile(r"\[(\d+):\s+(.*)\]\s+(.*)")

        with open(log_example_file, "r") as file:
            content = file.readlines()

    
        for line in content:
            if line.startswith("#"):
                print("\n")
                print((line.lstrip("#").rstrip("\n") + " ").center(100,"#"))
                print("=" * 100)

            mo = rexFields.search(line)
            if mo:
                logId = mo.group(1)
                date = mo.group(2)
                otherFieldsString = mo.group(3)

                otherFieldsDict = json.loads(otherFieldsString)

                print(logId, " // Event Id")
                print(date)
                pprint.pprint(otherFieldsDict)
    
    
if __name__ == "__main__":
    
    log_example_file = os.path.join(os.getcwd(), "log_examples", "cifs_share")
    dissector = Dissect()
    dissector.dissect(log_example_file = log_example_file)





        



        