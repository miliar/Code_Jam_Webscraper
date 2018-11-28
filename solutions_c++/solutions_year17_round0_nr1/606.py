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

int T, N, K;
char s[1100];

int main () {
	scanf("%d", &T);
	fo(t, 1, T+1) {
		//REMEMBER CLEAR DS
		//REMEMBER CLEAR DS
		asdf("Doing case %d... ", t);
		printf("Case #%d: ", t);

		scanf(" %s %d", s, &K);
		N = (int) strlen(s);
		int ans = 0;

		for (int i = 0; i+K <= N; i++) {
			if (s[i] == '-') {
				ans++;
				fo(j, 0, K) s[i+j] = s[i+j] == '+' ? '-' : '+';
			}
		}
		fo(i, 0, N) if (s[i] == '-') ans = -1;

		if (ans != -1) printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
