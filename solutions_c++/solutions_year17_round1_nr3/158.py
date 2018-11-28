#include <bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#ifdef _DEBUG_
	#define debug(...) printf(__VA_ARGS__)
#else
	#define debug(...) (void)0
#endif
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;

const ll MAX = 100;
const ll INF = 1e9;


ll Hd, Ad, Hk, Ak, B, D;

ll simulate(int buf, int debuf) {
	ll Hd = ::Hd;
	ll Ad = ::Ad;
	ll Hk = ::Hk;
	ll Ak = ::Ak;
	ll B = ::B;
	ll D = ::D;
	ll cnt = 1;
	for(int i = 0; i < debuf; i++) {

		Ak = max(0ll, Ak - D);
		Hd -= Ak;
		cnt++;
		if(Hd <= 0) {
			if(Hd == ::Hd - Ak) return INF;
			Hd = ::Hd - (Ak + D) - Ak;
			if(Hd <= 0) return INF;
			cnt++;
		}
	}
	for(int i = 0; i < buf; i++) {
		if(Hd - Ak <= 0) {
			cnt++;
			Hd = ::Hd - Ak;
		}
		if(Hd - Ak <= 0) return INF;
		Ad += B;
		Hd -= Ak;
		cnt++;
	}
	while(Hk > 0) {
		if(Hk - Ad <= 0) {
			break;
		}
		if(Hd - Ak <= 0) {
			cnt++;
			Hd = ::Hd - Ak;
		}
		if(Hd - Ak <= 0) return INF;
		Hk -= Ad;
		Hd -= Ak;
		cnt++;
		if(buf == 0 && debuf == 0) debug("%lld~ %lld %lld\n", cnt, Hd, Hk);
	}
	if(cnt == 7) debug("(%d, %d)\n", buf, debuf);
	return cnt;
}

int main() {
	int all_kase;
	scanf("%d", &all_kase);
	for(int num_kase = 1; num_kase <= all_kase; num_kase++) {
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
		ll ans = INF;
		for(int buf = 0; buf <= MAX; buf++)
			for(int debuf = 0; debuf <= MAX; debuf++) {
				ans = min(ans, simulate(buf, debuf));
			}
		if(ans >= INF)
			printf("Case #%d: IMPOSSIBLE\n", num_kase);
		else
			printf("Case #%d: %lld\n", num_kase, ans);
	}
	return 0;
}
