#include <bits/stdc++.h>

using namespace std;

#define ll long long int 

int main()
{
	int t,k[100];
	cin>>t;
	char s[100][1001];
	int count[100]={0};
	for (int i = 0; i < t; ++i)
	{
		cin>>s[i]>>k[i];
		//cout<<s[i]<<endl;
		//cout<<k<<endl;
	}
	for (int i = 0; i < t; ++i)
	{
		const int size=strlen(s[i]);
		
		for (int j = 0; j < size+1-k[i]; ++j)
		{
			if (s[i][j]=='-')
			{
				count[i]++;
				for (int p = j; p < j+k[i]; ++p)
				{
					s[i][p]=(s[i][p]=='+'?'-':'+');
				}
				//cout<<s[i]<<endl;
			}
		}
		for (int m = size-k[i]+1; m < size; ++m)
		{
			if (s[i][m]=='-')
			{
				count[i]=-1;
				break;			
			}
		}
	}
	for (int i = 0; i < t; ++i)
	{
		if (count[i]>=0)
		{
			cout<<"Case #"<<i+1<<": "<<count[i]<<endl;	
		}
		else
		{
			cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
		}
	}
	return 0;
}