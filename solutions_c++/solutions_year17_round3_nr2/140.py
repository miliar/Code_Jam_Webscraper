#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
using namespace std;

struct Act {
	int s;
	int e;
	int p;
	
	bool operator<(const Act& rhs) const {
		return s < rhs.s;
	}
};

int main() {
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		int ac, aj;
		cin >> ac >> aj;
		
		vector<Act> v(ac + aj);
		for (int i = 0; i < ac + aj; ++i) {
			cin >> v[i].s >> v[i].e;
			v[i].p = (i < ac ? 0 : 1);
		}

		sort(v.begin(), v.end());
		int sum[2] = {0, 0};
		multiset<int> gap[2];
		int first = v[0].p;
		int cur = first;
		int curs = v[0].s;
		int cure = v[0].e;
		int chg = 0;

		for (int i = 1; i < ac + aj; ++i) {
			if (v[i].p == cur) {
				gap[cur].insert(v[i].s - cure);
				cure = v[i].e;
			} else {
				sum[cur] += cure - curs;
				curs = v[i].s;
				cure = v[i].e;
				cur = v[i].p;
				++chg;
			}
		}
		sum[cur] += cure - curs;
		if (cur == first) {
			int g = 24*60 + v[0].s - cure;
			gap[cur].insert(g);
			sum[cur] += g;
		} else {
			++chg;
		}

		for (int p = 0; p < 2; ++p) {
			for (auto it = gap[p].rbegin(); it != gap[p].rend(); ++it) {
				if (sum[p] <= 720) {
					break;
				}
				sum[p] -= *it;
				chg += 2;
			}
		}

		cout << "Case #" << test << ": " << chg << endl;
	}
}
