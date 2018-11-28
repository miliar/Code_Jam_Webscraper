#define _CRT_SECURE_NO_WARNINGS
#include <cassert>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
using namespace std;

#define MEMSET(x, WITH) memset(x, (WITH), sizeof(x))
#define FOR(i, E) for (int i=0; i<(E); i++)
typedef long long ll;
//const ll MOD = 1000000007;
//const double PI = atan(1) * 4;



int N, P;
int G[10];


int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int TC; scanf("%d", &TC);
	for (int tc=1; tc<=TC; tc++) {
		printf("Case #%d: ", tc);
		MEMSET(G, 0);

		cin >> N >> P;
		FOR(i, N) {
			int g; cin >> g;
			G[g%P] += 1;
		}


		if (P == 2) {
			int ans = G[0] + (G[1] + 1) / 2;
			cout << ans << endl;
		}
		else if (P == 3) {
			int a = min(G[1], G[2]);
			int b = max(G[1], G[2]) - a;

			int ans = G[0] + a + (b + 2) / 3;
			cout << ans << endl;
		}





	}

	



	return 0;
}
