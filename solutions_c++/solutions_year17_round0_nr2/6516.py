#include <iostream>
#include <vector>
#include <string.h>
#include <queue>
#include <algorithm>
#include <cmath>
#include <set>
#include <stdio.h>
#include <map>

using namespace std;

#define speed ios::sync_with_stdio(false)
#define ll long long int
#define pb push_back

int main()
{
	speed;
	ll t,m=1;
	cin>>t;
	while(t--)
	{
		ll l,i,j,k,flag;
		string s;
		cin>>s;
		l = s.length();
		flag=0;
		for(i=0;i<l-1;i++)
		{
			if(s[i]<=s[i+1])
			{
				continue;
			}
			break;
		}
		if(i==(l-1))
		{
			cout<<"Case #"<<m++<<": ";
			cout<<s<<endl;
			continue;
		}
		for(i=0;i<l;i++)
		{
			if(s[i]=='0' || s[i]=='1')
			{
				continue;
			}
			flag=1;
			break;
		}
		if(!flag)
		{
			cout<<"Case #"<<m++<<": ";
			for(i=1;i<l;i++)
			{
				cout<<"9";
			}
			cout<<endl;
			continue;
		}
		for(i=0;i<l-1;i++)
		{
			if(s[i]<=s[i+1])
			{
				continue;
			}
			break;
		}
		s[i]--;
		k=i;
		for(j=i+1;j<l;j++)
		{
			s[j] = '9';
		}
		while(i>0)
		{
			if(s[i]<s[i-1])
			{
				s[i-1] = s[i];
				s[i] = '9';
			}
			i--;
		}
		cout<<"Case #"<<m++<<": ";
		for(i=0;i<l;i++)
		{
			if(s[i]!='0')
			{
				cout<<s[i];
			}
		}
		cout<<endl;
	}
	return 0;
}