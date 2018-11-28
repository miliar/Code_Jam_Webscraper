#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void solve()
{
	long long n;
	cin >> n;

	vector<int> v;

	while (n > 0) {
		v.push_back(n % 10);
		n /= 10;
	}

	int last9Idx = -1;

	for (int i = 0; i < v.size() - 1; i++) {
		if (v[i] < v[i + 1]) {
			last9Idx = i;
			while (v[i + 1] == 0) {
				last9Idx = i + 1;
				i++;
			}
			v[i + 1]--;
		}
	}
	bool b = false;
	for (int i = v.size() - 1; i >= 0; i--) {
		if (i <= last9Idx) {
			cout << 9;
			continue;
		}
		if (v[i] != 0) {
			b = true;
			cout << v[i];
		} else {
			if (b) {
				cout << v[i];
			}
		}
	}
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