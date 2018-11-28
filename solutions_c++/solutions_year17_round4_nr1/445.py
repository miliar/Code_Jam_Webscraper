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

int f[107][107][107][4];
int q[107];
int r[4];

struct res{
    int r[4];
};

int solve(res r) {
    if (r.r[1]==0&&r.r[2]==0&&r.r[3]==0) return 0;
    if (f[r.r[1]][r.r[2]][r.r[3]][r.r[0]]!=-1) return f[r.r[1]][r.r[2]][r.r[3]][r.r[0]];
    int &d=f[r.r[1]][r.r[2]][r.r[3]][r.r[0]];
    int tmp;
    for (int i=1;i<m;++i) {
        if (r.r[i]>0) {
            res k=r;
            k.r[i]--;
            k.r[0]=(k.r[0]+m-i)%m;
            tmp=solve(k);
            if (r.r[0]==0) tmp++;
            d=max(d,tmp);
        }
    }
    return d;
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
        scanf("%d%d",&n,&m);
        memset(f,-1,sizeof(f));
        res r;
        r.r[0]=0;
        r.r[1]=0;
        r.r[2]=0;
        r.r[3]=0;
        int r0 = 0;
        for (int i=0;i<n;++i) {
            scanf("%d",q+i);
            r.r[q[i]%m]++;
        }
        r0=r.r[0];
        r.r[0]=0;
        int ans = solve(r) + r0;
        printf("Case #%d: %d\n",ci, ans);
    }
    return 0;
}
