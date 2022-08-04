import pdfplumber, os, pandas

def createBingo(file, path, fileName = "serie", number_of_page = 0, ):
    if not(file) or not(path):
        print("Error your not provide the file or path")
        return
    print(file)
    
    data = pdfplumber.open(file).pages[number_of_page].extract_tables()
    
    for i in range(0, 6):
        df = pandas.DataFrame(data[i])

        dataFile = f"{fileName}{str(i)}.csv"

        if os.listdir().count(dataFile):

            os.remove(dataFile)

            print("-"* 40)

            print(f"Remove the file {fileName + str(i)}.csv")
            
            df.to_csv(path + "/"+ dataFile)

            print("-"* 40)

            print(f"Create new file: {dataFile}")

        else:
            df.to_csv(path + "/"+ dataFile)

            print(f"Create {dataFile}")

createBingo("",os.getcwd(),"serie",9)

