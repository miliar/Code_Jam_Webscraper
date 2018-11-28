#include<time.h>
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<map>
#include<queue>
#define maxn 1101
#define MAXN 120
#define inf (1<<30)
#define modp 1000000007

#define fst first
#define scn second
using namespace std;

typedef long long LL;
int n,m,tot;

LL mpow(LL x, LL y)
{
    if (y==0) return 1;
    LL res=mpow(x,y>>1);
    res*=res;
    res%=modp;
    if (y&1) res*=x;
    return res%modp;
}

typedef pair<double,double> PNT;
typedef pair<LL, LL> PA;

typedef struct Ed{
    int l,r,nxt;
}E;

const double pi=4*atan(1);
const double eps = 1e-6;

char upc(char x)
{
    if (x>='a'&&x<='z') return x-32; else return x;
}

int mcmp(const E& x, const E&y)
{
    return x.nxt<y.nxt;
}

int C;
int q[maxn],u[maxn];

int chk(int d) {
    int pr=0;
    int res=0;
    for (int i=1;i<=n;++i) {
        if (q[i]<d) res+=d-q[i];
        else {
            if (q[i]-d>res) return -1;
            res-=q[i]-d;
            pr+=q[i]-d;
        }
    }
    return pr;
}

int main(void)
{
    int T = 1;
    char op;
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for (int ci = 1; ci <= T; ++ci)
    //while (scanf("%d",&n)!=EOF)
    {
        scanf("%d%d%d",&n,&C,&m);
        memset(q,0,sizeof(q));
        memset(u,0,sizeof(u));
        for (int i=0;i<m;++i) {
            int x,y;
            scanf("%d%d",&x,&y);
            q[x]++;
            u[y]++;
        }
        int mx=0;
        for (int i=1;i<=C;++i) mx = max(mx,u[i]);
        int l=mx-1, r=m;
        int ans=0, tmp;
        while (l+1<r) {
            int mi=l+r>>1;
            if ((tmp=chk(mi))>=0) r=mi, ans=tmp;
            else l=mi;
        }
        printf("Case #%d: %d %d\n",ci, r,ans);
    }
    return 0;
}
