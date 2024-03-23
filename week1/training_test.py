def word_count(input_file,output_file):
    #dictionary to store the word count
    word_counts = {}

    #open input file for reading    
    with open(input_file,"r") as file:
        #read the content of the file
        contents = file.read()
        #split the content into words
        words = contents.split()
        #count the words of occurance
        for word in words:
           word_counts[word] = word_counts.get(word,0)+1

    #open output file for writing
    with open(output_file,"w") as file:
        for word,count in word_counts.items():
            file.write(f"{word}:{count}\n")

    
input_file = 'hello_data.txt'
output_file = 'hello_data_copy.txt'
word_count(input_file,output_file)
print("Word count complted successfully!")