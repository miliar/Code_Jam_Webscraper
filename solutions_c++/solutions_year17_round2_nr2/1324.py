#include <bits/stdc++.h>
using namespace std;

#define pb push_back

int printred(int &red, int &g) {
	cout << "R";
	if (!red) {
		red = 1;
		for (int i = 0; i < g; i++)
			cout << "GR";
	}
	return 1;
}
int printyellow(int &yellow, int &v) {
	cout << "Y";
	if (!yellow) {
		yellow = 1;
		for (int i = 0; i < v; i++)
			cout << "VY";
	}
	return 1;
}
int printblue(int &blue, int &o) {
	cout << "B";
	if (!blue) {
		blue = 1;
		for (int i = 0; i < o; i++)
			cout << "OB";
	}
	return 1;
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0);

	int num, r, o, y, g, b, v;
	int red, yellow, blue, half;

	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cout << "Case #" << tt << ": ";
		cin >> num >> r >> o >> y >> g >> b >> v;
		half = num/2;
		// special case
		if (r > half || y > half || b > half) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		if (o == half || g == half || v == half) {
			if (num % 2 == 1)
				cout << "IMPOSSIBLE" << endl;
			else {
				if (o == half && b == half) {
					for (int i = 0; i < half; i++) cout << "OB";
					cout << endl;
				}
				else if (g == half && r == half) {
					for (int i = 0; i < half; i++) cout << "GR";
					cout << endl;
				}
				else if (v == half && y == half) {
					for (int i = 0; i < half; i++) cout << "VY";
					cout << endl;
				}
				else {
					cout << "IMPOSSIBLE" << endl;
				}
			}
			continue;
		}
		// general case
		if ((o && b <= o) || (g && r <= g) || (v && y <= v)) {
			cout << "IMPOSSIBLE" << endl;
		}
		else {
			// compress and expand
			r -= g;
			y -= v;
			b -= o;
			// build string with new r,y,b
			red = blue = yellow = 0;
			char prev;
			if (r) {
				r -= printred(red, g); 
				prev = 'R';// start with red
			}
			else if (b) {
				b -= printblue(blue, o); 
				prev = 'B';
			}
			else if (y) {
				y -= printyellow(yellow, v);
				prev = 'Y';
			}
			while (r + y + b > 0) {
				if (prev == 'R') {
					if (b >= y) {
						b -= printblue(blue, o);
						prev = 'B';
					}
					else {
						y -= printyellow(yellow, v);
						prev = 'Y';
					}
				}
				else if (prev == 'B') {
					if (r >= y) {
						r -= printred(red, g);
						prev = 'R';
					}
					else {
						y -= printyellow(yellow, v);
						prev = 'Y';
					}
				}
				else {
					if (r >= b) {
						r -= printred(red, g);
						prev = 'R';
					}
					else {
						b -= printblue(blue, o);
						prev = 'B';
					}
				}
			}
			cout << endl;
		}
	}
	
	return 0;
}
