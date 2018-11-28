#include<bits/stdc++.h>
using namespace std;
#define INF 1000000007
typedef long long int ll;
char str[10001];
int main()
{
	ios_base::sync_with_stdio(false);
	ll t,i,len,cnt,j,cs,k,flag;
	cin>>t;
	for(cs=1;cs<=t;cs++)
	{
		cin>>str>>k;
		i=0;
		len=strlen(str);
		cnt=flag=0;
		while(i<len && flag==0)
		{
			if(str[i]=='-')
			{
				if(i+k-1>=len)
				{
					flag=1;
				}
				else
				{
					j=i;
					while(j<len && j-i<k)
					{
						if(str[j]=='-')
						{
							str[j]='+';
						}
						else
						{
							str[j]='-';
						}
						j++;
					}
					cnt++;
				}
			}
			i++;
		}
		if(flag==1)
		{
			cout<<"Case #"<<cs<<":"<<" "<<"IMPOSSIBLE"<<"\n";
		}
		else
		{
			flag=0;
			i=0;
			while(i<len && flag==0)
			{
				if(str[i]=='-')
				{
					flag=1;
				}
				i++;
			}
			if(flag==1)
			{
				cout<<"Case #"<<cs<<":"<<" "<<"IMPOSSIBLE"<<"\n";
			}
			else
			{
				cout<<"Case #"<<cs<<":"<<" "<<cnt<<"\n";
			}
		}
		
	}
	return(0);
}
