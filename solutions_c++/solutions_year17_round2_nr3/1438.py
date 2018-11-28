//If you are trying to hack me I wish you can get it, Good Luck :D
#include <bits/stdc++.h>
using namespace std;

#define debug(args...) fprintf (stderr,args)
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef long double ld;

const int MAX = 112;
const int INF = 0x3f3f3f3f;
const ll  MOD = 1000000007;

int n, q;
ld d[MAX];
ld s[MAX];
ld e[MAX];

ld solve (int i) {
    if (i == n) return 0;
    ld ret = 1e18;
    ld sum = d[i];
    for (int j = i + 1; sum <= e[i] && j <= n; j++) {
	ret = min(ret, solve(j) + (sum) / s[i]);
	sum += d[j];
    }
    return ret;
}

int main () {
    int T;
    scanf ("%d", &T);
    for (int t = 1; t <= T; t++) {
	for (int i = 0; i < MAX; i++)
	    d[i] = 1e18;
	scanf ("%d %d", &n, &q);
	for (int i = 1; i <= n; i++) {
	    scanf ("%LF %LF", e + i, s + i);
	}
	
	for (int i = 1; i <= n; i++) {
	    for (int j = 0; j < n; j++) {
		ld a;
		scanf ("%LF", &a);
		if (a != -1) d[i] = a;
	    }
	}
	
	for (int i = 0; i < q; i++) {
	    int a, b;
	    scanf ("%d %d", &a, &b);
	}
	
	printf ("Case #%d: %LF\n", t, solve(1)); 
    }
}

