#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <string.h>
#include <stack>
#include <list>

#define IMAX 1234567890

using namespace std;

int main(int argc, const char * argv[]) {

	int test;
	pair<int, int> horse[1001];
	cin >> test;

	for (int z = 1; z <= test; z++) {

		string s = "";
		int n;
		cin >> n;
		int r, o, y, g, b, v;
		cin >> r >> o >> y >> g >> b >> v;
		

		if (g == 0 && r == 0 && v == 0 && y == 0 && o == b) {
			for (int i = 0; i < o; i++) s += "BO";
			printf("Case #%d: ", z);
			cout << s << endl;
		}
		else if (g == r && v == 0 && y == 0 && o == 0 && b == 0) {
			for (int i = 0; i < r; i++) s += "RG";
			printf("Case #%d: ", z);
			cout << s << endl;
		}
		else if (g == 0 && r == 0 && v == y && o == 0 && b == 0) {
			for (int i = 0; i < v; i++) s += "YV";
			printf("Case #%d: ", z);
			cout << s << endl;
		}
		else {
			string bo = "B";
			string rg = "R";
			string yv = "Y";

			if (o != 0) {
				if (o >= b) {
					printf("Case #%d: IMPOSSIBLE\n", z);
					continue;
				}
				else {
					for (int i = 0; i < o; i++) bo += "OB";
				}
				b -= o;
			}

			if (g != 0) {
				if (g >= r) {
					printf("Case #%d: IMPOSSIBLE\n", z);
					continue;
				}
				else {
					for (int i = 0; i < g; i++) rg += "GR";
				}
				r -= g;
			}

			if (v != 0) {
				if (v >= y) {
					printf("Case #%d: IMPOSSIBLE\n", z);
					continue;
				}
				else {
					for (int i = 0; i < v; i++) yv += "VY";
				}
				y -= v;
			}

			if ((b + r < y) || (r + y < b) || (y + b < r)) {
				printf("Case #%d: IMPOSSIBLE\n", z);
				continue;
			}

			if (r <= b && b <= y) {
				for (int i = 0; i < r - y + b; i++) s += "YBR";
				for (int i = 0; i < y - r; i++) s += "YB";
				for (int i = 0; i < y - b; i++) s += "YR";
			}
			else if (b <= r && r <= y) {
				//b -> r and r -> b
				for (int i = 0; i < b - y + r; i++) s += "YRB";
				for (int i = 0; i < y - b; i++) s += "YR";
				for (int i = 0; i < y - r; i++) s += "YB";
			}
			else if (r <= y && y <= b) {
			    //b -> y and y -> b
				for (int i = 0; i < r - b + y; i++) s += "BYR";
				for (int i = 0; i < b - r; i++) s += "BY";
				for (int i = 0; i < b - y; i++) s += "BR";
			}
			else if (y <= r && r <= b) {
				//y -> r and r -> y
				for (int i = 0; i < y - b + r; i++) s += "BRY";
				for (int i = 0; i < b - y; i++) s += "BR";
				for (int i = 0; i < b - r; i++) s += "BY";
			}
			else if (b <= y && y <= r) {
				//r -> b and b -> r
				for (int i = 0; i < b - r + y; i++) s += "RYB";
				for (int i = 0; i < r - b; i++) s += "RY";
				for (int i = 0; i < r - y; i++) s += "RB";
			}
			else if (y <= b && b <= r) {
				for (int i = 0; i < b - r + y; i++) s += "RBY";
				for (int i = 0; i < r - y; i++) s += "RB";
				for (int i = 0; i < r - b; i++) s += "RY";
			}

			if (o != 0) {
				int i = 0;
				for (i = 0; i < s.size(); i++) {
					if (s[i] == 'B') break;
				}
				s = s.substr(0, i) + bo + s.substr(i + 1, s.size() - (i + 1));
			}

			if (g != 0) {
				int i = 0;
				for (i = 0; i < s.size(); i++) {
					if (s[i] == 'R') break;
				}
				s = s.substr(0, i) + rg + s.substr(i + 1, s.size() - (i + 1));
			}

			if (v != 0) {
				int i = 0;
				for (i = 0; i < s.size(); i++) {
					if (s[i] == 'Y') break;
				}
				s = s.substr(0, i) + yv + s.substr(i + 1, s.size() - (i + 1));
			}

			printf("Case #%d: ", z);
			cout << s << endl;
		}
	}
	return 0;
}