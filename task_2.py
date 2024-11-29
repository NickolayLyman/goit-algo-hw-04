def get_cats_info(path):
    try:
        with open(path,'r', encoding='UTF-8')  as fh:
            cats = list()
            for cat in fh.readlines():
                cat_info = cat.split(",")
                cats.append({'id':cat_info[0],"name":cat_info[1], "age":int(cat_info[2])})
            return cats
    except FileNotFoundError:
        print("File does not exist.")

cats_info = get_cats_info("cats_file.txt")
print(cats_info)