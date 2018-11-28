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
using namespace std;
#define MP make_pair
#define PB push_back
#define mst(a,b) memset((a),(b),sizeof(a))
typedef long long LL;
typedef unsigned long long uLL;
typedef pair<int, int> Pii;
typedef vector<int> Vi;
typedef vector<Pii> Vii;
const int inf = 0x3f3f3f3f;
const LL INF = (1uLL << 63) - 1;
const LL mod = 1000000007;
const int N = 1e5 + 7;
const double Pi = acos(-1.0);
const int maxn = 1e4 + 5;
const uLL Hashmod = 29050993;
char s[maxn];
int pre[maxn];
int main() {
#ifdef local
    freopen("A-large.in", "r", stdin);
    freopen("w","w",stdout);
#endif
   // ios::sync_with_stdio(0);
   // cin.tie();
    int T;
    cin >> T;
    for(int cas = 1; cas <= T; ++cas) {
        printf("Case #%d: ",cas);
        mst(pre, 0);
        int n, k;
        scanf("%s%d",s+1,&k);
        n = strlen(s + 1);
        int now = 0;
        int ans = 0;
        bool flag = 0;
        for(int i = 1; i <= n; i++) {
            now += pre[i];
            if(((now & 1) && s[i] == '+' ) || (!(now & 1) && s[i] == '-')) {
                ans++;
                if(i + k > n + 1) {
                    flag = 1;
                    break;
                }
                now++;
                pre[i + k]--;
            }
        }
        if(flag)printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }
}
