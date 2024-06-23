# ZoraChecker

## RUS

Чекер Зора на базе rubyscore.

Для использования:

1. Установите Python последней версии.
2. Создайте папку в удобном для вас месте и перейдите в нее.
3. Клонируйте репозиторий в эту папку, или просто скачайте архив с программой и разархивируйте.
4. Добавьте проверяемые кошельки в файл "wallets.txt", каждый кошелек - отдельная строка.
5. Добавьте прокси для проверки кошельков в файл "proxy.txt", каждое proxy - отдельная строка. **Формат Proxy - LOGIN:PASSWORD@IP:PORT**
6. Откройте cmd и пропишите следующие команды:
   1. `cd XXX`  - где XXX - путь до вашей папки с программой.
   2. `pip install -r requires.txt`
   3. `python main.py`

После выполнения программы будет сгенерирован Excel файл с данными.

## ENG

Zora checker based on rubyscore.

To use:

1. Install the latest version of Python.
2. Create a folder in a convenient location and navigate to it.
3. Clone the repository into that folder, or just download the archive with the program and unzip.
4. Add the wallets you want to verify to the "wallets.txt" file, each wallet is a separate line.
5. Add proxies for checking wallets to the file "proxy.txt", each proxy is a separate line. **Proxy format - LOGIN:PASSWORD@IP:PORT**
6. Open cmd and type the following commands:
   1. `cd XXX` - where XXX is the path to your program folder.
   2. `pip install -r requires.txt`
   3. `python main.py`

After the program is executed, an Excel file with data will be generated.
