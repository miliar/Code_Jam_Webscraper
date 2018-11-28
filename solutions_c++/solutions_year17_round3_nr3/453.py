#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define PI acos(-1)
#define MOD 1000000007
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;
const int M = 55;
int n, k;
double p[M];
int main()
{
        freopen("C-small-1-attempt0.in", "r", stdin);
        freopen("out.txt", "w", stdout);
        int t, c = 0;
        scanf("%d", &t);
        while(t--) {
                c++;
                cin >> n >> k;
                double u;
                cin >> u;
                for(int i = 0; i < n; i++) {
                        cin >> p[i];
                }
                sort(p, p + n);
                for(int i = 0; i < n - 1; i++) {
                        double v = p[i + 1] - p[i];
                        if(v * (i + 1) <= u) {
                                for(int j = 0; j <= i; j++) {
                                        p[j] += v;
                                }
                                u -= v * (i + 1);
                        } else {
                                for(int j = 0; j <= i; j++) {
                                        p[j] += u / (i + 1);
                                }
                                u = 0;
                                break;
                        }
                }
                if(u > 0) {
                        for(int i = 0; i < n; i++) {
                                p[i] += u / n;
                        }
                }
                double ans = 1.0;
                for(int i = 0; i < n; i++) {
                        ans *= p[i];
                }
                printf("Case #%d: %lf\n", c, ans);
        }
        return 0;
}
