#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;
int main()
{
freopen("/home/krishna/Downloads/A-large.in","r",stdin);
    freopen("/home/krishna/Desktop/codejm/lb.out","w",stdout);
	 int t,n;
	cin>>t;
	for( int i=1;i<=t;i++)
	{
		long long int u=0;		
		string s;
		cin>>s>>n;
		long long int y=s.length();
		for(long long int j=0;j<y;j++)
		{
			if(s[j]=='-')
			{
				if(j+n<=y)
				{
					for(long long int p=j;p<j+n;p++)
					{
						if(s[p]=='-')
						s[p]='+';
						 else if(s[p]=='+')
						s[p]='-';
					}//cout<<s<<endl;
				u++;
				}
			}
		}
		int f=0;
		for(long long int j=0;j<y;j++)
		{
			if(s[j]=='-')
			f=1;
		}
		if(f==1)
		cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
		else
		cout<<"Case #"<<i<<": "<<u<<endl;

	}
return 0;
}
