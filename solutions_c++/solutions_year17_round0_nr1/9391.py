#include<iostream>
using namespace std;
int main()
{
	int testCase;
	cin>>testCase;
	for(int m=1;m<=testCase;m++)
	{
		string input;
		int k;
		bool imp=false;

		cin>>input>>k;

		
		int i=0,j=0, count=0;
		if(k>input.length())
		{
			imp=true;
			
		}
		else
		{
			while(i<=input.length()-k)
			{
				if(input[i]=='+')
					i++;
				else
				{

					j=0;
					while(j<k)
					{

						if(input[i+j]=='-')
							input[i+j]='+';	
						else
							input[i+j]='-';
						j++;
					
						
					//if(c=='-')
					}
					i++;
					//cout<<count++;
					count++;
					//i+=k;

				}
				//cout<<input<<"\n";
				//
			}

			
		}
		for(char c:input)
			{
				if(c=='-')
					imp=true;
					
			}
		if(imp)
			cout<<"Case #"<<m<<": IMPOSSIBLE"<<"\n";
		else
			cout<<"Case #"<<m<<": "<<count<<"\n";//<<input<<"\n";


	}
	return 0;
}
