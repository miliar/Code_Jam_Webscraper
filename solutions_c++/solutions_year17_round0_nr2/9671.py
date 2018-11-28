#include <bits/stdc++.h>
#define ll long long
using namespace std;
//vector <ll> a;
//vector <ll> dp;
int main()
{
	
	int j,i,t,len,k;
	string s,s1;
	ifstream input;
	ofstream output;
	input.open("B-large.in");
	output.open("output.txt");
	input>>t;
	for(j=1;j<=t;j++)
	{
		input>>s;
		len=s.length();
		if(len==1) output<<"Case #"<<j<<": "<<s<<endl;
		else
		{
			for(i=len-1;i>=1;i--)
			{
				if(s[i]<s[i-1])
				{
					for(k=i;k<=len-1;k++) s[k]='9';
					s[i-1]=s[i-1]-1;
				}
			}
			if(s[0]=='0') s1=s.substr(1,len-1);
			else s1=s;
			output<<"Case #"<<j<<": "<<s1<<endl;
		}
	}
	input.close();
	output.close();
}
