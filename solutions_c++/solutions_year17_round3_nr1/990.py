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

struct Node{
        ll r, h;
        friend bool operator<(const Node &n1, const Node &n2){
            //if(n1.r != n2.r) return n1.r > n2.r;
            //return n1.h > n2.h;
            return n1.r * n1.h > n2.r * n2.h;
            }
        };

Node nd[maxn];


int main(){
        //printf("%.10f\n", PI);
        freopen("A-large.in", "r", stdin);
        freopen("A.out", "w", stdout);
        int T;
        cin >> T;
        for(int cas=1; cas <= T; cas++){
            int n, k;
            cin >> n >> k;
            FOR(i, 1, n){
                cin >> nd[i].r >> nd[i].h;
                }
            sort(nd+1, nd+n+1);
            double mx = 0;
            for(int i=1; i <= n; i++){
                double ans = nd[i].r * nd[i].r + 2*nd[i].r*nd[i].h;
                int cnt = 1;
                for(int j=1; j <=n; j++) {
                    if(cnt == k) break;
                    if(j != i && nd[j].r <= nd[i].r){
                        cnt++;
                        ans += 2*nd[j].r*nd[j].h;
                        }
                    }
                mx = max(mx, ans);
                }
            printf("Case #%d: %.10f\n",cas,  PI*mx);

            }
        return 0;;
        }

