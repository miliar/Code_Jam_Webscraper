#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <cmath>

using namespace std;

int r, o, y, g, b, v, n;
int c[7];
char ch[7] = {'R', 'O', 'Y', 'G', 'B', 'V'};

void fun() {
	int half = n / 2;
	for (int i = 0; i < 6; i ++ ) {
		if (c[i] > half) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	int counter = 0;
	string res(n, ' ');
	int max_index = -1;
	int max_num = -1;
	for (int i = 0; i < 6; i ++ ) {
		if (c[i] > max_num) {
			max_num = c[i];
			max_index = i;
		}
	}
	for (int i = 0; i < c[max_index]; i ++ ) {
		res[counter] = ch[max_index];
		counter += 2;
		if (counter >= n) {
			counter = 1;
		}
	}
	for (int i = 0; i < 6; i ++ ) {
		if (i != max_index) {
			for (int j = 0; j < c[i]; j ++ ) {
				res[counter] = ch[i];
				counter += 2;
				if (counter >= n) {
					counter = 1;
				}
			}			
		}
	}
	cout << res << endl;
}

int main () {
	int t;
	freopen("B-small-attempt3.in", "r", stdin);
	freopen("out", "w", stdout);
	cin >> t;
	for (int i = 0; i < t ; i ++ ) {
		cin >> n;
		for (int j = 0; j < 6; j ++ ) {
			cin >> c[j];
		}
		cout << "Case #" << i + 1 << ": ";
		fun();
	}
	return 0;
}