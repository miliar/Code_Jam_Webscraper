#include <iostream>
#include<string>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int loop=1;loop<=t;loop++)
	{
		string a;
		int k;
		int count=0;
		int flag=1;
		cin>>a>>k;
		for(int i=0;i<a.length();i++)
		{
			if(a[i]=='-')
			{
				try
				{
					for(int j=0;j<k;j++)
					{
						if(a[i+j]=='-')
						a[i+j]='+';
						else if(a[i+j]=='+')
						a[i+j]='-';
						else
						throw 10;
					}
				}
				catch(int e)
				{
					flag=0;
				}
				count++;
			}
		}
		if(flag)
		{
			printf("Case #%d: %d\n",loop,count);
		}
		else
		{
				printf("Case #%d: %s\n",loop,"IMPOSSIBLE");
			
		}
	}
	return 0;
}