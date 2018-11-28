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

const int INF = ((1<<30)-1);

int HD, AD, HK, AK, B, D;
int hd, ad, hk, ak, b, d;

int go(int bs, int ds) {
	int cnt = 0;
	for(int i=0; i<ds; i++, cnt++) {
		if(hd-(ak-d) <= 0) {
			hd = HD-ak;
			cnt++;
		}
		if(hd-(ak-d) <= 0)	return -1;

		ak = max(0, ak-d);
		hd -= ak;
	}
	for(int i=0; i<bs; i++, cnt++) {
		if(hd-ak <= 0) {
			hd = HD-ak;
			cnt++;
		}
		if(hd-ak <= 0)	return -1;
		
		ad += b;
		hd -= ak;
	}

	if(bs == 0 && ds == 0)
		debug("hd=%d, ad=%d, hk=%d, ak=%d|\n", hd, ad, hk, ak);
	while(hk) {
		if(ad >= hk) {
			cnt++;
			break;
		}

		if(hd-ak <= 0) {
			hd = HD-ak;
			cnt++;
		}
		if(hd-ak <= 0)	return -1;

		hk = max(0, hk-ad);
		hd -= ak;
		cnt++;
	}

	return cnt;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int kase=1; kase<=T; kase++) {
		scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);
		HD = hd;
		AD = ad;
		HK = hk;
		AK = ak;

		int ans = INF;
		for(int i=0; i<=100; i++) {
			for(int j=0; j<=100; j++) {
				hd = HD;
				ad = AD;
				hk = HK;
				ak = AK;
				int tmp = go(i, j);
				if(tmp >= 0)	ans = min(ans, tmp);
			}
		}
		
		printf("Case #%d: ", kase);
		if(ans == INF)	puts("IMPOSSIBLE");
		else	printf("%d\n", ans);
	}
    
    return 0;
}
