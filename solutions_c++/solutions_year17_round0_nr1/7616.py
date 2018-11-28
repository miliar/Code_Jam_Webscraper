#include<iostream>
#include<string.h>
using namespace::std;


int main()
{
	int n;
	char s[1000];
	cin>>n;
	
	for(int i=0;i<n;i++)
	{
		int flip;
		int count=0;
		cin >> s >>flip;
		//cout<<strlen(s)-flip;
		for(int j=0;j<strlen(s)-flip+1;j++)
		{
			
			if(s[j]=='-')
			{
				for(int k=0;k<flip;k++)
				{
					if(s[j+k]=='-')
						s[j+k]='+';
					else
						s[j+k]='-';
					
				}
				count++;
				
			}
			
		}
		//cout<<s;
		int flag=0;
		for(int j=0;j<strlen(s);j++)
		{
			if(s[j]=='-')
				flag=1;
		}
		if(flag==0)
			cout<<"Case #"<<i+1<<": "<<count<<'\n';
		else
			cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE\n";
	}
	return 0;
}
