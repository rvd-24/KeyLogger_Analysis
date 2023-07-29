# Keylogger Analysis<br>
<h3> Project Structure:<br>
1. Project: This folder has the main `keylogger.py` file.<br>
2. Cryptography: This folder has the `generate_key.py` to encrypt the log files and `decrypt_file.py` & `decrypt_log_file.py` to decrypt the log files.<br>
3. Model: Some machine learning algorithms like ANN, Random Forest, and SVM were used to train the header files of the keylogger to analyse the headers of malicious and benign files. <br>
<br>
To convert the keylogger.py to .exe file, use the python package [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/) <br>

To get the header files of a .exe files use tools like Qu1ckSc0pe or pefile

