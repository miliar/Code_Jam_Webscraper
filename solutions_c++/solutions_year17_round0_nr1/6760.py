#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>

#pragma warning(disable:4996)

using namespace std;

int TI, T;

void flip(bool *side, int pos, int cnt)
{
	while (cnt > 0)
	{
		side[pos] = !side[pos];
		pos++;
		cnt--;
	}
}

int solve(string s, int n)
{
	bool side[1009];
	int i, l = s.length();
	for (i = 0; i < l; i++)
	{
		if (s[i] == '+')
			side[i] = true;
		else
			side[i] = false;
	}

	int cnt = 0;
	for (i = 0; i < l; i++)
	{
		if (i + n > l)
			break;
		if (!side[i]) {
			flip(side, i, n);
			cnt++;
		}
	}

	for (i = 0; i < l; i++)
	{
		if (!side[i])
			return 999999;
	}
	return cnt;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	/*
	cout << 100 << endl;
	for (int i = 0; i < 100; i++)
	{
		for (int j = 0; j < 500; j++) {
			cout << "-+";
		}
		cout << " 99" << endl;
	}
	return 0;
	*/
	cin >> T;
	for (TI = 0; TI < T; TI++)
	{
		string s;
		int n;
		cin >> s >> n;
		int sol1, sol2, ans;
		sol1 = solve(s, n);
		s.reserve();
		sol2 = solve(s, n);
		ans = min(sol1, sol2);
		if (ans == 999999) {
			cout << "Case #" << TI + 1 << ": " << "IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << TI + 1 << ": " << ans << endl;
		}
	}
	return 0;
}