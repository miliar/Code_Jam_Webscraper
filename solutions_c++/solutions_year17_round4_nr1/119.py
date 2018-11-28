#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for(int i=(a);i<(b);i++)
#define MOD 1000000007
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef long double ld;
#define PI ((ld)acos(-1.))
#define asdf(x...) fprintf(stderr, x)

int T, dp[101][101][101][101];
int N, P, a[110], n[5];

void u (int &i, int j) {
	if (j>i) i = j;
}

int main () {
	scanf("%d", &T);
	fo(t, 1, T+1) {
		//REMEMBER CLEAR DS
		fo(i, 0, 5) n[i] = 0;
		//REMEMBER CLEAR DS
		asdf("Doing case %d... ", t);

		scanf("%d %d", &N, &P);
		fo(i, 0, N) {
			scanf("%d", &a[i]);
			a[i] %= P;
			n[a[i]]++;
		}
		int ans = 0;
		vector<int> v;

		if (P == 2) {
			while (n[0]) v.PB(0), n[0]--;
			while (n[1]) v.PB(1), n[1]--;
		} else if (P == 3) {
			while (n[0]) v.PB(0), n[0]--;
			while (n[1] && n[2]) {
				v.PB(1), v.PB(2);
				n[1]--, n[2]--;
			}

			while (n[1]) v.PB(1), n[1]--;
			while (n[2]) v.PB(2), n[2]--;
		} else if (P == 4) {
			while (n[0]) v.PB(0), n[0]--;
			while (n[1] && n[3]) {
				v.PB(1), v.PB(3);
				n[1]--, n[3]--;
			}

			while (n[2]) v.PB(2), n[2]--;
			while (n[1]) v.PB(1), n[1]--;
			while (n[3]) v.PB(3), n[3]--;
		}

		int sum = 0;
		for (int i : v) {
			if (sum % P == 0) ans++;
			sum += i;
		}

		printf("Case #%d: %d\n", t, ans);
		asdf("%d\n", ans);
	}
	return 0;
}
