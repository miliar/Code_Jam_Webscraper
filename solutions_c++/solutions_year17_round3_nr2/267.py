#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdio>
#include <cassert>
using namespace std;

#define REP(i, n) for (int i = 0; i < (int)(n); i++)

void openFiles() {
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
	//freopen("test.in", "rt", stdin);
	//freopen("test.out", "wt", stdout);
#endif
}

typedef pair<int, int> pii;
typedef pair<pii, int> piii;

vector<int> f, s, fs;

template <class T, class U>
ostream& operator<<(ostream& os, const pair<T, U>& p) {
	os << "[" << p.first << ", " << p.second << "]";
	return os;
}

template <class T>
ostream& operator<<(ostream& os, const vector<T>& v) {
	os<<"[";for(int i=0;i<v.size();i++)os<<" "<<v[i];os<<" ]";
    return os;
}

void add(int r, int type) {
	if (type == 0) {
		f.push_back(r);
	} else if (type == 1) {
		s.push_back(r);
	}
}

void solve() {
	f.clear(); s.clear(); fs.clear();
	int n, m; scanf("%d %d ", &n, &m);
	vector<pii> sn(n), sm(m);
	REP(i, n) scanf("%d %d ", &sn[i].first, &sn[i].second);
	REP(i, m) scanf("%d %d ", &sm[i].first, &sm[i].second);

	vector<piii> v(n + m);
	REP(i, n) {
		v[i].first = sn[i];
		v[i].second = 0;
	}
	REP(i, m) {
		v[n + i].first = sm[i];
		v[n + i].second = 1;
	}

	sort(v.begin(), v.end());
	//cout << v << endl;
	
	// add tails
	int last = n + m - 1;
	int dayStart = v[0].first.first;
	int dayEnd = 1440 - v[last].first.second;
	if (v[0].second == v[last].second) {
		add(dayStart + dayEnd, v[0].second);
	} else {
		fs.push_back(dayStart + dayEnd);
	}

	vector<int> t(2);
	REP(i, n + m) {
		int duration = v[i].first.second - v[i].first.first;
		int type = v[i].second;
		t[type] += duration;
		if (i > 0) {
			int blank = v[i].first.first - v[i - 1].first.second;
			int prevType = v[i - 1].second;
			if (prevType == type) {
				add(blank, type);
			} else {
				fs.push_back(blank);
			}
		}
	}
	int switches = fs.size();

	sort(f.begin(), f.end());
	sort(s.begin(), s.end());

	REP(i, f.size()) {
		if (t[0] + f[i] <= 720) {
			t[0] += f[i];
		} else {
			switches += 2;
		}
	}

	REP(i, s.size()) {
		if (t[1] + s[i] <= 720) {
			t[1] += s[i];
		} else {
			switches += 2;
		}
	}

	printf("%d\n", max(2, switches));
	// cout << "f = " << f << endl;
	// cout << "s = " << s << endl;
	// cout << "fs = " << fs << endl;

	// cout << "t = " << t << endl;
}

int main() {
    openFiles();
    int n; scanf("%d ", &n);
    for (int i = 0; i < n; i++) {
            printf("Case #%d: ", i + 1);
            solve();
    }
    return 0;
}
