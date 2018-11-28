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
#define N 1005
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
#define IN freopen("C-small-1-attempt0.in", "r", stdin)
#define OUT freopen("C-small-1-attempt0.out", "w", stdout)
using namespace std;
const int MOD = 1000000007;
const double PI = acos(-1.0);
const double EPS = 1e-8;
inline void II(int &n){char ch = getchar(); n = 0; bool t = 0;
for(; ch < '0'; ch = getchar()) if(ch == '-') t = 1;
for(; ch >= '0'; n = n * 10 + ch - '0', ch = getchar()); if(t) n =- n;}
inline void OO(int a){if(a < 0) {putchar('-'); a = -a;}
if(a >= 10) OO(a / 10); putchar(a % 10 + '0');}
inline int sgn(double x){return (x > EPS) - (x < -EPS);}
int n, k;
double p[N], U;
int main(){
    IN;
    OUT;
    int _; SC(_);
    FF(CA, 1, _){
        SCC(n, k);
        scanf("%lf", &U);
        FF(i, 1, n){
            scanf("%lf", &p[i]);
        }
        sort(p + 1, p + 1 + n);
        p[n + 1] = 1;
        int cnt = 0;
        double P = 0;
        FF(i, 1, n){
            double t = p[i + 1] - p[i];
            if(sgn(t) > 0){
                double nt = i * t;
                if(sgn(U - nt) >= 0){
                    U -= nt;
                }else {
                    P = p[i] + U / i;
                    cnt = i;
                    break;
                }
            }
        }
        if(cnt == 0){
            printf("Case #%d: 1.000000\n", CA);
            continue;
        }
        double s = 1;
        FF(i, 1, cnt){
            s *= P;
        }
        FF(i, cnt + 1, n){
            s *= p[i];
        }
        printf("Case #%d: %.10f\n", CA, s);
    }
    return 0;
}
