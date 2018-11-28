#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <cmath>
#include <ctime>
#pragma comment (linker, "/STACK:256000000")

using namespace std;

void readData() {
}

int n, r, o, y, g, b, v;

map < char, string > M;

bool isGood(char a, char b) {
	string u = M[a];
	string v = M[b];
	for (int i = 0; i < u.size(); ++i) {
		for (int j = 0; j < v.size(); ++j) {
			if (u[i] == v[j]) {
				return false;
			}
		}
	}
	return true;
}

string solveStupid(int r, int o, int y, int g, int b, int v) {
	string res = string(r, 'R') + string(o, 'O') + string(y, 'Y') + string(g, 'G') + string(b, 'B') + string(v, 'V');
	sort(res.begin(), res.end());
	do {
		bool ok = true;
		for (int i = 1; i < res.size() && ok; ++i) {
			if (!isGood(res[i - 1], res[i])) {
				ok = false;
			}
		}
		if (res.size() > 1 && !isGood(res[0], res.back())) {
			ok = false;
		}
		if (ok) {
			return res;
		}
	} while (next_permutation(res.begin(), res.end()));
	return "IMPOSSIBLE";
}

vector < string > build(int r, int g, char X, char Y) {
	if (r == 0) {
		return vector < string >();
	}
	string start(1, X);
	--r;
	for (int i = 0; i < g; ++i) {
		start += Y;
		start += X;
		--r;
	}

	vector < string > res(1, start);
	for (int i = 0; i < r; ++i) {
		res.push_back(string(1, X));
	}
	return res;
}

string solveClever(int r, int o, int y, int g, int b, int v) {
	int n = r + o + y + g + b + v;
	int totalr = r + o + v;
	int totaly = o + g + y;
	int totalb = g + v + b;

	if (totalr * 2 > n || totaly * 2 > n || totalb * 2 > n) {
		return "IMPOSSIBLE";
	}

	if (o > b || v > y || g > r) {
		return "IMPOSSIBLE";
	}

	int bg = b - o;
	int yg = y - v;
	int rg = r - g;

	if (bg == 0 && b > 0) {
		if (b + o != n) {
			return "IMPOSSIBLE";
		}
		string res(n, ' ');
		for (int i = 0; i < n; i += 2) {
			res[i] = 'B';
			res[i + 1] = 'O';
		}
		return res;
	}
	if (yg == 0 && y > 0) {
		if (y + v != n) {
			return "IMPOSSIBLE";
		}
		string res(n, ' ');
		for (int i = 0; i < n; i += 2) {
			res[i] = 'Y';
			res[i + 1] = 'V';
		}
		return res;
	}
	if (rg == 0 && r > 0) {
		if (r + g != n) {
			return "IMPOSSIBLE";
		}
		string res(n, ' ');
		for (int i = 0; i < n; i += 2) {
			res[i] = 'R';
			res[i + 1] = 'G';
		}
		return res;
	}

	int nn = rg + yg + bg;
	vector < vector < string > > f(3);

	f[0] = build(r, g, 'R', 'G');
	f[1] = build(y, v, 'Y', 'V');
	f[2] = build(b, o, 'B', 'O');
	int a[3] = {rg, yg, bg};

	if (rg * 2 > nn || yg * 2 > nn || bg * 2 > nn) {
		return "IMPOSSIBLE";
	}

	for (int i = 0; i < 3; ++i) {
		for (int j = i + 1; j < 3; ++j) {
			if (a[j] > a[i]) {
				swap(a[j], a[i]);
				swap(f[j], f[i]);
			}
		}
	}

	vector < string > res(nn);
	for (int i = 0; i < nn; i += 2) {
		for (int j = 0; j < 3; ++j) {
			if (a[j] > 0) {
				res[i] = f[j].back();
				f[j].pop_back();
				--a[j];
				break;
			}
		}
	}
	for (int i = 1; i < nn; i += 2) {
		for (int j = 0; j < 3; ++j) {
			if (a[j] > 0) {
				res[i] = f[j].back();
				f[j].pop_back();
				--a[j];
				break;
			}
		}
	}

	string ans = "";
	for (int i = 0; i < res.size(); ++i) {
		ans += res[i];
	}

	bool ok = true;
	for (int i = 1; i < ans.size(); ++i) {
		if (!isGood(ans[i - 1], ans[i])) {
			ok = false;
		}
	}
	if (ans.size() > 1 && !isGood(ans[0], ans[n - 1])) {
		ok = false;
	}
	if (!ok) {
		cerr << "BAD" << endl;
	}
	return ans;
}

string solve(int r, int y, int b) {
	int a[3] = {r, y, b};
	string t = "RYB";

	for (int i = 0; i < 3; ++i) {
		for (int j = i + 1; j < 3; ++j) {
			if (a[j] > a[i]) {
				swap(a[j], a[i]);
				swap(t[j], t[i]);
			}
		}
	}

	string res(n, ' ');
	for (int i = 0; i < n; i += 2) {
		for (int j = 0; j < 3; ++j) {
			if (a[j] > 0) {
				res[i] = t[j];
				--a[j];
				break;
			}
		}
	}
	for (int i = 1; i < n; i += 2) {
		for (int j = 0; j < 3; ++j) {
			if (a[j] > 0) {
				res[i] = t[j];
				--a[j];
				break;
			}
		}
	}

	bool ok = true;
	for (int i = 1; i < n; ++i) {
		if (res[i] == res[i - 1] || (n > 1 && res[0] == res[n - 1])) {
			ok = false;
		}
	}

	if (!ok) {
		cerr << "BAD" << endl;
	}

	return res;
}

void solve(int test) {
	cin >> n >> r >> o >> y >> g >> b >> v;
	/*if (2 * r > n || 2 * y > n || 2 * b > n) {
		printf("Case #%d: IMPOSSIBLE\n", test);
		return ;
	}
	if (r + y + b != n) {
		printf("Case #%d: IMPOSSIBLE\n", test);
		return;
	}*/

	printf("Case #%d: %s\n", test, solveClever(r, o, y, g, b, v).c_str());
}

int main(int argc, char* argv[]) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	M['R'] = "R";
	M['Y'] = "Y";
	M['B'] = "B";
	M['O'] = "RY";
	M['G'] = "YB";
	M['V'] = "RB";

	/*int bound = 5;
	for (int r = 0; r <= bound; ++r) {
		for (int o = 0; o <= bound; ++o) {
			for (int y = 0; y <= bound; ++y) {
				//cerr << r << " " << o << " " << y << endl;
				for (int g = 0; g <= bound; ++g) {
					for (int b = 0; b <= bound; ++b) {
						for (int v = 0; v <= bound; ++v) {
							if (r + o + y + g + v + b < 3) {
								continue;
							}
							//string aa = solveStupid(r, o, y, g, b, v);
							string bb = solveClever(r, o, y, g, b, v);

							bool cana = (aa != "IMPOSSIBLE");
							bool canb = (bb != "IMPOSSIBLE");
							if (cana != canb) {
								cerr << r << " " << o << " " << y << " " << g << " " << b << " " << v << endl;
								cerr << aa << endl;
								cerr << bb << endl;
							}
						}
					}
				}
			}
		}
	}*/

	int left_bound, right_bound;

	/*freopen(argv[3], "w", stdout);	
	sscanf(argv[1], "%d", &left_bound);
	sscanf(argv[2], "%d", &right_bound);*/

	int t;
	cin >> t;
	left_bound = 1, right_bound = t;
	for (int i = 1; i <= t; ++i) {
		if (i >= left_bound && i <= right_bound) {
			solve(i);
		} else {
			readData();
		}
		cerr << i << ": " << clock() << endl;
	}

	return 0;
}
