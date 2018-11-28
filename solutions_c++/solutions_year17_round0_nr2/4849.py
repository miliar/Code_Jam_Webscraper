#include <bits/stdc++.h>
#define ll long long int

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	int t,l,index;
	ll n;
	string s;
	cin>>t;
	for(int loop=1;loop<=t;loop++)
	{
		cin>>n;
		s="";
		while(n)
		{
			s += '0' + n%10;
			n/=10;
		}
		l=s.length();
		index = 0;
		for(int i=0;i<l-1;i++)
			if(s[i] < s[i+1])
			{
				s[i+1]--;
				index=i+1;
			}
		for(int i=0;i<index;i++)
			s[i] = '9';
		cout<<"Case #"<<loop<<": ";
		if(s[l-1] != '0')
			cout<<s[l-1];
		for(int i=l-2;i>=0;i--)
			cout<<s[i];
		cout<<"\n";
	}
	return 0;
}