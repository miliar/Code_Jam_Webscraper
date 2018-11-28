#include <iostream>
#include <vector>
#include <utility>
#include <iomanip>
#include <deque>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstdio>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int c = 0; c < t; c++) {
		string s;
		int k, res = 0;
		cin >> s >> k;
		vector<bool> a(s.size());
		for (int i = 0; i < s.size(); i++)
			a[i] = (s[i] == '-' ? 1 : 0);
		for (int i = 0; i < s.size() - k + 1; i++) {
			if (a[i]) {
				for (int j = 0; j < k; j++)
					a[i + j] = !a[i + j];
				res++;
			}
		}
		bool q = false;
		for (int i = s.size() - k + 1; i < s.size(); i++)
			q |= a[i];
		cout << "Case #" << c + 1 << ": ";
		if (!q)
			cout << res << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
