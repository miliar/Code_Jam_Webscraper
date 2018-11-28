#include <bits/stdc++.h>

#define ff first
#define ss second
#define pii pair < int, int >
#define puba push_back

using namespace std;

typedef long long LL;

void impossible() {
	cout << "IMPOSSIBLE" << endl;
}

int n, r, o, y, g, b, v;

bool pr(int compr, int elem, string const & s) {
	if (compr == elem && compr != 0) {
		if (compr + elem != n) {
			impossible();
		}
		else {
			for (int i = 0; i < compr; ++i) {
				cout << s;
			}
			cout << endl;
		}
		return true;
	}
	return false;
}



string get_ans(int r, int y, int b) {
	vector<pair<int, char>> vec;
	vec.puba({r, 'R'});
	vec.puba({y, 'Y'});
	vec.puba({b, 'B'});

	sort(vec.begin(), vec.end());

	if (vec[2].ff > vec[1].ff + vec[0].ff) {
		return "";
	}

	int n = r + y + b;
	char ans[n];

	for (int i = 0; i < n; ++i) {
		ans[i] = '#';
	}

	for (int i = 0; i < vec[2].ff; ++i) {
		ans[2 * i] = vec[2].ss;
	}

	for (int i = 0; i < vec[1].ff - vec[0].ff; ++i) {
		ans[2 * i + 1] = vec[1].ss;
	}

	vector < int > emp;

	for (int i = 0; i < n; ++i) {
		if (ans[i] == '#') {
			emp.puba(i);
		}
	}

	for (int i = 0; i < vec[0].ff; ++i) {
		ans[emp[2 * i]] = vec[0].ss;
		ans[emp[2 * i + 1]] = vec[1].ss;
	}



	string ret;

	for (int i = 0; i < n; ++i) {
		ret += ans[i];
	}
	return ret;
}


int main() {
	int t;
	cin >> t;
	for (int q = 1; q <= t; ++q) {
		cout << "Case #" << q << ": ";
		cin >> n;

		cin >> r >> o >> y >> g >> b >> v;

		if (o > b || v > y || g > r) {
			impossible();
			continue;
		}

		if (pr(o, b, "OB")) continue;
		if (pr(v, y, "VY")) continue;
		if (pr(g, r, "GR")) continue;


		r -= g;
		y -= v;
		b -= o;

		string ans = get_ans(r, y, b);
		if (ans == "") {
			impossible();
			continue;
		}


		bool r_flag = false, y_flag = false, b_flag = false;
		
		for (char c : ans) {
			cout << c;
			if (!r_flag && c == 'R') {
				for (int i = 0; i < g; ++i) {
					cout << "GR";
				}
				r_flag = true;
			}
			if (!y_flag && c == 'Y') {
				for (int i = 0; i < v; ++i) {
					cout << "VY";
				}
				y_flag = true;
			}
			if (!b_flag && c == 'B') {
				for (int i = 0; i < o; ++i) {
					cout << "OB";
				}
				b_flag = true;
			}
		}

		cout << endl;
	}
	return 0;
}