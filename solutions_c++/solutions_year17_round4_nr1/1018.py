#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <stdint.h>
#include <string>
#include <utility>
#include <vector>
#include <iostream>

using namespace std;

void solve(int t) {
	int N, P;
	cin >> N >> P;
	vector<int> ostCnt(P);
	int sum = 0;
	for (int i = 0; i < N; ++i) {
		int k;
		cin >> k;
		ostCnt[k%P]++;
		sum += (k%P);
	}
	int toadd = 0;
	if ((sum % P) != 0)
		toadd++;
	int res = ostCnt[0];
	if (P == 2) {
		res += ostCnt[1] / 2;
	}
	else if (P == 3) {
		int mini = min(ostCnt[1], ostCnt[2]);
		res += mini;
		ostCnt[1] -= mini;
		ostCnt[2] -= mini;
		res += max(ostCnt[1], ostCnt[2]) / 3;
	}
	else {
		int mini1 = min(ostCnt[1], ostCnt[3]);
		res += mini1;
		ostCnt[1] -= mini1;
		ostCnt[3] -= mini1;
		res += ostCnt[2] / 2;
		ostCnt[2] %= 2;
		if (ostCnt[2] && ostCnt[3] >= 2) {
			ostCnt[2]--;
			ostCnt[3] -= 2;
			res++;
		}
		if (ostCnt[2] && ostCnt[1] >= 2) {
			ostCnt[2]--;
			ostCnt[1] -= 2;
			res++;
		}
		res += max(ostCnt[1], ostCnt[3]) / 4;
	}
	printf("Case #%d: %d\n", t, min(res + toadd, N));
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		solve(i + 1);
	}
	return 0;
}
