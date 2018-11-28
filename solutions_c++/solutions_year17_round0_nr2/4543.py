#include "bits/stdc++.h"
using namespace std;
typedef long long ll;
string s;
void bond()
{
	bool ok=true;
	while(ok)
	{
		int pos=-1;
		for(int i=s.size()-1;i>0;i--)
		{
			if(s[i]<s[i-1])
			{
				pos=i;
			}
		}
		if(pos==-1)
		{
			ok=false;
			continue;
		}
		s[pos-1]-=1;
		for(int i=pos;i<s.size();i++)
			s[i]='9';

	}
}
int main()
{
	int t;
	cin>>t;
	for(int case1=1;case1<=t;case1++)
	{
		cin>>s;
		bond();
		printf("Case #%d: ",case1);
		int i;
		for(i=0;i<s.size();i++)
		{
			if(s[i]!='0')break;
		}
		for(int j=i;j<s.size();j++)
			cout<<s[j];
		printf("\n");
	}

	return 0;
}
