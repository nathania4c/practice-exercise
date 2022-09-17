import feature_1

def main():
    # Read text file contents before running features
    with open('text.txt','r') as f:
        print(f.read())
    
    # run feature
    feature_1.main()

    # Read text file contents after running features
    # (NOTE: Should be a new Hello World added)
    with open('text.txt','r') as f:
        print(f.read())

if __name__ == "__main__" : 
    main()
