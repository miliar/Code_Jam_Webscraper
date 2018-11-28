#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
	freopen("inp.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	std::ios::sync_with_stdio(false);
	cin.tie(NULL);
	int tc;
	cin >> tc;
	for (int t = 0; t < tc; ++t) {
		string s;
		int l;
		cin >> s >> l;
		int flag = 1;
		int ans = 0;
		int n = s.length();
		vector <int> a(n, 0), b(l, 1);
		for (int i = 0; i < n; ++i) {
			if (s[i] == '-') {
				a[i] = 1;
			}
		}
		int j = 0;
		while (j < n) {
			while (j < n && !a[j]) ++j;
			if (j == n) break;
			if (j + l <= n) {
				for (int t = j; t < j + l; ++t) {
					a[t] = (a[t] + 1) % 2;
				}
				++ans;
			} else {
				flag = 0;
				break;
			}
		}
		///
		cout << "Case #" << t + 1 << ": ";
		if (flag) {
			cout << ans << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
	}
	fclose (stdout);
	fclose (stdin);
	return 0;
}