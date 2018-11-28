#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool check(vector<char> &v)
{
	for (int i = 0; i < v.size(); i++) {
		if (v[i] == '-') return false;
	}
	return true;
}

void flip(vector<char> &v, int start, int count)
{
	for (int i = start; i < start + count; i++) {
		v[i] = v[i] == '+' ? '-' : '+';
	}
}

void solve()
{
	int k;
	string s;
	cin >> s >> k;

	int n = s.length();

	int res = 0;
	char cur;

	vector<char> v(n);
	for (int i = 0; i < n; i++)
		v[i] = s[i];
	
	for (int i = 0; i <= n - k; i++) {
		cur = v[i];
		if (cur == '-') {
			flip(v, i, k);
			res++;
		}
	}
	if (check(v)) cout << res;
	else cout << "IMPOSSIBLE";
}

int main()
{
	freopen("small.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}

	return 0;
}