#include <bits/stdc++.h>

using namespace std;

string degrade_ans(int n)
{
	return string(n, '9');
}

string solve()
{
	string n;
	cin >> n;

	char prev = n.back();
	for (int i = n.size() - 2; i >= 0; i--) {
		if (n[i] > prev) {
			for (int j = i + 1; j < n.size(); j++) {
				n[j] = '9';
			}
			n[i] -= 1;
		}
		prev = n[i];
	}

	return '0' == n[0] ? n.substr(1) : n;
}

int main()
{
	int t;
	cin >> t;

	for (int cs = 1; cs <= t; cs++) {
		cout << "Case #" << cs << ": " << solve() << endl;
	}
}
