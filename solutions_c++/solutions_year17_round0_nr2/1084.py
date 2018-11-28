#include <iostream>
#include <string>
#include <vector>

using namespace std;

void solve() {
	string s;
	cin >> s;
	int n = s.size();
	vector < int > a(n, 0);
	for (int i = 0; i < n; i++)
		a[i] = s[i] - '0';
	int len = 1;
	for (int i = 1; i < n; i++) {
		if (a[i] >= a[i - 1])
			len++;
		else
			break;
	}
	if (len == n) {
		cout << s << endl;
		return;
	}
	bool ok = false;
	for (int i = len - 1; i >= 0; i--) {
		if (i == 0 && a[i] > 1) {
			a[i]--;
			for (int j = 1; j < n; j++)
				a[j] = 9;
			ok = true;
			break;
		}
		if (i > 0 && a[i] - 1 >= a[i - 1]) {
			a[i]--;
			for (int j = i + 1; j < n ; j++)
				a[j] = 9;
			ok = true;
			break;
		}
	}
	if (!ok) {
		for (int i = 0; i < n - 1; i++)
			cout << 9;
		cout << endl;
		return;
	}
	for (int i = 0; i < n; i++)
		cout << a[i];
	cout << endl;
	return;
}

int main() {
	int test = 0;
	cin >> test;
	for (int i = 1; i <= test; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}