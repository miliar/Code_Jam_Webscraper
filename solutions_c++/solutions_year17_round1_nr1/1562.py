#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

#define uchar unsigned char
#define ushort unsigned short
#define uint unsigned int
#define ull unsigned ll
#define ll long long
#define ull unsigned ll

#define E 2.718281828
#define PI 3.14159265358979323846264338328

using namespace std;

int r, c;
char grid[25][26];
char res[25][26];
bool flag[25];

void print() {
	cout << endl;
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++)
			cout << res[i][j];
		cout << endl;
	}
}

void solve() {
	cin >> r >> c;
	for (int i = 0; i < r; i++)
		cin >> grid[i];
	for (int i = 0; i < r; i++)
		flag[i] = false;
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++) {
			res[i][j] = grid[i][j];
			if (res[i][j] != '?')
				flag[i] = true;
		}
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
			if (res[i][j] == '?') {
				int tr = i;
				while (tr >= 0 && !flag[tr])
					tr--;
				if (tr < 0) {
					tr = i;
					while (!flag[tr])
						tr++;
				}
				int tc = j;
				while (tc >= 0 && grid[tr][tc] == '?')
					tc--;
				if (tc < 0) {
					tc = j;
					while (grid[tr][tc] == '?')
						tc++;
				}
				res[i][j] = grid[tr][tc];
			}
	print();
}

int main() {
	int t, i;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
