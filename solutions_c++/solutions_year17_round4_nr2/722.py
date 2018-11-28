#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

typedef long long ll;
typedef vector <ll> vl;
typedef vector <pair <ll, ll>> vll;

void solve(int nn)
{
	int c, n, m;
	int ans1, ans2;
	int temp1, temp2;
	int kol1 = 0, kol2 = 0;
	int kol[1001];
	fill(kol, kol + 1001, 0);
	cin >> n >> c >> m;

	for (int i = 0; i < m; i++)
	{
		cin >> temp1 >> temp2;
		if (temp2 == 1)
			kol1++;
		else
			kol2++;
		kol[temp1]++;
	}

	ans1 = max(kol[1], max(kol1, kol2));
	int mx = 0;
	for (int i = 2; i <= 1000; i++)
		mx = max(mx, kol[i]);
	ans2 = max(0, mx - ans1);

	cout << "Case #" << nn + 1 << ": " << ans1 << ' ' << ans2;
	cout << endl;
}

int main()
{
	ios::sync_with_stdio(false);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
		solve(i);
	return 0;
}