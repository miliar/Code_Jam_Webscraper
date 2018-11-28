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
struct node{
    int pos,speed;
    bool operator <(const node& a){
        if(pos!=a.pos) return pos<a.pos;
        return speed<a.speed;
    }
}A[M];
int main() {
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--){
        int D,n;
        scanf("%d%d",&D,&n);
        for(int j=1;j<=n;j++){
            scanf("%d%d",&A[j].pos,&A[j].speed);
        }
        sort(A+1,A+1+n);
        int ed=1;
        for(int j=1;j<n;j++){
            if(A[j+1].speed>A[j].speed) break;
            //if(A[j+1].speed>=A[j].speed&&1LL*A[j].speed*(A[j].pos-A[j+1].pos)<=1LL*(D-A[j].pos)*(A[j+1].speed-A[j].speed)) ed=j+1;
            if(A[j+1].speed<=A[j].speed&&1LL*A[j].speed*(A[j].pos-A[j+1].pos)>=1LL*(D-A[j].pos)*(A[j+1].speed-A[j].speed)) ed=j+1;
            //printf("j = %d 1 = %lld 2 = %lld\n",j,1LL*A[j].speed*(A[j].pos-A[j+1].pos),1LL*(D-A[j].pos)*(A[j+1].speed-A[j].speed));
        }
        //printf("ed = %d\n",ed);
        //printf("sp = %d\n",A[ed].speed);
        double ans=1.0*D*A[ed].speed/(D-A[ed].pos);
        printf("Case #%d: %.12f\n",cas++,ans);
    }
    return 0;
}
