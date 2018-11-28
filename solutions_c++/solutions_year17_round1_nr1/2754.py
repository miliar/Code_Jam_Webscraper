#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

typedef pair<int, int> P;

int main() {
	string ss = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int r, c;
		cin >> r >> c;
		vector< vector<char> > ans(r, vector<char>(c));
		vector<P> dd[26];
		vector<int> ll(26, 1);
		char cc;
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				cin >> cc;
				ans[j][k] = cc;
				if (cc != '?') {
					dd[cc - 'A'].push_back(P(j, k));
					ll[cc - 'A'] = 0;
				}
			}
		}
		vector<P> d2[26];
		for (int j = 0; j < 26; j++) {
			if (dd[j].size() != 0) {
				int maxj, minj, maxk, mink;
				maxj = minj = dd[j][0].first;
				maxk = mink = dd[j][0].second;
				for (int k = 0; k < dd[j].size(); k++) {
					maxj = max(maxj, dd[j][k].first);
					minj = min(minj, dd[j][k].first);
					maxk = max(maxk, dd[j][k].second);
					mink = min(mink, dd[j][k].second);
				}
				for (int jj = minj; jj <= maxj; jj++) {
					for (int kk = mink; kk <= maxk; kk++) {
						ans[jj][kk] = ss[j];
					}
				}
				d2[j].push_back(P(minj, mink));
				d2[j].push_back(P(maxj, maxk));
			}
		}
		for (int j = 0; j < 26; j++) {
			if (dd[j].size() != 0) {
				bool h = true;
				int minj = d2[j][0].first;
				int mink = d2[j][0].second;
				int maxj = d2[j][1].first;
				int maxk = d2[j][1].second;
				for (int j2 = minj - 1; j2 >= 0; j2--) {
					for (int k2 = mink; k2 <= maxk; k2++) {
						if (ans[j2][k2] != '?') {
							h = false;
							break;
						}
					}
					if (h) {
						for (int k2 = mink; k2 <= maxk; k2++) {
							ans[j2][k2] = ss[j];
						}
						minj--;
					}
					else {
						break;
					}
				}
				h = true;
				for (int j2 = maxj + 1; j2 < r; j2++) {
					for (int k2 = mink; k2 <= maxk; k2++) {
						if (ans[j2][k2] != '?') {
							h = false;
							break;
						}
					}
					if (h) {
						for (int k2 = mink; k2 <= maxk; k2++) {
							ans[j2][k2] = ss[j];
						}
						maxj++;
					}
					else {
						break;
					}
				}
				d2[j][0].first = minj;
				d2[j][1].first = maxj;
			}
		}
		for (int j = 0; j < 26; j++) {
			if (dd[j].size() != 0) {
				bool h = true;
				int minj = d2[j][0].first;
				int mink = d2[j][0].second;
				int maxj = d2[j][1].first;
				int maxk = d2[j][1].second;
				h = true;
				for (int k2 = mink - 1; k2 >= 0; k2--) {
					for (int j2 = minj; j2 <= maxj; j2++) {
						if (ans[j2][k2] != '?') {
							h = false;
							break;
						}
					}
					if (h) {
						for (int j2 = minj; j2 <= maxj; j2++) {
							ans[j2][k2] = ss[j];
						}
						mink--;
					}
					else {
						break;
					}
				}
				h = true;
				for (int k2 = maxk + 1; k2 < c; k2++) {
					for (int j2 = minj; j2 <= maxj; j2++) {
						if (ans[j2][k2] != '?') {
							h = false;
							break;
						}
					}
					if (h) {
						for (int j2 = minj; j2 <= maxj; j2++) {
							ans[j2][k2] = ss[j];
						}
						maxk++;
					}
					else {
						break;
					}
				}
			}
		}
		printf("Case #%d:\n", i+1);
		for (int j = 0; j < r; j++) {
			for (int k = 0; k < c; k++) {
				cout << ans[j][k];
			}
			cout << endl;
		}
	}
	return 0;
}