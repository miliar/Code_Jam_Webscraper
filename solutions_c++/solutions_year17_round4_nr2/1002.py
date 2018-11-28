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
	for (int cc = 0; cc < t; cc++) {
		int n, c, m;
		cin >> n >> c >> m;
		multiset<pair<int, int> > s;
		vector<int> cnt(n + 1);
		for (int i = 0; i < m; i++) {
			int p, b;
			cin >> p >> b;
			s.insert({ p, b });
			cnt[p]++;

		}
		multiset<pair<int, int> > saved = s;
		int res = 0;
		while (!s.empty()) {
			res++;
			vector<bool> man_was(c + 1, false);
			int cur_place = 1;
			vector<multiset<pair<int, int> >::iterator> tmp;
			for (multiset<pair<int, int> >::iterator x = s.begin(); x != s.end(); x++) {
				pair<int, int> el = *x;
				if (!man_was[el.second] && cur_place <= el.first) {
					tmp.push_back(x);
					man_was[el.second] = true;
					cur_place++;
				}
			}
			for (auto x : tmp) {
				s.erase(x);
			}
		}
		/*
		s = saved;
		for (int j = 0; j < res; j++) {
			vector<bool> man_was(c + 1, false), space_was(n + 1, false);
			vector<multiset<pair<int, int> >::iterator> tmp;
			for (multiset<pair<int, int> >::iterator x = s.begin(); x != s.end(); x++) {
				pair<int, int> el = *x;
				if (!man_was[el.second] && !space_was[el.first]) {
					tmp.push_back(x);
					man_was[el.second] = true;
					space_was[el.first] = true;
				}
			}
			for (auto x : tmp) {
				s.erase(x);
			}
		}//1st method
		*/
		int shift = 0;
		for (int i = 0; i < n + 1; i++) {
			shift += max(cnt[i] - res, 0);
		}
		cout << "Case #" << cc + 1 << ": " << res << ' ' << shift<< endl;

	}
	return 0;
}
