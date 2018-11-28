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



const int maxn = 1010;
const int mod = 10007;
const double PI = 3.1415926535879323846;
const double eps = 1e-12;


double p[maxn];


int main(){
        //printf("%.10f\n", exp(log(2.7)));
        freopen("C-small-1-attempt0.in", "r", stdin);
        freopen("C-small-new.out", "w", stdout);
        int T;
        cin >> T;
        int n, m;
        for(int cas=1; cas <= T; cas++){
            cin >> n >> m;
            double X;
            cin >> X;
            FOR(i, 1, n) cin >> p[i];
            sort(p+1, p+n+1);
            double ans = 0;
            int cur = 1;
            while(cur < n && X > eps){
                if(cur*(p[cur+1]- p[cur]) < X) {
                    X -= cur*(p[cur+1]- p[cur]);
                    p[cur] = p[cur+1];
                    cur++;
                    }
                else{
                    p[cur] += X / cur;
                    break;
                    }
                }
            if(cur == n){
                p[cur] += X / cur;
                }
            for(int i = n; i >= 1; i--){
                //printf("p[%d] %.6f\n", i , p[i]);
                if (i > cur) ans += log(p[i]);
                else ans += log(p[cur]);
                }
            printf("Case #%d: %.8f\n",cas, exp(ans));
            }
        return 0;;
        }

