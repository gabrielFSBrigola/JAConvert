from PIL import Image
import json



img_path_user = None

img_output_user = None

name_output_user = None

format_output_user = None

def converter(img_path, img_output ,name_output, format_output):
    open_img = Image.open(img_path)

    if open_img.format == ".jpg" or open_img.format == ".jpeg":
        rgb_in = open_img.convert("RGB")

        rgb_in.save(img_output + name_output + "." + format_output)
        print("SUCESSO! arquivo criado!!")
    else:
        open_img.save(img_output + name_output + "." + format_output)
        print("SUCESSO! arquivo criado!!")

with open("data.json", "r") as file:
    dados = json.load(file)

img_path_user = dados["image_path"]
img_output_user = dados["image_output"]
name_output_user = dados["name"]
format_output_user = dados["format"]

#print(f"{img_path_user} || {img_output_user} || {name_output_user} || {format_output_user}")




converter(img_path_user,img_output_user,name_output_user,format_output_user)
