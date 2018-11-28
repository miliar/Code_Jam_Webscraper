#include<bits/stdc++.h>
using namespace std;
string rev(string &s ,int j,int k)
{
	int p=j;
	for(p;p<j+k;p++)
	{
		if(s[p]=='+')
		s[p]='-';
		else
		s[p]='+';
	}
	return s;
}
int main()
{
	//ios_base :: sync_with_stdio(false);cin.tie(0);
	freopen("A-large.in","r",stdin);
freopen("out.txt","w",stdout);
	int t,i=1;
	cin>>t;
	while(i<=t)
	{
		int j,k,l=0;
		string s;
		cin>>s;
		cin>>k;
		for(j=0;j<=s.size()-k;j++)
		{
			if(s[j]=='-')
			{
			 s=rev(s,j,k);
			 l++;	
			}
		}
		while(j<s.size())
		{
			if(s[j]=='-')
			{
				l=-1;
				break;
			}
			j++;
		}
		if(l==-1)
		cout<<"Case #"<<i<<": IMPOSSIBLE\n";
		else
		cout<<"Case #"<<i<<": "<<l<<"\n";
		i++;
	}
	return 0;
}

