#include <bits/stdc++.h>
using namespace std;
#define ll long long int

int main()
{
	ll t;
	cin>>t;
	string s;
	for(int z=1;z<=t;z++)
	{
		cin>>s;
		int i,l = s.length(),flag = 0;
		for(i=1;i<l;i++)
		{
			if(s[i] < s[i-1])
			{
				flag = 1;
				break;
			}
		}
		if(flag == 0)
		{
			cout<<"Case #"<<z<<": "<<s<<endl;
			continue;
		}
		flag = 0;
		for(int j = i-1;j>0;j--)
		{
			if(s[j] != s[j-1])
			{
				i = j+1;
				flag = 1;
				break;
			}
		}
		if(flag == 0)
		{
			i = 1;
		}
		for(int j = i;j<l;j++)
		{
			s[j] = '9';
		}
		s[i-1] = (char)(s[i-1] - 1);
		for(i=0;i<l;i++)
		{
			if(s[i] != '0')
				break;
		}
		string str = "";
		for(int j=i;j<l;j++)
		{
			str += s[j];
		}
		cout<<"Case #"<<z<<": "<<str<<endl;
	}
	return 0;
}