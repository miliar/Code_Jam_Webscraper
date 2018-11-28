#include<bits/stdc++.h>
using namespace std;
#define INF 1000000007
typedef long long int ll;
char str[20];
int main()
{
	ios_base::sync_with_stdio(false);
	ll t,i,ch,len,id,flag,cs;
	cin>>t;
	for(cs=1;cs<=t;cs++)
	{
		cin>>str;
		len=strlen(str);
		i=len-1;
		flag=0;
		while(i>=1 && flag==0)
		{
			//check for an already tidy no
			if(str[i-1]>str[i])
			{
				flag=1;
			}
			i--;
		}
		if(flag==0)  //already tidy
		{
			cout<<"Case #"<<cs<<":"<<" "<<str<<"\n";
		}
		else
		{
			i=len-1;
			while(i>=1)
			{
				if(str[i-1]>str[i])
				{
					ch=str[i-1];
					ch=ch-1;
					str[i-1]=ch;
					id=i;
				}
				i--;
			}
			if(str[0]=='0')
			{
				i=0;
				while(i<len-1)
				{
					str[i]='9';
					i++;
				}
				str[len-1]='\0';
			}
			else
			{
				for(i=id;i<len;i++)
				{
					str[i]='9';
				}
			}
			cout<<"Case #"<<cs<<":"<<" "<<str<<"\n";
		}
	}
	return(0);
}
