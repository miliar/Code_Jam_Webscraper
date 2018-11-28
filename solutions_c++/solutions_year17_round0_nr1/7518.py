#include<bits/stdc++.h>
using namespace std;
#define FALSE 0
#define TRUE 1
bool isCheck(char *str)
{
	int i;
	for(i=0 ; i<strlen(str) ; i++)
	{
		if(str[i]=='-')
			return FALSE;
	}
	return TRUE;
}
int main()
{
	int t,k,i,j,count,ii;
	cin>>t;
	for(ii=1 ; ii<=t ; ii++)
	{
		cout<<"Case #"<<ii<<": ";
		count=0;
		char s[1009];
		cin>>s>>k;
		if(strlen(s)<k)
		{
			if(isCheck(s))
				cout<<"0\n";
			else
				cout<<"IMPOSSIBLE\n";

		}
		else
		{
			for(i=0 ; i<=(strlen(s)-k) ; i++)
			{
				if(s[i]=='-')
				{
					count++;
					for(j=0 ; j<k ; j++)
					{
						if(s[i+j]=='+')
							s[i+j]='-';
						else
							s[i+j]='+';
					}
				}
			}
			if(isCheck(s))
			{
				cout<<count<<endl;
			}
			else
			{
				cout<<"IMPOSSIBLE\n";
			}
		}
	}
	return 0;
}