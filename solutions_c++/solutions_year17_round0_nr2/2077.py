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

ll End = 1e17;
vector<ll> vec;

void Go(ll num) {
	vec.PB(num);
	if(num > End) return;
	for(int i = max(num % 10, 1ll); i <= 9; i++)
		Go(10 * num + i);
}

void Init() {
	Go(0);
	sort(ALL(vec));
}

int main() {
	Init();
	int all_kase;
	scanf("%d", &all_kase);
	for(int num_kase = 1; num_kase <= all_kase; num_kase++) {
		ll N;
		scanf("%lld", &N);
		printf("Case #%d: %lld\n", num_kase, upper_bound(ALL(vec), N)[-1]);
	}
	return 0;
}
