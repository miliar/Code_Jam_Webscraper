#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <cstring>

using namespace std;

const long double EPS = 1e-9;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int c = 0; c < t; c++) {
		int n, p;
		cin >> n >> p;
		vector<int> a(p);
		for (int i = 0; i < n; i++) {
			int k;
			cin >> k;
			a[k % p]++;
		}
		int res = 0;
		res += a[0];
		if (p == 3) {
			int t = min(a[1], a[2]);
			res += t;
			a[1] -= t;
			a[2] -= t;
			res += a[1] / 3 + (bool)(a[1] % 3);
			res += a[2] / 3 + (bool)(a[2] % 3);//only 1 of them nonzero
		}
		else if (p == 2) {
			res += a[1] / 2 + (bool)(a[1] % 2);
		}
		else if (p == 4) {
			int t = min(a[1], a[3]);
			a[1] -= t;
			a[3] -= t;
			res += t;
			res += a[2] / 2;
			a[2] %= 2;
			res += (bool)(a[1] + a[2] + a[3]); //if anything - only 1 can be
		}
		cout << "Case #" << c + 1 << ": " << res << endl;

	}
	return 0;
}
