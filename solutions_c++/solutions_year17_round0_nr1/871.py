#include <bits/stdc++.h>

#define maxn 200100
#define sq 333
#define logn 23
#define inf 0x3F3F3F3F
#define linf 0x3F3F3F3F3F3F3F3FLL
#define eps 1e-9
#define pb push_back
#define mp make_pair
#define mod 1000000007LL

using namespace std;

typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;
typedef priority_queue<pii, vii, greater<pii> > pq;

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

int t, n, k;
char s[1010];

int main() {
	scanf("%d", &t);
	for(int cas = 1; cas <= t; ++cas) {
		int cnt = 0;
		scanf("%s %d", s, &k);
		n = strlen(s);
		for(int i = 0; i <= n - k; ++i) {
			if(s[i] == '-') {
				for(int j = i; j < i+k; ++j) {
					s[j] = (s[j] == '+')?'-':'+';
				}
				cnt++;
			}
		}
		bool ok = true;
		for(int i = 0; i < n; ++i) {
			if(s[i] == '-') ok = false;
		}
		if(ok)
			printf("Case #%d: %d\n", cas, cnt);
		else
			printf("Case #%d: IMPOSSIBLE\n", cas);
	}

	return 0;
}