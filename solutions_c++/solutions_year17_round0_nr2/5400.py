#include <bits/stdc++.h>
using namespace std;

long long get(long long n)
{if(n/10==0)return n;
	string s="0000000000000000000";
	long long t=n;
	int count=0;
	while(t)
	{
       count++;
       s[19-count]=t%10;
       
       t/=10;
	}
	int p =20;
		for(int i=17;i>18-count;i--)
		{
           if(s[i]<=s[i+1])
           continue;
           s[i+1]=9;
           s[i]=s[i]-1;
           p=i+1;
		}
		int j=0;
	for(int i=0;i<19;i++)
	{
		if(s[i])
		{
			j=i;break;
		}
	}
	t=0;
	for(int i=j;i<19;i++)
	{
		if(i<p)
		t=t*10+s[i];
	     else
	     	t=t*10+9;
	}
	return t;
}
int main()
{
	int t;
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		long long n;
		cin>>n;
		n=get(n);
		cout<<"Case #"<<z<<": "<<<<endl;
	}
	return 0;
}
