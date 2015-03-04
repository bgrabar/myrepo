import os

def rename_files():

  working_path = os.getcwd()
  # print working_path

  new_path = "/Users/bob/myrepo/python/python.course.ud036/l1/prank"
  # print new_path

  file_list = os.listdir(new_path)
  # print file_list

  os.chdir(new_path)
  for file_name in file_list:
    print("Old Name - "+file_name)
    os.rename(file_name, file_name.translate(None, "0123456789"))
    print("New Name - "+file_name.translate(None, "0123456789"))

  os.chdir(working_path)

rename_files()


