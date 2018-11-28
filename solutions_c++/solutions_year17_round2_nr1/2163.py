#include <bits/stdc++.h>
#define ll long long
#define mst(a,x) memset(a,x,sizeof(a))
#define For(i, t) for(int i = 0; i < t; i++)
#define Debug(x) cerr << #x << " = "  << x << endl;
using namespace std;


int main() {
    int T;

    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    For(cas, T) {
        int d, n;
        scanf("%d%d", &d, &n);
        double ans = -1;
        For(i, n) {
            int k, s;
            scanf("%d%d", &k, &s);
            double val = k * 1.0 * s / (d - k) + s;
            //Debug(val);
            if(ans < 0) ans = val;
            else ans = min(ans, val);
        }
        printf("Case #%d: %.15f\n", cas + 1, ans);
    }
	return 0;
}
