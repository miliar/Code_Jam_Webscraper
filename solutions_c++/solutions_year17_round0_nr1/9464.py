//#include <bits/stdc++.h>
#include <iostream>
#include <stdio.h>
#include <map>
#include <string>
#include <algorithm>
#include <vector>
#include <string.h>
#include <stdlib.h>
#include <iomanip>
#include <queue>
using namespace std;



void function()
{
	string s;
	int k;
	cin>>s>>k;
	int i,n=0;
	for(i=0;i<=s.length()-k;)
	{
		while(i<=s.length()-k&&s[i]=='+')
			++i;
		if(i>s.length()-k)
			break;
		for(int j=i;j<i+k;++j)
		{
			s[j]=(s[j]=='+')?'-':'+';
		}
		n++;
	}
	for(int j=i;j<s.length();++j)
	{
		if(s[j]=='-')
		{
			cout<<"IMPOSSIBLE"<<endl;
			return;
		}
	}
	cout<<n<<endl;
}
int main()
{
	//freopen("in","r",stdin);
	//freopen("D-out","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;++i)
	{
		cout<<"Case #"<<i<<": ";
		function();
	}
	
}
