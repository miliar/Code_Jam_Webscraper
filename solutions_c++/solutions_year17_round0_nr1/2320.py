#pragma comment(linker, "/STACK:268435456")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <vector>
#include <math.h>
#include <set>
#include <map>
#include <queue>
#include <iomanip>
#include <assert.h>
#include <stack>
#include <deque>
#include <limits.h>
#include <memory.h>
#include <time.h>
//#include <unordered_map>
//#include <unordered_set>
using namespace std;

void prepare(string q)
{
#ifdef _DEBUG
	//system("color F0");
	freopen("input.txt", "r", stdin);
	freopen("output.txt","w",stdout);
#else
	if (q.size() != 0)
	{
		freopen((q + ".in").c_str(), "r", stdin);
		freopen((q + ".out").c_str(), "w", stdout);
	}
#endif
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	cin.tie(false);
}

void solve()
{
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; ++tt)
	{
		string s;
		int n;
		cin >> s >> n;
		int ans = 0;
		int sz = s.size();
		for (int i = 0; i + n <= sz; ++i)
		{
			if (s[i] == '-')
			{
				++ans;
				for (int j = i; j < i + n; ++j)
					s[j] = (s[j] == '-') ? '+' : '-';
			}
		}
		bool ki = false;
		for (int i = 0; i < sz; ++i)
			if (s[i] == '-')
				ki = true;
		cout << "Case #" << tt << ": ";
		if (ki)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;
	}
}

int main()
{
	prepare("");
	solve();
	return 0;
}