import os
import dropbox
from dropbox.files import WriteMode

class TransferData(object):
    def __init__(self,acess_token):
        self.acess_token=acess_token

    def upload_folder(self,folder_from,folder_to):
        dbx=dropbox.Dropbox(self.acess_token)

        for root,dirs,files in os.walk(folder_from):
            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, folder_from)
                dropbox_path = os.path.join(folder_to, relative_path)

                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))
    



def main():
    acess_token='sl.A08zWIccEj_xFvoRHOJAGjON1ozOrH1DZkrtHXcrflANwLuExSYlXRny8dXKtdnee_n-DmrMyPpsxFM8EtbATcDSCBCG_qr3TxOG5_onjlRXD2SMPk8D71gR3f6FtOwqOQgi2QU'
    
    backup=TransferData(acess_token)

    folder_from=input('Enter the folder to be backed up: ')
    folder_to=input('Enter the path the folder is to be placed: ')

    backup.upload_folder(folder_from,folder_to)

    print("The file is succesfully backed up!")

main()
