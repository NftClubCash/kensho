import json
import os 

image_link= 'https://raw.githubusercontent.com/NftClubCash/kensho/main/png/'
nft_name = 'Kensho #'
directory_in_name = "./json/"
directory_out_name = directory_in_name


# Loop over all NFTs in separate files in directory_in_name
# fix traits and write output into separate files in directory_out_name
print("Loading NFTs and fixing metadata")
directory_in = os.fsencode(directory_in_name)
for file in os.listdir(directory_in):
    filename = os.fsdecode(file)
    if filename.endswith(".json"): 
        input_file = directory_in_name + filename
        # print(input_file)
        with open(input_file, 'r') as jsonfile:
            data = json.load(jsonfile)
            jsonfile.close()

            
            id = str(filename[:-len('.json')])
            # check id consistency
            id_from_edition = str(data["edition"])
            id_from_name = data["name"].split('#')[-1]
            id_from_image = data["image"].split('/')[-1][:-len('.png')]
            # if id != id_from_name or id != id_from_image or id != id_from_edition:
                # print("Fixing mismatched ids in metadata " + input_file)
                # print(str(id) + " " + str(id_from_edition) + " " + str(id_from_name) + " " + str(id_from_image))
            if True: # in case metadata needs to be fixed no matter what
                data["edition"] = id
                data['name'] = nft_name + id 
                data['image'] = image_link + str(data['edition']) + '.png'   
                data['description'] = "The Amazing Kensho NFT Collection by the NFT Club"
 
            

            out_file_name = directory_out_name + filename
            with open(out_file_name, 'w') as outfile:
                json.dump(data, outfile)

