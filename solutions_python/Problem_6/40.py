cat "small.in" | 
while
read line
do
echo "scale=100; (sqrt(5) + 3) ^ $line " | bc 
done