#pragma comment(linker, "/STACK:1024000000,1024000000")
#include<algorithm>
#include<iostream>
#include<cstring>
#include<fstream>
#include<bitset>
#include<cstdio>
#include<string>
#include<vector>
#include<cmath>
#include<queue>
#include<stack>
#include<map>
#include<set>
#define INF 0X3F3F3F3F
#define N 10005
#define M 200005
#define LL long long
#define FF(i, a, b) for(int i = a; i <= b; ++i)
#define RR(i, a, b) for(int i = a; i >= b; --i)
#define FJ(i, a, b) for(int i = a; i < b; ++i)
#define SC(x) scanf("%d", &x)
#define SCC(x, y) scanf("%d%d", &x, &y)
#define SCCC(x, y, z) scanf("%d%d%d", &x, &y, &z)
#define SS(x) scanf("%s", x)
#define PR(x) printf("%d\n", x)
#define CL(a, x) memset(a, x, sizeof(a))
#define _P fd[rt]
#define _L fd[rt << 1]
#define _R fd[rt << 1 | 1]
#define MID int mid = ((l + r) >> 1)
#define lson rt<<1 ,l, mid
#define rson rt<<1 | 1, mid + 1, r
#define PB push_back
#define SZ size
#define PII pair<int, int>
#define PLL pair<long long, long long>
#define MP make_pair
#define IN freopen("A-large.in", "r", stdin)
#define OUT freopen("A-large.out", "w", stdout)
using namespace std;
const int MOD = 1000000007;
const double PI = acos(-1.0);
const double EPS = 1e-8;
inline void II(int &n){char ch = getchar(); n = 0; bool t = 0;
for(; ch < '0'; ch = getchar()) if(ch == '-') t = 1;
for(; ch >= '0'; n = n * 10 + ch - '0', ch = getchar()); if(t) n =- n;}
inline void OO(int a){if(a < 0) {putchar('-'); a = -a;}
if(a >= 10) OO(a / 10); putchar(a % 10 + '0');}
struct T{
    double r, h, s;
    bool operator < (const T& rhs)const {
        return s > rhs.s;
    }
}a[N];
int n, k;
int main(){
    IN;
    OUT;
    int _; SC(_);
    FF(CA, 1, _){
        SCC(n, k);
        FF(i, 1, n){
            scanf("%lf%lf", &a[i].r, &a[i].h);
            a[i].s = 2 * PI * a[i].r * a[i].h;
        }
        sort(a + 1, a + 1 + n);
        double ans = 0;
        int cnt = 0;
        FF(i, 1, n){
            double s = a[i].r * a[i].r * PI;
            s += a[i].s;
            cnt = 1;
            FF(j, 1, n){
                if(cnt == k) break;
                if(i != j && a[j].r <= a[i].r){
                    ++cnt;
                    s += a[j].s;
                }
                if(cnt == k) break;
            }
            if(cnt == k){
                if(s > ans) ans = s;
            }
        }
        printf("Case #%d: %.10f\n", CA, ans);
    }
    return 0;
}
