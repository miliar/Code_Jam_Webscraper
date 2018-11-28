#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define PI acos(-1)
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;
const int M = 1005;
long double k[M], s[M], d;
int n;
bool check(long double v) {
        for(int i = 0; i < n; i++) {
                long double t1 = d / v;
                long double t2 = (d - k[i]) / s[i];
                if(t1 < t2) {
                        return 0;
                }
        }
        return 1;
}
int main()
{
        freopen("A-large.in", "r", stdin);
        freopen("out.txt", "w", stdout);
        int t, c = 0;
        scanf("%d", &t);
        while(t--) {
                c++;
                printf("Case #%d: ", c);
                cin >> d >> n;
                for(int i = 0; i < n; i++) {
                        cin >> k[i] >> s[i];
                }
                double L = 0, R = 1e18, m;
                int it = 10000;
                while(it--) {
                        m = (L + R) / 2.0;
                        if(!check(m)) {
                                R = m;
                        } else {
                                L = m;
                        }
                }
                printf("%lf\n", m);
        }
        return 0;
}
