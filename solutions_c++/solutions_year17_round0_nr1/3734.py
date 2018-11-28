#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <list>
#include <stdio.h>
#include <time.h>
#include <assert.h>
#include <math.h>
typedef long long ll;
typedef long double ld;
using namespace std;

const int SZ = 1e5 + 10;
const int INF = 1e9;

string x;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false);

	int t;
	cin >> t;
	for (int testn = 1; testn <= t; testn++) {
		int k;
		cin >> x >> k;
		int ans = 0;
		for (int i = 0; i <= x.length() - k; i++)
			if (x[i] == '-') {
				ans++;
				for (int j = i; j < i + k; j++)
					x[j] = (x[j] == '+' ? '-' : '+');
			}
		bool ok = true;
		for (int i = x.length() - k; i < x.length(); i++)
			if (x[i] != '+')
				ok = false;
		cout << "Case #" << testn << ": ";
		if (ok)
			cout << ans;
		else
			cout << "IMPOSSIBLE";
		cout << "\n";
		cerr << testn << "\n";
	}

	return 0;
}