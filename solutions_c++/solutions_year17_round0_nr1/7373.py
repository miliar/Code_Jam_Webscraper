#include<iostream>
#include<algorithm>
#include<string.h>
using namespace std;
long long int func(long long int a)
{
	long long int i,j,k;k=a%10;
	for(i=a/10;i>0;i/=10)
	{
		j=i%10;
		if(j>k)
		  return 0;
		k=j;  
	}
	return 1;
}
int main()
{
	long long int i,j,k,n,p=0,t,u=0,q;char s[11];
	cin>>t;
	while(t--)
	{
		cin>>s;cin>>p;n=strlen(s);k=0;u++;q=0;
		for(i=0;i<=n-p;i++)
		{
			if(s[i]=='-')
			{
				k++;
				for(j=i;j<i+p;j++)
				{
					if(s[j]=='+')s[j]='-';
					else s[j]='+';
				}
			}
		}
		for(i=n-p;i<n;i++)
		{
			if(s[i]=='-'){cout<<"Case #"<<u<<": "<<"IMPOSSIBLE "<<endl;q=1;break;}
		}
		if(!q)
		cout<<"Case #"<<u<<": "<<k<<endl;
	}
}
