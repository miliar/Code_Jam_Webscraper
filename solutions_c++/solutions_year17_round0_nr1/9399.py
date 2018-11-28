//Google Code Jam
//Kunal Zantye
// Question 1 Flipper
#include<iostream>
using namespace std;

int checkFliper(string input, int k)
{
	int i=0,j=0, count=0;
	while(i<=input.length()-k)
	{
		if(input[i]=='+')
			i++;
		else
			{				
				for(j=0;j<k;j++)
				{

					if(input[i+j]=='-')
						input[i+j]='+';	
					else
						input[i+j]='-';

				}
					i++;
					count++;
				}
		}

			
		for(char c:input)
			{
				if(c=='-')
					return -1;
					
			}
	return count;
}
int main()
{
	int testCase;
	cin>>testCase;
	for(int t=1;t<=testCase;t++)
	{
		string input;
		int k;
		bool imp=false;

		cin>>input>>k;
		if(k>input.length())
		{
			cout<<"Case #"<<t<<": IMPOSSIBLE"<<"\n";
			
		}
		else{
		int count= checkFliper(input,k);	
			if(count==-1)
				cout<<"Case #"<<t<<": IMPOSSIBLE"<<"\n";
			else
				cout<<"Case #"<<t<<": "<<count<<"\n";
		}

	}
	return 0;
}