#include <iostream>
#include <string>
#include <vector>

using namespace std;

int r, c;
vector<string> v;

struct point {
	int x;
	int y;
};

struct child {
	char c;
	struct point min;
	struct point max;
};

void find_edge(struct child &ch) {
	for (int x = ch.min.x; x < r; ++x) {
		for (int y = 0; y < c; ++y) {
			if (v[x][y] == ch.c) {
				if (x < ch.min.x) ch.min.x = x;
				else if (x > ch.max.x) ch.max.x = x;
				if (y < ch.min.y) ch.min.y = y;
				else if (y > ch.max.y) ch.max.y = y;
			}
		}
	}
}

bool is_uniq(char c, vector<struct child> &alp) {
	for (int x = 0; x < alp.size(); ++x) {
		if (c == alp[x].c)
			return false;
	}
	return true;
}

void fill_in(struct child &ch) {
	for (int x = ch.min.x; x <= ch.max.x; ++x) {
		for (int y = ch.min.y; y <= ch.max.y; ++y) {
			v[x][y] = ch.c;
		}
	}
}

void expand(struct child &ch) {
	// y expansion to max
	for (int y = ch.min.y - 1; y >= 0; --y) {
		bool empty = true;
		for (int x = ch.min.x; x <= ch.max.x; ++x) {
			if (v[x][y] != '?') {
				empty = false;
				break;
			}
		}
		if (empty) {
			for (int x = ch.min.x; x <= ch.max.x; ++x) {
				v[x][y] = ch.c;
			}
			--ch.min.y;
		} else {
			break;
		}
	}
	for (int y = ch.max.y + 1; y < c; ++y) {
		bool empty = true;
		for (int x = ch.min.x; x <= ch.max.x; ++x) {
			if (v[x][y] != '?') {
				empty = false;
				break;
			}
		}
		if (empty) {
			for (int x = ch.min.x; x <= ch.max.x; ++x) {
				v[x][y] = ch.c;
			}
			++ch.max.y;
		} else {
			break;
		}
	}
	// x expansion to max
	for (int x = ch.min.x - 1; x >= 0; --x) {
		bool empty = true;
		for (int y = ch.min.y; y <= ch.max.y; ++y) {
			if (v[x][y] != '?') {
				empty = false;
				break;
			}
		}
		if (empty) {
			for (int y = ch.min.y; y <= ch.max.y; ++y) {
				v[x][y] = ch.c;
			}
			--ch.min.x;
		} else {
			break;
		}
	}
	for (int x = ch.max.x + 1; x < r; ++x) {
		bool empty = true;
		for (int y = ch.min.y; y <= ch.max.y; ++y) {
			if (v[x][y] != '?') {
				empty = false;
				break;
			}
		}
		if (empty) {
			for (int y = ch.min.y; y <= ch.max.y; ++y) {
				v[x][y] = ch.c;
			}
			++ch.max.x;
		} else {
			break;
		}
	}
}

int main(int argc, char *argv[]) {
	int t;
	cin >> t;
	for (int _ = 0; _ < t; ++_) {
		vector<string> _v;
		v = _v;
		cin >> r >> c;
		vector<struct child> alp;
		for (int i = 0; i < r; ++i) {
			string s;
			cin >> s;
			v.push_back(s);
		}
		for (int i = 0; i < r; ++i) {
			for (int j = 0; j < c; ++j) {
				if (v[i][j] != '?' && is_uniq(v[i][j], alp)) {
					struct child ch = {
						.c = v[i][j],
						.min = {
							.x = i,
							.y = j,
						},
						.max = {
							.x = i,
							.y = j,
						}
					};
					find_edge(ch);
					fill_in(ch);
					alp.push_back(ch);
				}
			}
		}
		// cout << "Fill in:" << endl;
		// for (int x = 0; x < v.size(); ++x) {
		// 	cout << v[x] << endl;
		// }
		for (int x = 0; x < alp.size(); ++x) {
			expand(alp[x]);
			// cout << "Expand: " << alp[x].c << ":" << endl;
			// for (int i = 0; i < v.size(); ++i) {
			// 	cout << v[i] << endl;
			// }
		}
		cout << "Case #" << _ + 1 << ":" << endl;
		for (int x = 0; x < v.size(); ++x) {
			cout << v[x] << endl;
		}
	}
}
