#include<bits/stdc++.h>
using namespace std;

string s;

ifstream goo;
ofstream gle;

void solve()
{
	int n,a=0;
	goo>>s>>n;
	for(int i=0; i<=s.size()-n; i++)
	{
		if(s[i]=='-')
		{
			a++;
			for(int j=i; j<i+n; j++)
			{
				if(s[j]=='-') s[j]=43;
				else s[j]=45;
			}
		}
	}
	for(int i=s.size()-n; i<s.size(); i++)
	{
		if(s[i]=='-')
		{
			gle<<"IMPOSSIBLE\n";
			return;
		}
	}
	gle<<a<<"\n";
	return;
}

int main()
{
	goo.open("C:\\Users\\Mateusz\\Desktop\\Testy\\A-large (4).in");
	gle.open("C:\\Users\\Mateusz\\Desktop\\Testy\\tak.out");
	int t;
	goo>>t;
	for(int i=1; i<=t; i++)
	{
		gle<<"Case #"<<i<<": ";
		solve();
	}
	goo.close();
	gle.close();
	return 0;
}
