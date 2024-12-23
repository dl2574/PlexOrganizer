import os
import argparse




def main():
    parser = argparse.ArgumentParser(prog="Directory Crawler",
                                     description="Crwals a directory at a given path to restructure the files and folders found in that directory")
    
    parser.add_argument("--dir", help="The path to the root directory to begin crawling.")
    args = parser.parse_args()

    if args.dir is None:
        args.dir = "./"

    dir_list = []
    file_list = []
    for root, dir_names, file_names in os.walk(os.path.join(args.dir)):
        
        for dir in dir_names:
            dir_list.append(os.path.join(root,dir))

        for f in file_names:
            file_list.append(f)

    print("************************ Directory Listing ************************\n", dir_list, "\n************************************************")
    print("************************ File List ************************\n",file_list,"\n************************************************")

    

if __name__ == "__main__":
    main()