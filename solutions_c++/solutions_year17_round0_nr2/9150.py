#include <bits/stdc++.h>
using namespace std;
 
unsigned long long tidy_sort(string number)
{
       unsigned long long n=0,i=0;
        while(number[i]!='\0')
        {
                n=n*10+((int)number[i]-48);
                i++;
        }
        return n;
}
void get_tidy_number(int cases, string number){
	int input_length = number.size();
	int flag = 0;
	if (input_length==1)
	{
        cout<<"Case #"<<cases<<": "<<number<<endl;
        return;
    }
    //check if number is already sorted
    for (int i=1;i<input_length;i++)
    {
    	if (number[i]<number[i-1])
    	{
    		flag=1;
    		break;
    	}
    }
    if (flag==0)
    	cout<<"Case #"<<cases<<": "<<tidy_sort(number)<<endl;
    else
    {
    	for (int i=0;i<input_length-1;i++)
    	{
    	    if (number[i]>=number[i+1])
    	    {
    	        number[i]=number[i]-1;
    	        for (int j=i+1;j<input_length;j++)
	             number[j]='9';
	            break;
    	    }
    	}
    	cout<<"Case #"<<cases<<": "<<tidy_sort(number)<<endl;
    }
}
int main() {
	freopen("inputsmall2.in","r",stdin);
    freopen("outputsmall2.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for (int cases=1;cases<=t;cases++)
	{
	    string input;
	    cin>>input;
	    get_tidy_number(cases, input);
	}
	return 0;
}