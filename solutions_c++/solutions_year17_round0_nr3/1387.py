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

int main() {
	int t;
	scanf("%d", &t);
	for(int kase=1; kase<=t; kase++) {
		printf("Case #%d: ", kase);
		ll k, n;
		scanf("%lld%lld", &n, &k);
		k--;
		ll cp=0;
		while(true) {
			ll tmp = (cp<<1)|1;
			if(tmp <= k)
				cp = tmp;
			else
				break;
		}
		ll q = (n-cp)/(cp+1), r = (n-cp)%(cp+1);
		ll len = (k-cp < r) ? q+1 : q;
		debug("len = %lld\n", len);

		if(len&1)
			printf("%lld %lld\n", len>>1, len>>1);
		else
			printf("%lld %lld\n", len>>1, (len-1)>>1);
	}
	return 0;
}
