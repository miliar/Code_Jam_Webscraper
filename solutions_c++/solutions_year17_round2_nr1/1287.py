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
#include <assert.h>
#include <bitset>
#include <algorithm>
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
const int maxn = 1e5 + 5;
const int N = 2e4 + 5;
const ULL hashmod = 2908361;
const double eps = 1e-8;
int d,n;
struct node{
    int x,s;
};
node h[1005];
double judge(){
    double ans = 0;
    for(int i = 0; i < n; i++){
        ans = max(ans, (double)(d - h[i].x)/h[i].s );
    }
    return ans;
}
int main() {
#ifdef local
    freopen("A-large.in", "r", stdin);
//    freopen("w","w",stdout);
#endif
   // ios::sync_with_stdio(false);
  //  cin.tie(0);
    int T;
    cin>>T;
    for(int cas = 1; cas <= T; cas++){
        printf("Case #%d: ",cas);
        scanf("%d%d",&d,&n);
        cout<<d<<" "<<n<<" ";
        for(int i = 0; i < n; i++){
            int x,s;
            scanf("%d%d",&x,&s);
            h[i].x = x,h[i].s = s;
        }
        printf("%.10f\n",d/judge());
    }
}
