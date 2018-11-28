#include <bits/stdc++.h>
using namespace std;

string s;

int n, T, cont = 0, k;

int main()
{
	ios::sync_with_stdio(false); cin.tie(0);

	cin>>T;

	for(int t = 1; t <= T; t++)
	{
		cin>>s>>k;

		cont = 0;

		bool ok = true;

		for(int i = 0; i< s.size() - k + 1; i++)
		{
			if(s[i] == '-')
			{
				for(int j = 0; j< k; j++)
				{
					if(s[i + j] == '-') s[i + j] = '+';
					else s[i + j] = '-';
				}
				cont++;
			}
		}

		cout<<"Case #"<<t<<": ";

		for(int i = 0; i<s.size(); i++) if(s[i] == '-') ok = false;

		if(!ok) cout<<"IMPOSSIBLE\n";
		else cout<<cont<<"\n";

	}
}