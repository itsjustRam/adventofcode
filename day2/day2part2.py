# 

def count_balls(filename):
    #arr={"red": 12,"blue": 14,"green":13}
    with open(filename, 'r') as file:
        l=1
        #game=[1]*100
        sum=0
        for line in file:
                # Split the line into balls
                
                
                print("Game :",l)
                l=l+1
                ball_tokens = line.strip().split(';')
                round=1
                max_prod=1
                arr={"red": 0,"blue": 0,"green":0}
                for ball_set in ball_tokens:
                    product=1
                    
                    print("round=",round)
                    round=round+1
                    color_tokens= ball_set.strip().split(',')
                    
                    for i in color_tokens:
                         count,color=i.strip().split()[-2:]
                         arr[color]=max(int(count),arr.get(color))
                       
                    for i in arr:
                         product=product*int(arr[i])
                         
                    if product>=max_prod:
                         max_prod=product
                         print("max: ",max_prod)
                sum=sum+max_prod

        print(sum)

                
        
                

                         
        


 



# Specify the filename
filename = './day2/input.txt'

# Get the counts for all games
count_balls(filename)
