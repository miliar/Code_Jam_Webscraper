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
#define N 100005
#define M 200005
#define LL long long
#define FF(i,a,b) for(int i=a;i<=b;++i)
#define RR(i,a,b) for(int i=a;i>=b;--i)
#define FJ(i,a,b) for(int i=a;i<b;++i)
#define SC(x) scanf("%d",&x)
#define SCC(x,y) scanf("%d%d",&x,&y)
#define SCCC(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define SS(x) scanf("%s",x)
#define PR(x) printf("%d\n",x)
#define CL(a, x) memset(a, x, sizeof(a))
#define _q fd[rt]
#define _l fd[rt<<1]
#define _r fd[rt<<1|1]
#define MID int mid=((l+r)>>1)
#define lson rt<<1,l,mid
#define rson rt<<1|1,mid+1,r
#define PB push_back
#define SZ size
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define MP make_pair
#define IN freopen("C-large.in","r",stdin)
#define OUT freopen("C-large.out","w",stdout)
using namespace std;
LL n, k;
LL a, b, na, nb, sa, sb;
int main(){
    IN;
    OUT;
    int _; SC(_);
    FF(CA, 1, _){
        scanf("%lld%lld", &n, &k);
        if(n & 1){
            a = (n - 1) / 2;
            b = 0;
            na = 2;
            nb = 0;
        }else {
            a = (n - 1) / 2;
            b = n - 1 - a;
            na = 1;
            nb = 1;
        }
        if(k == 1){
            if(b == 0)printf("Case #%d: %lld %lld\n", CA, a, a);
            else printf("Case #%d: %lld %lld\n", CA, b, a);
            continue;
        }
        k -= 1;
        while(k > 0){
            if(b == 0){
                if(a & 1){
                    if(k <= na){
                        sb = a / 2;
                        sa = a / 2;
                        break;
                    }
                    k -= na;
                    a = (a - 1) / 2;
                    na = na * 2;
                    sa = sb = a;
                }
                else {
                    if(k <= na){
                        sb = a / 2;
                        sa = a - 1 - sb;
                    }
                    k -= na;
                    b = a / 2;
                    a = b - 1;
                    nb = na;
                }
            }else {
                if(k <= nb){
                    sb = b / 2;
                    sa = b - 1 - sb;
                    break;
                }
                k -= nb;
                if(k <= na){
                    sb = a / 2;
                    sa = a - 1 - sb;
                    break;
                }
                k -= na;
                if(a & 1)na = na * 2 + nb;
                else nb = na + nb * 2;
                b = b / 2;
                a = b - 1;
            }
        }
        printf("Case #%d: %lld %lld\n", CA, sb, sa);
    }
    return 0;
}
