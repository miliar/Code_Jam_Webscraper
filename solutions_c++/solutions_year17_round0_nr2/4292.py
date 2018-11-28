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

vector<unsigned long long> v;

void go(int k, unsigned long long x) {
	v.PB(x);

	if(k==18)	return ;
	int now = x%10;
	for(int i=now; i<=9; i++)
		go(k+1, x*10+i);
}

int main() {
	for(int i=1; i<=9; i++)
		go(0, i);
	sort(ALL(v));

	int T;
	scanf("%d", &T);
	for(int kase=1; kase<=T; kase++) {
		ll x;
		scanf("%lld", &x);

		printf("Case #%d: ", kase);
		printf("%lld\n", *--upper_bound(ALL(v), x));
	}
    
    return 0;
}
