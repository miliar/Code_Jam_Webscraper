# include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int ntest,n;
	string s;
	cin >> ntest;
	for (int test = 1; test <= ntest; test++)
	{
		cin >> s >> n;
		int count = 0;
		for (int i=0; i<=s.size()-n; i++)
		if (s[i] == '-')
		{
			count++;
			for (int j=i; j<i+n; j++) if (s[j] == '-') s[j] = '+'; else s[j] = '-';
		}
		bool check = true;
		for (int i=0; i<s.size(); i++) if (s[i] != '+')
		{
			check = false;
			break;
		}
		cout << "Case #" << test << ": ";
		if (check) cout << count << "\n";
		else cout << "IMPOSSIBLE\n"; 
	}
}
