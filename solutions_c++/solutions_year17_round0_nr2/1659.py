#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;

	for(int gh=1;gh<=t;gh++)
	{
		string s;
		cin>>s;

		for(int i=s.length()-2;i>=0;i--)
		{
			if(s[i]>s[i+1])
			{
				s[i]--;
				for(int j=i+1;j<s.length();j++)
					s[j]='9';
			}
		}

		for(int i=0;i<s.length();i++)
		{
			if(s[i]!='0')
			{
				s = s.substr(i);
				break;
			}
		}

		cout<<"Case #"<<gh<<": "<<s<<endl;
	}

	return 0;
}