#include <iostream>
#include <vector>
using namespace std;

void printr(int& g) {
	cout << "R";
	while (g > 0) {
		cout << "GR";
		--g;
	}
}

void printy(int& v) {
	cout << "Y";
	while (v > 0) {
		cout << "VY";
		--v;
	}
}

void printb(int& o) {
	cout << "B";
	while (o > 0) {
		cout << "OB";
		--o;
	}
}

int main() {
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		int n, r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;

		cout << "Case #" << test << ": ";

		if (o > 0) {
			if ((b + o < n && b <= o) || (b + o == n && b != o)) {
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
			if (b + o == n) {
				for (int i = 0; i < n; i += 2) {
					cout << "BO";
				}
				cout << endl;
				continue;
			}
			b -= o;
			n -= o;
		}

		if (g > 0) {
			if ((r + g < n && r <= g) || (r + g == n && r != g)) {
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
			if (r + g == n) {
				for (int i = 0; i < n; i += 2) {
					cout << "RG";
				}
				cout << endl;
				continue;
			}
			r -= g;
			n -= g;
		}

		if (v > 0) {
			if ((y + v < n && y <= v) || (y + v == n && y != v)) {
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
			if (y + v == n) {
				for (int i = 0; i < n; i += 2) {
					cout << "YV";
				}
				cout << endl;
				continue;
			}
			y -= v;
			n -= v;
		}

		if (r > y + b || y > b + r || b > y + r) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}

		if (r == 0) {
			if (y != b) {
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
			for (int i = 0; i < n; i += 2) {
				printy(v);
				printb(o);
			}
			cout << endl;
			continue;
		}

		if (y == 0) {
			if (r != b) {
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
			for (int i = 0; i < n; i += 2) {
				printr(g);
				printb(o);
			}
			cout << endl;
			continue;
		}

		if (b == 0) {
			if (r != y) {
				cout << "IMPOSSIBLE" << endl;
				continue;
			}
			for (int i = 0; i < n; i += 2) {
				printr(g);
				printy(v);
			}
			cout << endl;
			continue;
		}

		if (y >= r && y >= b) {
			int p = b + r - y;
			for (int i = 0; i < p; ++i) {
				printy(v);
				printb(o);
				printr(g);
			}
			for (int i = 0; i < b - p; ++i) {
				printy(v);
				printb(o);
			}
			for (int i = 0; i < r - p; ++i) {
				printy(v);
				printr(g);
			}
			cout << endl;
			continue;
		}

		if (b >= r && b >= y) {
			int p = r + y - b;
			for (int i = 0; i < p; ++i) {
				printb(o);
				printr(g);
				printy(v);
			}
			for (int i = 0; i < r - p; ++i) {
				printb(o);
				printr(g);
			}
			for (int i = 0; i < y - p; ++i) {
				printb(o);
				printy(v);
			}
			cout << endl;
			continue;
		}

		if (r >= y && r >= b) {
			int p = y + b - r;
			for (int i = 0; i < p; ++i) {
				printr(g);
				printy(v);
				printb(o);
			}
			for (int i = 0; i < y - p; ++i) {
				printr(g);
				printy(v);
			}
			for (int i = 0; i < b - p; ++i) {
				printr(g);
				printb(o);
			}
			cout << endl;
			continue;
		}
	}
}
