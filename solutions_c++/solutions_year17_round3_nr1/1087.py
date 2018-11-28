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
struct node{
    LL h,r;
    LL x;
    bool operator < (const node &a)const{
        return x > a.x;
    }
};
node ct[maxn];
LL sum[maxn];
int main() {
#ifdef local
    freopen("A-large.in", "r", stdin);
    freopen("w", "w", stdout);
#endif
  //  ios::sync_with_stdio(false);
  //  cin.tie(0);
    int t;
    scanf("%d",&t);
    int cas = 1;
    while(t--){
        printf("Case #%d: ",cas++);
        int n,k;
        scanf("%d%d",&n,&k);
        for(int i = 0; i < n; i++){
            int a,b;
            scanf("%d%d",&a,&b);
            ct[i].h = b,ct[i].r = a;
            ct[i].x = 2LL * a * b;
        }
        sort(ct,ct+n);
        memset(sum,0,sizeof sum);
        for(int i = 1; i <= n; i++){
            sum[i] = sum[i-1] + ct[i - 1].x;
        }
        double ans = 0;
        for(int i = k; i < n; i++){
            ans = max(ans,ct[i].r * ct[i].r * Pi + ct[i].x * Pi + sum[k - 1] * Pi);
        }
        for(int i = 0; i < k; i++){
            ans = max(ans,ct[i].r * ct[i].r * Pi + sum[k] * Pi);
        }
        printf("%.9f\n",ans);
    }
}
