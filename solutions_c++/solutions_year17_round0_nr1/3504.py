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
const int M = 2e5 + 5, INF = 0x3f3f3f3f, mod = 1e9 + 7;
char s[M];
int sum[M];
int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--){
        memset(sum,0,sizeof(sum));
        scanf("%s",s+1);
        int n=strlen(s+1),K;
        scanf("%d",&K);
        for(int j=1;j+K-1<=n;j++){
            if(j) sum[j]=sum[j-1];
            int t=(sum[j]-sum[max(0,j-K)])&1;
            if((t&&s[j]=='+')||(!t&&s[j]=='-')){
//                printf("j = %d\n",j);
                sum[j]++;
            }
        }
        for(int j=n-K+2;j<=n;j++) sum[j]=sum[j-1];
        int ok=1;
        for(int j=1;j<=n;j++){
            int t=(sum[j]-sum[max(0,j-K)])&1;
            if((t&&s[j]=='+')||(!t&&s[j]=='-')){
//                printf("j = %d\n",j);
                ok=0;
            }
        }
        printf("Case #%d: ",cas++);
        if(!ok) printf("IMPOSSIBLE\n");
        else printf("%d\n",sum[n]);
    }
    return 0;
}
