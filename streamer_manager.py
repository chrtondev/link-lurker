def edit_streamers():
    # menu for user choice 
    print("1 add a streamer")
    print("2 remove a streamer")
    choice = input("chose 1 or 2")
    
    # will add a streamer if 1 is entered
    if choice == '1':
        streamer = input("enter the name of the streamer to add")
        with open("streamers.txt", "a") as file:
            file.write(streamer + '\n')
        print("streamer added") # add validation
        
    # will delete a streamer from the txt file
    elif choice == '2':
        streamer = input("enter the name of the streamer to remove: ")
        with open("streamers.txt", "r") as file:
            streamers = file.readlines()
        with open("streamers.txt", "w") as file:
            for line in streamers:
                if line.strip() != streamer:
                    file.write(line)
        print("streamer removed") # del validation 