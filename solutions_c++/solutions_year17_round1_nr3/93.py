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

int T, HD, AD, HK, AK, B, D;

struct state {
	int myh, mya, hish, hisa, c;
	int hash () {
		return myh + mya * 101 + hish * 101 * 101 + hisa * 101 * 101 * 101;
	}
};
bool s[110110110];

int main () {
	scanf("%d", &T);
	fo(t, 1, T+1) {
		//REMEMBER CLEAR DS
		//REMEMBER CLEAR DS
		asdf("Doing case %d... ", t);

		int ans = 2e9;
		scanf("%d %d %d %d %d %d", &HD, &AD, &HK, &AK, &B, &D);

		memset(s, 0, sizeof(s));
		queue<state> q;

		q.push((state) {HD, AD, HK, AK, 0});
		while (q.size()) {
			state a = q.front(), b; q.pop();
			s[a.hash()] = true;

			//asdf("%d %d %d %d\n", a.myh, a.mya, a.hish, a.hisa);

			//attack, get hit
			b = a, b.c++;
			b.hish -= b.mya;
			if (b.hish <= 0) {
				ans = min(ans, a.c + 1);
				break;
			} else {
				b.myh -= b.hisa;
				if (b.myh > 0 && !s[b.hash()]) {
					s[b.hash()] = true;
					q.push(b);
				}
			}

			//buff, get hit
			b = a, b.c++;
			b.mya += B;
			b.mya = min(b.mya, b.hish);
			b.myh -= b.hisa;
			if (b.myh > 0 && !s[b.hash()]) {
				s[b.hash()] = true;
				q.push(b);
			}

			if (b.hisa >= 0) {
				//debuff, get hit
				b = a, b.c++;
				b.hisa -= D;
				b.hisa = max(b.hisa, 0);
				b.myh -= b.hisa;
				if (b.myh > 0 && !s[b.hash()]) {
					s[b.hash()] = true;
					q.push(b);
				}
			}

			//cure, get hit
			b = a, b.c++;
			b.myh = HD;
			b.myh -= b.hisa;
			if (b.myh > 0 && !s[b.hash()]) {
				s[b.hash()] = true;
				q.push(b);
			}
		}

		printf("Case #%d: ", t);
		if (ans == 2e9) {
			printf("IMPOSSIBLE\n");
			asdf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", ans);
			asdf("%d\n", ans);
		}
	}
	return 0;
}
