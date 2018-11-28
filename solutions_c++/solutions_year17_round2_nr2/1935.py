#include <iostream>
#include <string>

using namespace std;

bool check1B(int r, int y, int b) {
	if (r >= y&&r >= b && r > y + b) return false;
	if (y >= r&&y >= b && y > r + b) return false;
	if (b >= y&&b >= r && b > y + r) return false;
	return true;
}
int main()
{
	int t, ct;
	freopen("a.in", "r", stdin);
	cin >> ct;
	for (t = 1; t <= ct; t++)
	{
		cout << "Case #" << t << ": ";
		int n, r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;
		if (check1B(r,y,b) == false) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		else if (r >= y&&r >= b) {
			int temp = y + b - r + 1;
			int flag = 1;
			for (int i = 0; i < temp; i++) {
				if (flag &&y) {
					cout << "Y";
					flag = 0;
					y--;
				}
				else if (b) {
					cout << "B";
					flag = 1;
					b--;
				}
				
				
			}
			for (int i = 0; i < y; i++) {
				cout << "RY";
			}
			for (int i = 0; i < b; i++) {
				cout << "RB";
			}
			cout << "R";
			cout << endl;
		}else if (y >= r&&y >= b) {
			int temp = r + b - y + 1;
			int flag = 1;
			for (int i = 0; i < temp; i++) {
				if (flag &&r) {
					cout << "R";
					flag = 0;
					r--;
				}
				else if (b) {
					cout << "B";
					flag = 1;
					b--;
				}


			}
			for (int i = 0; i < r; i++) {
				cout << "YR";
			}
			for (int i = 0; i < b; i++) {
				cout << "YB";
			}
			cout << "Y";
			cout << endl;
		}else if (b >= y&&b >= r) {
			int temp = y + r - b + 1;
			int flag = 1;
			for (int i = 0; i < temp; i++) {
				if (flag &&y) {
					cout << "Y";
					flag = 0;
					y--;
				}
				else if (r) {
					cout << "R";
					flag = 1;
					r--;
				}


			}
			for (int i = 0; i < y; i++) {
				cout << "BY";
			}
			for (int i = 0; i < r; i++) {
				cout << "BR";
			}
			cout << "B";
			cout << endl;
		}
	}


	return 0;
}

