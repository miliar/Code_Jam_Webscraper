#include <bits/stdc++.h>

using namespace std;

void flip(string &pk, int s, int e)
{
	for (int i = s; i < e; i++) {
		pk[i] = ('+' == pk[i]) ? '-' : '+';
	}
}

string solve()
{
	string pk;
	int k;
	cin >> pk >> k;

	int ans = 0, i = 0;
	for (i = 0; i < pk.size() - k + 1; i++) {
		if ('-' == pk[i]) {
			ans++;
			flip(pk, i, i + k);
		}
	}
	for (; i < pk.size(); i++) {
		if ('-' == pk[i]) {
			return "IMPOSSIBLE";
		}
	}

	return to_string(ans);
}

int main()
{
	int t;
	cin >> t;

	for (int cs = 1; cs <= t; cs++) {
		cout << "Case #" << cs << ": " << solve() << endl;
	}
}
