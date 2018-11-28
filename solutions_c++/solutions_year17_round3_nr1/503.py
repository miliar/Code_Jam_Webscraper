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
const double pi=acos(-1.0);
struct node{
    int r,h;
}A[M];
bool cmp(node a,node b){
    if(a.r!=b.r) return a.r>b.r;
    return a.h>b.h;
}
int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--){
        int n,m;
        scanf("%d%d",&n,&m);
        for(int j=1;j<=n;j++) scanf("%d%d",&A[j].r,&A[j].h);
        sort(A+1,A+1+n,cmp);
        double ans=0;
        for(int j=1;j<=n-m+1;j++){
            double now=pi*A[j].r*A[j].r+pi*A[j].r*A[j].h*2;
            priority_queue<double>q;
            for(int k=j+1;k<=n;k++){
                q.push(pi*A[k].r*A[k].h*2);
            }
            for(int k=1;k<m;k++){
                now+=q.top();q.pop();
            }
            ans=max(ans,now);
        }
        printf("Case #%d: %.12f\n",cas++,ans);
    }
    return 0;
}
