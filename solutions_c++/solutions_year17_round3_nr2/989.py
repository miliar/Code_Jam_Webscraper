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
        int col;
        int l, r;
        friend bool operator<(const Node &n1, const Node &n2){
            return n1.l < n2.l;
            }
        };

Node nd[maxn];


int main(){
        //printf("%.10f\n", PI);
        freopen("B-small-attempt1.in", "r", stdin);
        freopen("B-small-new.out", "w", stdout);
        int T;
        cin >> T;
        int n, m;
        for(int cas=1; cas <= T; cas++){
            cin >> n >> m;
            int ans = 2;
            if(n+m <= 2){
                FOR(i, 1, n) {
                    cin >> nd[i].l >> nd[i].r;
                    nd[i].col = -1;
                    }
                FOR(i, 1, m) {
                    cin >> nd[i+n].l >> nd[i+n].r;
                    nd[i].col = 1;
                    }
                sort(nd+1, nd+n+m+1);
                if(n+m==1 || n==1 || m==1) ans=2;
                else if(n == 0 || m == 0){
                    if(nd[2].r-nd[1].l <= 720 || 1440 - nd[2].l + nd[1].r <= 720)  ans = 2;
                    else ans = 4;
                    }
                }
            else{

                }
            printf("Case #%d: %d\n",cas,ans);
            }
        return 0;;
        }

