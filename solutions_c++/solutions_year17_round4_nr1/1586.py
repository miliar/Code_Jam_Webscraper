#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<fstream>
using namespace std;
int n[1000];
int v[5];
int main() {
	ofstream out("answer.txt");
	int T, kase;
	cin >> T;
	int N, P;
	int i, j, k, x, y;
	int ans;
	for (kase = 1; kase <= T; kase++) {
		out << "Case #" << kase << ": ";
		memset(v, 0, sizeof(v));
		ans = 0;
		cin >> N >> P;
		for (i = 0; i < N; i++) {
			cin >> n[i];
			v[n[i] % P]++;
		}

		if (P == 2) {
			ans = v[0] + (v[1] + 1) / 2;
		} else if (P == 3) {
			x = min(v[1], v[2]);
			v[1] -= x;
			v[2] -= x;
			ans = v[0] + x;
			if (v[1])
				ans += ((v[1] - 1) / 3 + 1);
			if (v[2])
				ans += ((v[2] - 1) / 3 + 1);
		}
		out << ans << endl;
	}
	out.close();
	return 0;
}
