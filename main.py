#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# with open("Input/Letters/starting_letter.txt") as file:
#     letter_format = file.read()
#     #print(letter_format)
#
#
# guest_list = ()
# f = open("Input/Names/Invited_names.txt","r")
# data = f.readlines()
# #each_name =data.strip()
# #each_name.append(guest_list)
# print(data)
#
# # final_letter = letter_format.replace("[name]",each_name)
# # with open("ang_letter.txt", "w") as letter:
# #     content = letter.write("../../final_letter")
PLACEHOLDER = "[name]"
with open("Input/Names/Invited_names.txt") as names_file:
    names = names_file.readlines()
    #print(names)
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER,stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as finalize_lettter:
            finalize_lettter.write(new_letter)

        #print(new_letter)






