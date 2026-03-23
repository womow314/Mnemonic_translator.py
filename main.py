import random
"""#Translation functions"""
if True:
    def runAdmin(user_input, contains_two_parts):
        clean_word = user_input.strip("[]").lower()
        #Sets up spacing
        prefix = " " if user_input.startswith("[") else ""
        suffix = " " if user_input.endswith("]") else ""
        #checks for comma multi-part printing
        if user_input.count(",") > 0:
            array = user_input.split(",")
            for word in array:
                runAdmin(word, False)
            return
        
        #checks if it is a two part admin command
        if contains_two_parts:
            #Split into parts
            words_in_random = clean_word.split("-")
            
            #Get number value
            num_part = translateToNUM(words_in_random[0])
            
            #Make String value for randomizer
            string_of_words = [f"{prefix}{w}{suffix}" for w in words_in_random]
            string_of_words = str(string_of_words)
            string_of_words = string_of_words.replace("\'", "\"")
            
            #Print
            print(f'"{prefix}{num_part}{suffix}": random.choice({string_of_words}),')
        else:
            #Set up number and string part
            num_part = translateToNUM(clean_word)
            str_part = clean_word
            
            #print
            print(f'"{prefix}{num_part}{suffix}": "{prefix}{str_part}{suffix}",')
    
    def translateToSTR(string):
        #Formating punctuation
        if True:
            punctuation_at_end = string[-1]
            if punctuation_at_end not in ["!", ".", "?"]:
                punctuation_at_end = ""
            string = string.strip("!.?")
            string = " " +string + " "
        string = " "+string+" "
        #Random Word details
        replacement = {
            #------------------------------------random words
            "–": "-",
            "—":"--",
            " 9-7--0- ": " because ",
            " 6-4- ": " there ",
            " 0- ": " so ",
            " --99-27": " yapping",
            " --9": " yap",
            " 2-8-4 ": " never ",
            " 0-01-4": " sister",
            " 94-6-4": " brother",
            " 8-6-4": " father",
            " 3-6-4": " mother",
            " 95---27 ": " playing ",
            " --273-2 ": " hangman ",
            " 6-3 ": " them ",
            " -7-- ": " okay ",
            " --47": " work",
            " ---5- ": " while ",
            " --0 ": random.choice([" yes ", " was "]),
            " 2- ": " no ",
            " 7--27 ": " going ",
            " 9-40-": " parse",
            " 9-6 ": " both ",
            " 6-1 ": random.choice([" chat ", " that ", " shot "]),
            " 0-9-4-1-": " seperate",
            " -91-1-": " update",
            " -27-39-00 ": " encompass ",
            " 6-0- ": random.choice([" these ", " those "]),
            " --41": " word",
            " 014--7-1": " straight",
            " 7--": " guy",
            " 0-3-1-3-": " sometime",
            " 1-47": " dork",
            " 3-2- ": random.choice([" many ", " mini "]),
            " 3-7-27 ": " making ",
            " 0-70 ": " six ",
            " 3-2-74-81 ": " minecraft ",
            " 6-2 ": random.choice([" then ", " than "]),
            " 4-7-1": " right",
            " -4-1-": " write",
            " 0-6- ": " sushi ",
            " 1-01-": " taste",
            " 7--1": " good",
            " --451": " world",
            " 2--1": " need",
            " 5--8-": " leave",
            " 8-4- ": " very ",
            " 0--2 ": " soon ",
            " 6--7- ": " though ",
            " 1-2'1 ": " don't ",
            " 1-3-44-- ": " tomorrow ",
            " 06--5": " school",
            " --6 ": " with ",
            " --4 ": " our ",
            " --2 ": " own ",
            " --451": " world",
            " --42-27": " warning",
            " 9--51-27 ": " building ",
            " 0-21-27-": " sentance",
            " -5-9-4-1- ": " elaborate ",
            " 14-9": " trap",
            " 5-27": " link",
            " 1-074-91--2": " discription",
            " 4-22-4": " runner",
            " 09--2": " spawn",
            " 8-4--42": " forwarn",
            " -07": " ask",
            " 14-6": " truth",
            " 1-4-": " dare",
            " 9--7-": " piece",
            " 01-8-": " steve",
            " 6-7-2": " chicken",
            " 9-9-4": " paper",
            " --55- ": " hello ",
            " -9": " up",
            " 1--2": " down",
            " -4": " or",
            
            " --00-9": " wassup",
            " -6-4--0- ": " otherwise ",
            " 5-1-4-55- ": " literally ",
            " 6-01 ": " just ",
            " -0-27 ": " using ",
            " 7-2 ": " can ",
            " 5-5 ": " lol ",
            " --3--": " Womow",
            " ---51 ": " would ",
            " -05--9 ": " asleep ",
            " 1-4-27 ": " during ",
            " 7-39-1-1--2": " competition",
            " 0-8-2 ": " seven ",
            " 9-4 ": random.choice([" per ", " bar "]),
            " 7-4--5": " cereal",
            " -87 ": " afk ",
            " --7-1 ": random.choice([' eight ', ' hiked ']),
            " -50- ": random.choice([" else ", " also "]),
            " ---4": random.choice([" hour", " your"]),
            " 5-7-": " like",
            " 91- ": " btw ",
            " 9-7": " pig",
            " 9--4 ": random.choice([" poor ", " pair ", " beer "]),
            " 95--": " play",
            " 4--5-0-": " realize",
            " 3-00-1 ": " missed ",
            " 32-3-2-7-55- ": " mnemonically ",
            " 32-3-2-7": " mnemonic",
            " -7--8-5-21 ": " equivalent ",
            " 0--": " say",
            " 8-5-1 ": " valid ",
            " 6-27 ": random.choice([" think ", " chunk ", " thunk "]),
            " 9-01 ": " best ",
            " 94-- ": " bruh ",
            " 94- ": " bro ",
            " 1-39 ": " dumb ",
            " -2- ": random.choice([" one ", " any "]),
            " 1-- ": " two ",
            " 64-- ": " three ",
            " ---4- ": " where ",
            " 14--27 ": " trying ",
            " -4- ": " are ",
            " 8-4 ": " for ",
            " 8--4 ": " four ",
            " 7-1": " get",
            " 8-8- ": " five ",
            " 2-2- ": " nine ",
            " 01-4-": " stare",
            " 01-4-27 ": " staring ",
            " 01-4": " star",
            " 32-3-2-7 ": " mnemonic ",
            " 1-1 ": random.choice([" dad ", " did "]),
            " --57-3- ": " welcome ",
            " 6-27": " thank",
            " 2-701": " next",
            " --3- ": " home ",
            " ---6": " youth",
            " 1-2-7-1 ": " tonight ",
            " ---6": " youth",
            " 9-7 ": " back ",
            " ---4 ": " your ",
            " -1'0 ": " it's ",
            " 7-21- ": " kinda ",
            " 74--9- ": " creepy ",
            " 8-43 ": random.choice([" farm ", " form "]),
            " 6-1": random.choice([" that", " shot"]),
            " 9-11-4 ": random.choice([" better ", " butter "]),
            " 6--": random.choice([" show", " shoe"]),
            " 2-1 ": " not ", 
            " -1 ": random.choice([" it ", " at "]),
            " 0-6 ": " such ",
            " -3-4-51": " emerald",
            " - ": " a ",
            " 9-1 ": random.choice([" bed ", " put ", " pit ", " bad ", " but "]),
            " -3 ": " am ", 
            " 8-21": " find",
            " 6- ": random.choice([" she ", " the "]),
            " --- ": random.choice([" who ", " you ", " why ", " how ", " way ", " you "]),
            " 5 ": " I ",
            " 9- ": " be ",
            " 4--1": random.choice([" raid", " root"]),
            " -9--1 ": " about ",
            " 1- ": random.choice([" do ", " to "]),
            " ---1": random.choice([" wait", " what", " wood", " head", " heat"]),
            " -8 ": random.choice([" of ", " if "]),
            " -21 ": " and ",
            " -2-6-4 ": " another ",
            " -55": " all",
            " 7-8-": " give",
            " -4--21 ": " around ",
            " 3-7-": " make",
            " 0-48-7-": " service",
            " --02'1 ": " hasn't ",
            " 01-41": " start",
            " 7-3-": " game",
            " 8-1--": " video",
            " 8-8-4-1-": " favorite",
            " - ": " a ",
            " -2 ": random.choice([" in ", " on "]),
            " 1--1": " that",
            " --8- ": " have ",
            " 5-8-": " love",
            " 3- ": random.choice([" me ", " my "]),
            " -- ": random.choice([' hi ', ' we ']),
            " -0 ": " is ",
            " 2-3-": " name",
            " 6- ": random.choice([" she ", " the "]),
            " -70-5-15": " axolotl",
            " --1 ": random.choice([" eat ", " yet "]),
            " 14- ": " try ",
            " --43": " worm",
            " 07-5-1-2": " skeleton",
            " --41": " word",
            " --21": " want",
            " 14-205-1-": " translate",
            " 74--9-4": " creeper",
            " 0-39--": " zombie",
            " 7-1": random.choice([" get", " cat", " hat"]),
            " 1-7": " dog",
            " 7--7 ": " quick ", 
            " 94-2": " brown", 
            " 8-70": " fox",
            " 6-39": random.choice([" thumb", " jump"]),
            " -8-4 ": " over ",
            " 5-0-": " lazy",
            " 1-7": " dog", 
            " 6-0 ": " this ",
            " 9-4-27 ": " boring ",
            " --4- ": " here ",
            #------------------------------------endings
            "6-2 ": "tion ",
            #------------------------------------names
            " 8-01-4": " Foster",
            " 9-47-4": " Parker",
            " 0-3": " Sam",
            " 5-4--2": " Lorien",
            " 94-21-2": " Brandon",
            " 3-77--": " Maggie",
            " 75--4-": " Claire",
            " 2---": " Noah",
            " 6-6--": " Joshua",
            " 6-55--": " Shelley",
            " 5-21-2": " Landen",
            " 6-7": " Jack",
            " --24-": " Henry",
            " ---2": random.choice([" Owen", " when"]),
            " 6-1-": " Jude",
            " -4--2 ": " Arwen",
            #--------------------------------------------------------------------------
            #------------------------------------MUST BE LAST--------------------------
            #--------------------------------------------------------------------------
            "0 ": "s "
        }
        for word in replacement:
            string = string.replace(word, replacement[word])
        
        #Letter details
        replacement = {
            "1": random.choice(["t", "d"]),
            "2": "n",
            "3": "m",
            "4": "r",
            "5": "l",
            "6": random.choice(["j", "ch", "sh", "th"]),
            "7": random.choice(["c", "k", "ck", "g"]),
            "8": random.choice(["f", "v"]),
            "9": random.choice(["p", "b"]),
            "0": random.choice(["s", "z"]),
            "-": random.choice(["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "w", "h", "y"]),
            "—": random.choice(["ea", "io", "ou", "ie", "wo"])
        }
        for word in replacement:
            string = string.replace(word, replacement[word])
        
        #Return
        return string.strip(" ") + punctuation_at_end
    
    def translateToNUM(string):
        string = " " + string + " "
        #Dictionary of letters
        translate = {
            "ch": "6",
            "sh": "6",
            "th": "6",
            "ck": "7",
            " i ": " 5 ",
            "a": "-",
            "b": "9",
            "c": "7",  
            "d": "1",
            "e": "-",
            "f": "8",
            "g": "7",  
            "h": "-",
            "i": "-",
            "j": "6",
            "k": "7",
            "l": "5",
            "m": "3",
            "n": "2",
            "o": "-",
            "p": "9",
            "q": "7",
            "r": "4",
            "s": "0",
            "t": "1",
            "u": "-",
            "v": "8",
            "w": "-",
            "x": "70", 
            "y": "-",
            "z": "0"
        }
        
        #Parse
        for word, parse in translate.items():
            string = string.replace(word, parse)
        
        #Return
        return string.strip(" ")

def runGame():
    #Setting up arrays
    if True:
        alphabet = [
        "a",
        "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        numbers = [
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "—", "\""
            ]
     
    """Runs the game"""   
    while True:
        #User Input
        user_input = input("What word do you want to translate: ").strip()
        if not user_input:
            continue
        clean_word = user_input.strip("[]").lower()
        #Admin code
        if True:
            #Check if admin command is multi-part
            contains_two_parts = user_input.count("-") > 0
            
            #Check if admin command is true
            is_admin = user_input.startswith("[") or user_input.endswith("]")
            
            if is_admin:
                runAdmin(user_input, contains_two_parts)
        
        
            #Check which languge to run
            elif user_input[0].lower() in alphabet:
                print(translateToNUM(clean_word))
            elif user_input[0].lower() in numbers:
                for _ in range(10):
                    print(translateToSTR(user_input))


