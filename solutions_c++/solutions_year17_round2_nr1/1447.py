// #pragma comment(linker,"/STACK:102400000,102400000")
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>

#include <string>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <fstream>
// #include <unordered_set>

using namespace std;

#define FF first
#define SS second
#define MP make_pair
#define PB push_back
#define lson rt << 1, l, mid
#define rson rt << 1 | 1, mid + 1, r
#define FOR(i, n, m) for(int i = n; i <= m; i++)
#define REP(i, n, m) for(int i = n; i >= m; i--)
#define ll long long

typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL, LL> PLL;
typedef unsigned long long ULL;

const int maxn = 110;

int main(){
        freopen("A-large.in", "r", stdin);
        freopen("A-large.out", "w", stdout);
        int T;
        cin >> T;
        int cas = 0;
        int n;
        LL D, k, s;
        double ans;
        while(T--){
            cas++;
            cin >> D >> n;
            cin >> k >> s;
            ans = D*s*1.0 / (D-k);
            FOR(i, 2, n){
                cin >> k >> s;
                ans = min(ans, D*s*1.0 / (D-k));
                }
            printf("Case #%d: %.6f\n", cas, ans);
            }
        return 0;
        }
