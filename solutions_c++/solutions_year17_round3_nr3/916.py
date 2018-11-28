#include <cstdio>
#include <cstring>
#include <cmath>
#include <queue>
#include <vector>
#include <time.h>
#include <string>
#include <stack>
#include <set>
#include <map>
#include <iostream>
#include <bitset>
#include <algorithm>
#include <assert.h>
using namespace std;
#define MP make_pair
#define PB push_back
#define mst(a,b) memset((a),(b),sizeof(a))
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> Pii;
typedef vector<int> Vi;
typedef vector<Pii> Vii;
const int inf = 0x3f3f3f3f;
const LL INF = (1uLL << 63) - 1;
const int mod = 1e9 + 7;
const double Pi = acos(-1.0);
const int maxn = 1e3 + 5;
const int N = 2e5 + 5;
const ULL hashmod = 2908361;
const double eps = 1e-8;
double p[maxn];
int n, k;
double m;
double ans;
bool ju(double x){
    double ne = 0;
    for(int i = 0; i < n; i++){
        if(p[i] < x)ne += x - p[i];
    }
    return ne  < m;
}
int main() {
#ifdef local
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("w", "w", stdout);
#endif
    //  ios::sync_with_stdio(false);
    //  cin.tie(0);
    int t;
    scanf("%d", &t);
    int cas = 1;
    while(t--) {
        ans = 1;
        printf("Case #%d: ", cas++);
        scanf("%d%d%lf", &n, &k, &m);
        double l = 0, r = 1;
        for(int i = 0; i < n; i++) {
            scanf("%lf", &p[i]);
            l = min(p[i], l);
        }
        int cnt = 100;
        while(cnt--){
            double mid = (l + r)/2.;
            if(ju(mid))l = mid;
            else r = mid;
        }
        for(int i = 0; i < n; i++){
            if(p[i] < l)ans *= l;
            else ans *= p[i];
        }
        printf("%.9f\n",ans);
    }
}
