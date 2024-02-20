import os


def replace_string_in_files(folder_path, old_string, new_string):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                content = file.read()

            # 替换字符串
            content = content.replace(old_string, new_string)

            with open(file_path, 'w') as file:
                file.write(content)


# 示例用法
folder_path = "VOC2007/Annotations/"
old_string = " E:\paddle\data\Dataset\Dataset\1 "
new_string = "new_text"

replace_string_in_files(folder_path, old_string, new_string)
