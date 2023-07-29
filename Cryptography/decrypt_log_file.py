from cryptography.fernet import Fernet

key="8uZWqnn-nSfzKGKMCU-ZGfdKOlX7jm3346GAcd-rihI="


with open("E:\Syntax Error\Python!\Keylogger\Project\Log files.txt",'rb') as f:
        data=f.read()
        fernet=Fernet(key)
        decrypted=fernet.decrypt(data)
        print(decrypted)
        with open("E:\Syntax Error\Python!\Keylogger\Cryptography\encrypted_Log_file.txt","wb") as f:
            f.write(decrypted)