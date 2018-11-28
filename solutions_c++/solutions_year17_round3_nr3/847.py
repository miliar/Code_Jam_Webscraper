#include <iostream>
//#include <conio.h>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <stdlib.h>
#include <ctime>
#define _USE_MATH_DEFINES
#include <cmath>
#include <math.h>
#include <string>
#include <stack>
#include <queue>
#include <bitset>
//#include <sstream>
//#include <iomanip>
using namespace std;
typedef long long ll;
const ll mod = 1000000007;
const int inf = 1000000006;
const ll INF = 1000000000000000000;
#define y1 jghrdtslgblrsdjg
#define y0 shgeupisrhgasdfg
#define j1 hufvhvuifgragresgse

double a[100];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n;
		double p;
		cin >> n >> n >> p;
		for (int i = 0; i < n; i++)
			cin >> a[i];
		a[n] = 2;
		sort(a, a + n + 1);
		double res = 0;
		for (int i = 1; i < n + 1; i++) {
			if (a[i] != a[i - 1]) {
				double x = (a[i] - a[i - 1]) * i;
				if (x <= p) {
					p -= x;
				} else {
					double k = (a[i - 1] + p / i);
					res = 1;
					for (int j = 0; j < i; j++)
						res *= k;
					for (int j = i; j < n; j++)
						res *= a[j];
					break;
				}
			}
		}
		cout.precision(10);
		cout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}