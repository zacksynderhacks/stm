import statistics as st,math
array=list(map(int,input('enter value into array').split()))
print((int(input("Enter value"))-(st.mean(array)))/(st.stdev(array)))
