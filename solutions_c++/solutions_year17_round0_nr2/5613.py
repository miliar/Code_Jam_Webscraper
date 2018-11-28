#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <fstream>
using namespace std;

vector<int> rDigits;

int checkIfAlreadyTidy(unsigned long long number)
{
	int remainder = number%10;
	int last_digit; 
	unsigned long long temp = number/10;
	while(temp>0)
	{
		last_digit = temp%10;
		if(last_digit > remainder)
			return 0;
		remainder = last_digit;
		temp = temp/10;
	}	
	return 1;
}

int getDigits(unsigned long long number)
{
	int count=0;
	while(number>0)
	{
		rDigits.push_back(number%10);
		number = number/10;
		count++;
	}	
	return count;
}

int main()
{
	freopen("B-large-attempt0.in","r",stdin);
	freopen("output_file_name.out","w",stdout);
	
	int t,count,digitCount;
	scanf("%d\n",&t);
	count = t;
	while(t--)
	{
		vector<int> digits,answer;
		unsigned long long number;
		scanf("%llu\n",&number);
		if(checkIfAlreadyTidy(number))
			cout<<"Case #"<<count-t<<": "<<number<<"\n";
		else
		{
		    digitCount = getDigits(number);
			for(int i=digitCount-1;i>=0;i--)
			{
				digits.push_back(rDigits[i]);
				answer.push_back(rDigits[i]);					
			}
			
    		int flag;
		    do
		    {
		        flag=0;
				for(int i=0;i<digitCount;i++)
				{
			        if(i+1 < digitCount)
				    {
				        if((answer[i+1]<answer[i]))
    					{
    						answer[i]--;
    						flag=1;
    						
    						for(int j=i+1;j<digitCount;j++)
    						{
    						    answer[j]=9;    
    						}    						
    						break;
    					}    					
				    }
			    }				
    	    }while(flag);
    	    
    	    int i=0;
    	    if(answer[0]==0)
    	        i=1;
    	    
			cout<<"Case #"<<count-t<<": ";     
			for(;i<answer.size();i++)
			{
				cout<<answer[i];
			}
	        cout<<"\n";
		}
		rDigits.clear();	
	}
}

