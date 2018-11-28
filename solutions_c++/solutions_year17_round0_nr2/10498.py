#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

void reverse(char str[], int length)
{
    int start = 0;
    int end = length -1;
    while (start < end)
    {
        swap(*(str+start), *(str+end));
        start++;
        end--;
    }
}


char* itoa(int num, char* str, int base)
{
    int i = 0;
    bool isNegative = false;
 
    /* Handle 0 explicitely, otherwise empty string is printed for 0 */
    if (num == 0)
    {
        str[i++] = '0';
        str[i] = '\0';
        return str;
    }
 
    // In standard itoa(), negative numbers are handled only with 
    // base 10. Otherwise numbers are considered unsigned.
    if (num < 0 && base == 10)
    {
        isNegative = true;
        num = -num;
    }
 
    // Process individual digits
    while (num != 0)
    {
        int rem = num % base;
        str[i++] = (rem > 9)? (rem-10) + 'a' : rem + '0';
        num = num/base;
    }
 
    // If number is negative, append '-'
    if (isNegative)
        str[i++] = '-';
 
    str[i] = '\0'; // Append string terminator
 
    // Reverse the string
    reverse(str, i);
 
    return str;
}




int check(int a){
    
    int d=0,c=0;

	int temp=a;
	for(int b=0;temp!=0;b++){
	temp=temp/10;
	c++;
	}

	char buffer[c-1];

    itoa(a,buffer,10);

    for(int i=0;i<c;i++){ 
        for(int j=c-1;j>0;j--){
           
            if(i==j)
            {
                break;
            }
            
            else{
                
                if(buffer[j]<buffer[i])
                    d++;
                
                
           }
            
        }
        
    }
    
    return d;
    
    
}



int main() {
    int a,b;
    cin>>a;
    for(int i=1;i<=a;i++){
      
        cin>>b;
        int c=check(b);
        while(1){
            if(c==0){
                cout<<"Case #"<<i<<": "<<b<<"\n";
                break;
            }
            else {
                b--;
                c=check(b);
            }
            
        }
        
    }
	return 0;
}
