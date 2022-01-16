import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BAN0vkhkye0_89DbLtcFzLQ0CzVQBzwI9EdstDfn8XpEhsqBtNPUakdBNX40Buubi4dSTEZiqzbZoJtjThoLw9daynaMaGIKXSjBvhh_-8FfFRfFxQOROWwIuGRYFni2u_ki9s0'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ") 
    
   
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
