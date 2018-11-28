#include <bits/stdc++.h>
using namespace std;

main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,n,k;
	string s;
	ios::sync_with_stdio(false);
	cin >> t;
	for (int x = 1 ; x <= t ; x++)
	{
		cin >> s >> k;
		bool check = true;
		int coun = 0;
		if (k > s.length()) check =  false;
		for (int i = 0 ; i < s.length()-k+1 ; i++)
		{
			if (s[i] == '-')
			{
				coun++;
				for (int j = i ; j < i+k ; j++)
					if (s[j] == '-') s[j] = '+';
					else s[j] = '-';
			}
		}
		for (int i = s.length()-k+1 ; i < s.length() ; i++)
			if (s[i] == '-')
			{
				check = false;
				break;
			}
		cout<<"Case #"<<x<<": ";
		if (!check) cout<<"IMPOSSIBLE"<<endl;
		else cout<<coun<<endl;
	}
}
