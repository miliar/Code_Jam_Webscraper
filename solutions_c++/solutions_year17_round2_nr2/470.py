#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <vector>

#define ST first
#define ND second
#define MP make_pair
#define PB push_back

using namespace std;

typedef long long int lld;
typedef pair<int, int> pii;


int nr[255];

string col_nr = "RYBGVO";

string equal(int c, int lst, int fi) {
	int co[3];
	co[0] = (fi + 1) % 3;
	if ((lst + 1) % 3 != co[0]) {
		co[2] = (lst + 1) % 3;
	} else {
		co[2] = (lst + 2) % 3;
	}
	co[1] = 3 - co[0] - co[2];
	string res = "";
	for (int i=0; i<c; i++) {
		for (int j=0; j<3; j++) {
			res += col_nr[co[j]];
		}
	}
	//cout << co[0] << co[1] << co[2] << " " << fi << " " << lst << endl;
	return res;
}

string solve_small(int r, int y, int b) {
	if (r > y + b || y > r + b || b > r + y) {
		return "IMPOSSIBLE";
	}
	string res = "";
	int cnt[] = {r, y, b};

	if (r == y && r == b) {
		return equal(r, 0, 1);
	}

	if (r >= y && r >= b) {
		res += "R";
		cnt[0]--;
	} else if (y >= r && y >= b) {
		res += "Y";
		cnt[1]--;
	} else {
		res += "B";
		cnt[2]--;
	}

	while (cnt[0] != cnt[1] || cnt[0] != cnt[2] || cnt[1] != cnt[2]) {
		char last = res[res.size() - 1];
		int mx_cnt = 0, curr;
		for (int i=0; i<3; i++) {
			if (i != nr[last]) {
				if (cnt[i] > mx_cnt) {
					mx_cnt = cnt[i];
					curr = i;
				}
			}
		}
		res += string(1, col_nr[curr]);
		cnt[curr]--;
	}
	//cout << res << endl;
	//cout << equal(cnt[0], nr[res[0]], nr[res[res.size()-1]]) << endl;
	return res + equal(cnt[0], nr[res[0]], nr[res[res.size()-1]]);
}


string special(int t[6]) {
	int nonzero = 0;
	for (int i=0; i<6; i++) {
		if (t[i] > 0) {
			nonzero++;
		}
	}
	for (int i=0; i<3; i++) {
		if (t[i] == t[i+3] && t[i] > 0) {
			if (nonzero != 2) {
				return "IMPOSSIBLE";
			}
			else {
				string res = "";
				for (int j=0; j<t[i]; j++) {
					res += string(1, col_nr[i]);
					res += string(1, col_nr[i+3]);
				}
				return res;
			}
		}
	}
	return "";
}

bool test_small(string res, int r, int y, int b) {
	if (res == "IMPOSSIBLE") {
		return true;
	}
	for (int i=0; i<int(res.size()); i++) {
		if (res[i] == 'R') {
			r--;
		} else if (res[i] == 'Y') {
			y--;
		} else {
			b--;
		}
		if (res[i] == res[(i+1)%res.size()]) {
//			cerr << "dupa" << endl;
			return false;
		}
	}
	if (r != 0 || y != 0 || b != 0) {
		return false;
//		cerr << r << " " << y << " " << b << endl;
	}
	return true;
}

void solve_case() {
	int n, t[6];
//	cin >> n >> r    >> o    >> y    >> g    >> b    >> v;
	cin >> n >> t[0] >> t[5] >> t[1] >> t[3] >> t[2] >> t[4];
	string sp = special(t);
	if (sp != "") {
		cout << sp << endl;
		return;
	}

	t[0] -= t[3];
	t[1] -= t[4];
	t[2] -= t[5];

	string res = solve_small(t[0], t[1], t[2]);
	
	if (!test_small(res, t[0], t[1], t[2])) {
		cerr << t[0] << " " << t[1] << " " << t[2] << endl;
	}

	if (res == "IMPOSSIBLE") {
		cout << "IMPOSSIBLE" << endl;
		return;
	}

	for (int i=0; i<int(res.size()); i++) {
		if (res[i] == 'R') {
			if (t[3] > 0) {
				cout << "RGR";
				t[3]--;
			} else {
				cout << "R";
			}
		} else if (res[i] == 'Y') {
			if (t[4] > 0) {
				cout << "YVY";
				t[4]--;
			} else {
				cout << "Y";
			}
		} else {
			if (t[5] > 0) {
				cout << "BOB";
				t[5]--;
			} else {
				cout << "B";
			}
		}
	}
	cout << endl;
}


int main () {
	nr['R'] = 0;
	nr['Y'] = 1;
	nr['B'] = 2;

    int te;
	cin >> te;
	for (int tt=1; tt<=te; tt++) {
		cout << "Case #" << tt << ": ";
		solve_case();
	}
}
