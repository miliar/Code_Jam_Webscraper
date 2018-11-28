#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	int p=1;
	while(t--)
	{
		string s;
		cin>>s;
		int k,i,cnt=0;
		cin>>k;
		for(i=0;i<=s.length()-k;i++)
		{
			if(s[i]=='-')
			{
				for(int j=i;j<i+k;j++)
				{
					if(s[j]=='+')
						s[j]='-';
					else if(s[j]=='-')
						s[j]='+';
				}
				cnt++;
				//cout<<"i = "<<i<<" "<<s<<"\n";
			}
		}

		for(;i<s.length();i++)
		{
			if(s[i]=='-')
				break;
		}
		if(i==s.length())
			cout<<"Case #"<<p<<": "<<cnt<<"\n";
		else
			cout<<"Case #"<<p<<": IMPOSSIBLE\n";
		p++;
	}
	return 0;
}