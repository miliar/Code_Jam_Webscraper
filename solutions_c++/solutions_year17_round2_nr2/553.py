#include <bits/stdc++.h>

using namespace std;

bool check(int a, int b)
{
	int d = (a - b + 6) % 6;
	return d != 1 && d != 5 && d != 0;
}

void solve()
{
	int n;
	cin >> n;
	int a[6];
	for(int i = 0; i < 6; i++)
		cin >> a[i];
	string str = "ROYGBV";
	vector<int> ans;
	for(int i = 0; i < n; i++)
	{
		int nev = -1;
		for(int j = 0; j < 6; j++)
		{
			if(a[j] == 0)
				continue;
			bool ok = ans.empty() || (check(ans.back(), j) && (nev == -1 || a[j] >= a[nev]));
			ok &= (i + 1 < n) || check(ans[0], j);
			if(ok)
				nev = j;
		}
		//cout << nev << endl;
		if(nev == -1)
		{
			cout << "IMPOSSIBLE" << endl;
			return;
		}
		a[nev]--;
		ans.push_back(nev);
	}
	for(auto it: ans)
		cout << str[it];
	cout << endl;
	
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
