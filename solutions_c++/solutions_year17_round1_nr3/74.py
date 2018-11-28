#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <functional>

using namespace std;
#define lli long long int
const int N = 101;
const int INF = N * N * N;
double M = 1e7;

int d[N][N][N][N];

int initial, debuff, buff;

int solve(int hd, int ad, int hk, int ak) {
	if (hd <= 0) return INF;
	ad = max(0, ad); ad = min(100, ad);
	ak = max(0, ak); ak = min(100, ak);
	if (ad >= hk) return 1;
	if (d[hd][ad][hk][ak] == -1) {
		d[hd][ad][hk][ak] = INF;
		d[hd][ad][hk][ak] = min(d[hd][ad][hk][ak], 1 + solve(hd - ak, ad, hk - ad, ak));
		d[hd][ad][hk][ak] = min(d[hd][ad][hk][ak], 1 + solve(hd - ak, ad + buff, hk, ak));
		d[hd][ad][hk][ak] = min(d[hd][ad][hk][ak], 1 + solve(hd - max(0, ak - debuff), ad, hk, ak - debuff));
		d[hd][ad][hk][ak] = min(d[hd][ad][hk][ak], 1 + solve(initial - ak, ad, hk, ak));

		//cout << hd << " " << ad << " " << hk << " " << ak << " " << d[hd][ad][hk][ak] << endl;
	}
	return d[hd][ad][hk][ak];
}

int main() {
	ios_base::sync_with_stdio();
#ifdef FILE_IO
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << (qq + 1) << ": ";

		memset(d, -1, N*N*N*N*sizeof(int));
		int ad, ak, hk;
		cin >> initial >> ad >> hk >> ak >> buff >> debuff;
		int res = solve(initial, ad, hk, ak);
		if (res < INF) cout << res;
		else cout << "IMPOSSIBLE";

		cout << endl;
	}
	return 0;
}
