#include <iostream>
#include <cstdio>
using namespace std;

int N, R, O, Y, G, B, V;

void output(char c, int& count) {
	cout << c;

	if (count == 0) {
		char c1, num1;

		if (c == 'R') {
			c1 = 'G';
			num1 = G;
		}
		else if (c == 'Y') {
			c1 = 'V';
			num1 = V;
		}
		else {
			c1 = 'O';
			num1 = O;
		}
		
		for (int i = 0; i < num1; i++) {
			cout << c1 << c;
		}
	}

	count++;
}

bool check1() {
	if (R > 0 && R == G) {
		if (Y || V || B || O) {
			cout << "IMPOSSIBLE" << endl;
		}
		else {
			for (int i = 0; i < R; i++) {
				cout << "RG";
			}

			cout << endl;
		}

		return true;
	}

	if (Y > 0 && Y == V) {
		if (R || G || B || O) {
			cout << "IMPOSSIBLE" << endl;			
		}
		else {
			for (int i = 0; i < Y; i++) {
				cout << "YV";
			}

			cout << endl;
		}

		return true;
	}

	if (B > 0 && B == O) {
		if (R || G || Y || V) {
			cout << "IMPOSSIBLE" << endl;
		}
		else {
			for (int i = 0; i < B; i++) {
				cout << "BO";
			}

			cout << endl;
		}

		return true;
	}

	return false;
}

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("b-small.out", "w", stdout);

	int nCases;
	cin >> nCases;

	for (int cnt = 1; cnt <= nCases; cnt++) {		
		cin >> N >> R >> O >> Y >> G >> B >> V;

		cout << "Case #" << cnt << ": ";

		int r = R, o = O, y = Y, g = G, b = B, v = V;
		r -= g;
		y -= v;
		b -= o;
		int n = r + y + b;

		if (r < 0 || y < 0 || b < 0) {
			cout << "IMPOSSIBLE" << endl;
		} else if (r + r > n || y + y > n || b + b > n) {
			cout << "IMPOSSIBLE" << endl;
		}
		else if (check1()) {
			
		} else {
			char a1, a2, a3;
			int num1, num2, num3;

			if (r >= y && r >= b) {
				a1 = 'R'; num1 = r;
				a2 = 'Y'; num2 = y;
				a3 = 'B'; num3 = b;
			}
			else if (y >= r && y >= b) {
				a1 = 'Y'; num1 = y;
				a2 = 'R'; num2 = r;
				a3 = 'B'; num3 = b;
			}
			else {
				a1 = 'B'; num1 = b;
				a2 = 'R'; num2 = r;
				a3 = 'Y'; num3 = y;
			}

			int mod = n - num1 - num1;
			int curr1 = 0, curr2 = 0, curr3 = 0;

			for (int i = 0; i < num1; i++) {
				if (i < mod) {
					output(a1, curr1);
					output(a2, curr2);
					output(a3, curr3);					
				}
				else {
					output(a1, curr1);

					if (curr2 < num2) {
						output(a2, curr2);
					}
					else {
						output(a3, curr3);
					}
				}
			}

			cout << endl;
		}
	}

	return 0;
}