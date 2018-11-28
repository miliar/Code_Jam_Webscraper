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

int n, p;
int cnt[4];

void solve() {
	cin >> n >> p;
	for (int i = 0; i < 4; i++)
		cnt[i] = 0;
	while (n--) {
		int g;
		cin >> g;
		cnt[g % p]++;
	}
	int res = cnt[0];
	if (p == 2)
		res += (cnt[1] + 1) / 2;
	else if (p == 3) {
		int tmp = min(cnt[1], cnt[2]);
		cnt[1] -= tmp;
		cnt[2] -= tmp;
		res += tmp;
		tmp = max(cnt[1], cnt[2]);
		int tmp2 = tmp / 3;
		res += tmp2;
		tmp -= 3 * tmp2;
		if (tmp)
			res++;
	} else {
		int tmp = min(cnt[1], cnt[3]);
		cnt[1] -= tmp;
		cnt[3] -= tmp;
		res += tmp;
		tmp = cnt[2] / 2;
		cnt[2] -= 2 * tmp;
		res += tmp;
		if (cnt[2] == 0) {
			tmp = max(cnt[1], cnt[3]);
			int tmp2 = tmp / 4;
			res += tmp2;
			tmp -= 4 * tmp2;
			if (tmp)
				res++;
		}
		else {
			tmp = max(cnt[1], cnt[3]);
			if (tmp >= 2) {
				tmp -= 2;
				res++;
				int tmp2 = tmp / 4;
				res += tmp2;
				tmp -= 4 * tmp2;
				if (tmp)
					res++;
			} else
				res++;
		}
	}
	cout << res << endl;
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
