import PIL
import pypokedex
from PIL import Image, ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

root=tk.Tk()
root.geometry("500x500")
root.title("Pokemon")

'''
pokemon=pypokedex.get(name="Pikachu")
#print(pokemon.sprites)
#ouput is: Sprites(front={'default': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png','female': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/female/25.png','shiny': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/25.png'
#which is long so we focus on front
print(pokemon.sprites.front.get('default'))
#output is:https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png
'''


#create label
title_label=tk.Label(root, text="Pokedex")
title_label.configure(font=("Shanti", 32))
title_label.pack(padx=10,pady=10)

pokemon_image=tk.Label(root)
pokemon_image.pack(padx=10,pady=10)

pokemon_information=tk.Label(root)
pokemon_information.config(font=('Shanti',15))
pokemon_information.pack(padx=10,pady=10)

pokemon_types=tk.Label(root)
pokemon_types.config(font=('Shanti',15))
pokemon_types.pack(padx=10,pady=10)

#writin function for button
def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0,'end-1c'))

    #get sprites mentioned above in thriple inverted commas
    http=urllib3.PoolManager()
    response=http.request('GET',pokemon.sprites.front.get('default'))

    #turn the image in response to Bytes then into pillow
    image= PIL.Image.open(BytesIO(response.data))

    #put image into tkinter
    img=PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image=img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}")
    pokemon_types.config(text=",".join(pokemon.types))                  #join used to make it look more real rather than programmy



label_id_name=tk.Label(root, text="ID or Name:")
label_id_name.config(font=('Shanti',20))
label_id_name.pack(padx=10,pady=10)

text_id_name=tk.Text(root,height=1)
text_id_name.pack(padx=10,pady=10)


btn_load=tk.Button(root, text="Load Pokemon", command=load_pokemon)
btn_load.config(font=('Shanti'))
btn_load.pack(padx=10,pady=10)






root.mainloop()