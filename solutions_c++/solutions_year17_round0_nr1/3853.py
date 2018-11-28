#include<bits/stdc++.h>
using namespace std;
#define lli long long int
int main()
{
	lli t,j;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		char str[1002];
		lli k,flag=0,ans=0,i,m;
		cin>>str>>k;
		for(i=0;i<=strlen(str)-k;i++)
		{
			if(str[i]=='-')
			{
				ans++;
				for(m=i;m<i+k;m++)
				{
					if(str[m]=='-')
					str[m]='+';
					else
					str[m]='-';
				}
			}
			
		}
		i--;
		for(;i<strlen(str);i++)
		{
			if(str[i]=='-')
			flag=1;
		}
		if(flag==1)
		cout<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
		else
		cout<<"Case #"<<j<<": "<<ans<<endl;
	}
	return 0;
}
