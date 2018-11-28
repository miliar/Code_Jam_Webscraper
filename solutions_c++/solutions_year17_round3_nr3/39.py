#include <bits/stdc++.h>
#define ll long long
#define mst(a,x) memset(a,x,sizeof(a))
#define For(i, t) for(int i = 0; i < t; i++)
#define Debug(x) cerr << #x << " = "  << x << endl;
using namespace std;


const int N = 55;
double U, p[N];
int T, n, k;

double calc(int k, double x) {
    double ret = 1;
    For(i, n) {
        if(i < k) ret *= x;
        else ret *= p[i];
    }
    return ret;
}

int main() {

    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    For(cas, T) {
        scanf("%d%d", &n, &k);
        scanf("%lf", &U);
        For(i, n) scanf("%lf", p + i);
        sort(p, p + n);
        double ans = 1;
        For(i, n) ans = ans * p[i];
        //printf("pre ans %.5lf\n", ans);
        double sum = 0;
        For(i, n) {
            sum += p[i];
            double cur = min(1.0, (sum + U) / (i + 1));
            if(p[i] > cur) break;
            ans = max(ans, calc(i + 1, cur));
        }
        printf("Case #%d: %.10f\n", cas + 1, ans);
    }
	return 0;
}
