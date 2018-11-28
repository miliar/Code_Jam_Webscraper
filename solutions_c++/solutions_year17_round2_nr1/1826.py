#include <bits/stdc++.h>

#define rep(i, j, k) for(int i = (int) j; i < (int) k; ++i)
#define sz(x) ((int) (x).size())
#define ll long long
#define mp make_pair
#define pii pair<int, int >
#define fi first
#define se second
#define pb push_back
#define inf 0x3f3f3f3f
#define INF 0x3f3f3f3f3f3f3f
#define zero(x) memset((x), (0), sizeof (x))
#define zerox(x, y) memset((x), (y), sizeof (x))

using namespace std;
const int N = 1010;

int n, d;
pii p[N];



int main()
{
//#ifdef PIT
freopen("A-large.in", "r", stdin);
freopen("A-large.out", "w", stdout);
//#endif // PIT

    int T, ic = 1;
    for(scanf("%d", &T); T--; ic++){
    	printf("Case #%d: ", ic);
    	scanf("%d %d", &d, &n);

    	for(int i = 0; i < n; ++i) {
    		int k, s;
    		scanf("%d %d", &k, &s);
    		p[i] = {k, s};
    	}   
    	sort(p, p+n);
    	double tmx = 0;
    	for(int i = n-1; i >= 0; --i) {
    		double t = 1.* (d-p[i].fi) / p[i].se;
    		if(t > tmx) tmx = t;
    	}
    	printf("%.10f\n", d*1./tmx);
    }
    return 0;
}
