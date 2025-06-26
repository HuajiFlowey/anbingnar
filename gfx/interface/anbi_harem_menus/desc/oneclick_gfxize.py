import os

with open("images.gfx","w") as file2:
    file2.write('spriteTypes = {\n')

for filename in os.listdir(os.getcwd()):
    if '.' in filename:
        if not('.py' in  filename) and not('.gfx' in  filename):
            filename_noextension = '.'.join(filename.split('.',1)[:-1])
            with open("images.gfx","a") as file2:
                #print('\tSpriteType = {\n\t\tname = \"GFX_',filename_noextension,'\n\t\ttexturefile = \"*PATH_TO_REPLACE*',filename,'\"\n\t}\n')
                file2.write('\tSpriteType = {\n\t\tname = \"GFX_'+filename_noextension+'\"\n\t\ttexturefile = \"*PATH_TO_REPLACE*'+filename+'\"\n\t}\n')

with open("images.gfx","a") as file2:
    file2.write('}')