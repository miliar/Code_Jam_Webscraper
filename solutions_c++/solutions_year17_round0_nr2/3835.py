#include <bits/stdc++.h>
using namespace std;
string s;
bool check=0;
bool flag=0;
int index=0;
void fitb(int x)
{
	if(x==0)
	{
		if(s[x]=='0')
		{
			check=1;
			return ;
		}
		else
		{
			flag=1;
			index=x;
			return ;
		}
	}
	if(s[x-1]<=s[x])
	{
		flag=1;
		index=x;
		return ;
	}
	if(s[x-1]>s[x])
	{
		s[x-1]--;
		s[x]='9';
		fitb(x-1);
	}
}
void fitt(int x)
{
	if(x==0&&s[x]=='1')
	{
		check=1;
		return ;
	}
	s[x+1]='9';
	s[x]--;
	fitb(x);
}
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int n;
	cin>>n;
	for(int z=1;z<=n;z++)
	{
		check=0;
		flag=0;
		cin>>s;
		for(int i=0;i<s.length()-1;i++)
		{
		if(s[i]>s[i+1])
		fitt(i);
		if(check)
		break;
		if(flag)
		break;
		}
		if(check)
		{
		printf("Case #%d: ",z);
		for(int i=0;i<s.length()-1;i++)
		cout<<""<<"9";
		cout<<endl;
		continue;
		}
		if(flag)
		{
			printf("Case #%d: ",z);
			for(int i=0;i<=index;i++)
			cout<<s[i];
			for(int i=index+1;i<s.length();i++)
			cout<<"9";
			cout<<endl;
			continue;
		}
		else
		{
			printf("Case #%d: ",z);
			cout<<s<<endl;
		}
	}
	return 0;
}
