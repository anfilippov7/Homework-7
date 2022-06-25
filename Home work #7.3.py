import os

files_key = []
files_values = []

with os.scandir(r'C:\Users\sashf\PycharmProjects\pythonProject7.3\Home7_3') as entries:
    for entry in entries:
        files_key.append(entry.name)

def files_dict(files_key):

    for file in files_key:
        # print(file)
        file = open(file, encoding='utf-8')
        files_values.append(file.readlines())
    global dict_files
    dict_files = dict(zip(files_key, files_values))
    file.close()
    return dict_files
files_dict(files_key)

sorted_dict = {}
def files_write(dict_files):
    sorted_dict = ({k:v  for k, v in sorted(dict_files.items(), key=lambda x: len(x[1]))})
    file = open('file_overall.txt', 'w', encoding='utf-8')
    for k,v in sorted_dict.items():
        file.write(k + '\n')
        file.write(' ')
        file.write(str(len(v)) + '\n')
        file.writelines(v)
    file.close()

files_write(dict_files)




def file_path(file_name: str) -> str:
    for root, dirnames, filenames in os.walk('.'):
        for file in filenames:
            if file == file_name:
                print(file)
                print(filenames)
                return os.path.join(root, file)

file_path(files_key)