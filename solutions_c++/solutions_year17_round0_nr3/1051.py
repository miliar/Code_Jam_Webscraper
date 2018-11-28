#include <bits/stdc++.h>
#define ll long long
#define mst(a,x) memset(a,x,sizeof(a))
#define For(i, t) for(int i = 0; i < t; i++)
#define Debug(x) cerr << #x << " = "  << x << endl;
using namespace std;

int main() {
    int T;
    ll n, k;

    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    For(cas, T) {
        scanf("%I64d%I64d", &n, &k);
        ll a = n - 1 - (n - 1) / 2, b = (n - 1) / 2, x = 1, y = 1;
        if(k == 1) {
            printf("Case #%d: %I64d %I64d\n", cas + 1, a, b);
            continue;
        }
        k--;
        for(int deep = 1; k > (1LL << deep); k -= (1LL << deep), deep++) {
            //printf("x%I64d a%I64d y%I64d b%I64d\n", x, a, y, b);
            ll na = a - 1 - (a - 1) / 2;
            ll nb = (b - 1) / 2;
            ll nx, ny;
            if(a == b) {
                nx = x + y;
                ny = x + y;
            }else if(a & 1) {
                nx = x + x + y;
                ny = y;
            }else {
                nx = x;
                ny = x + y + y;
            }
            a = na, b = nb;
            x = nx, y = ny;
        }
        ll ansa, ansb;
        //printf("k %I64d x%I64d a%I64d y%I64d b%I64d\n", k, x, a, y, b);
        if(k <= x) {
            ansa = a - 1 - (a - 1) / 2;
            ansb = (a - 1) / 2;
        }else {
            ansa = b - 1 - (b - 1) / 2;
            ansb = (b - 1) / 2;
        }

        printf("Case #%d: %I64d %I64d\n", cas + 1, ansa, ansb);
    }
	return 0;
}
