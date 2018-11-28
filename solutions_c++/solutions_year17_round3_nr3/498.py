#pragma comment(linker, "/STACK:102400000,102400000")
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <complex>
#define LL long long
#define ULL long long
#define ls(x) tree[x].ls
#define rs(x) tree[x].rs
#define maxx(x) tree[x].maxx
#define len(p) (p.R-p.L+1)
#define keytree ch[ch[root][1]][0]
#define dis(x) dis[x.x1][x.y1][x.x2][x.y2][x.dir1][x.dir2]
using namespace std;
const int M = 1e6 + 5, INF = 0x3f3f3f3f, mod = 1e9 + 7;
const double eps=1e-12;
double P[M];
int sgn(double x){
    if(fabs(x)<=eps) return 0;
    if(x>0) return 1;
    return -1;
}
int main() {
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("C-small-1-attempt0.out","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--){
        int n,m;
        scanf("%d%d",&n,&m);
        double U;
        scanf("%lf",&U);
        for(int j=1;j<=n;j++) scanf("%lf",&P[j]);
        double ans=1;
        double l=0.0,r=1.0;
        for(int t=1;t<=100;t++){
            double mid=(l+r)/2;
            double cnt=0;
            for(int j=1;j<=n;j++){
                if(P[j]<mid) cnt+=mid-P[j];
            }
//            printf("mid = %.12f\n",mid);
            if(sgn(cnt-U)>0){
                r=mid;
            }
            else if(sgn(cnt-U)<0) l=mid;
            else{
                ans=1;
                for(int j=1;j<=n;j++){
                    if(P[j]<mid) ans*=mid;
                    else ans*=P[j];
                }
                break;
            }
        }
        printf("Case #%d: %.12f\n",cas++,ans);
    }
    return 0;
}
