#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <vector>
#include <numeric>
using namespace std;

int main() {
	ifstream cin("C-small-1-attempt0.in");
	ofstream cout("C-small-1-attempt0.out");
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i){
		int n, k;
		cin >> n >> k;
		string s(n + 2, '.');
		s[0] = s[n + 1] = '0';
		vector<pair<int, int> > a(n + 2);
		a[0].first = 0; a[0].second = n;
		a[n + 1].first = n; a[n + 1].second = 0;
		for (int i = 1; i < n + 1; ++i) {
			a[i].first = i - 1;
			a[i].second = n - i;
		}
		for (int j = 0; j < k; ++j) {
			int start = 1, min_ = -1, max_ = -1;
			for (int q = 1; q < n + 1; ++q) {
				if (s[q] == '.') {
					int b = min(a[q].first, a[q].second);
					int c = max(a[q].first, a[q].second);
					if (b > min_) {
						min_ = b;
						max_ = c;
						start = q;
					}
					else if (b == min_ && max_ < c) {
						max_ = c;
						start = q;
					}
				}
			}
			s[start] = '0';
			for (int q = 1; q < n + 1; ++q) {
				int x = q - 1, y = q + 1;
				while (s[x] != '0') --x;
				while (s[y] != '0') ++y;
			a[q].first = q - x - 1;
				a[q].second = y - q - 1;
			}
			if (j == k - 1) {
				cout << "Case #" << i + 1 << ": " << max(a[start].first, a[start].second) << " " << min(a[start].first, a[start].second) << endl;
			}
		}
	}
	cin.close();
	cout.close();
	system("pause");
}
