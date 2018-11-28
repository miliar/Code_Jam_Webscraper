#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int test;
	cin >> test;
	int a[1111];
	for(int t = 1; t <= test; t++)
	{
		string s;
		int k;
		cin >> s >> k;
		memset(a, 0, sizeof a);
		bool ok = true;
		for(int i = 0; i < s.length(); i++)
		{
			int times = a[i];
			if(i >= k) times -= a[i-k];
			if(s[i] == '-') times++;
			if(i > s.length()-k && times%2) ok = false;
			a[i] += times % 2;
			a[i+1] = a[i];
		}
		cout << "Case #" << t << ": ";
		if(!ok) cout << "IMPOSSIBLE\n";
		else cout <<  a[s.length() - 1] << "\n";
	}
	return 0;
}