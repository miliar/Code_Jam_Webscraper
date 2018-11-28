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

bool a[1500];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int res = 2;
		int ac, aj;
		cin >> ac >> aj;
		for (int i = 0; i < 1500; i++)
			a[i] = false;
		if (!(ac == 2 && aj == 0 || ac == 0 && aj == 2)) {
			res = 2;
			int x;
			for (int i = 0; i < ac + aj; i++)
				cin >> x >> x;
		} else {
			for (int i = 0; i < 2; i++) {
				int s, e;
				cin >> s >> e;
				for (int j = s; j < e; j++)
					a[j] = true;
			}
			int s = 0, ans = 0;
			for (int i = 0; i < 6000; i++) {
				if (a[i % 1440]) {
					s = 0;
				} else {
					s++;
					//if (s == 539)
					//	cout << i << endl;
					ans = max(ans, s);
				}
			}
			//cout << ans << endl;
			if (ans >= 720)
				res = 2;
			else
				res = 4;
		}
		cout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}