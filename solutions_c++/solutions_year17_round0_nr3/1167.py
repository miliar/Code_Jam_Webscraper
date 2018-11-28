#include<time.h>
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<queue>
#define maxn 1101
#define MAXN 120
#define inf (1<<30)
#define modp 1000000007
#define p 670001
#define X first
#define Y second
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


PA solve(LL N, LL K) {
    if (K == 1) {
        return PA(N>>1,N-1>>1);
    }
    LL pre = (K>>1);
    PA tmp = solve(N,pre);
    if (K == (pre<<1)) {
        N = tmp.first;
        return PA(N>>1,N-1>>1);
    } else {
        N = tmp.second;
        return PA(N>>1,N-1>>1);
    }
}

int main(void)
{
    int T = 1;
    char op;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for (int ci = 1; ci <= T; ++ci)
    //while (scanf("%d",&n)!=EOF)
    {
        LL N, K;
        cin>>N>>K;
        printf("Case #%d: ",ci);
        LL OD = (N&1), EV = 1 - OD;
        bool flag = (EV?true:false);
        LL b = 1;
        LL oo,ee;
        if (OD) oo = N, ee = N + 1;
        else oo = N + 1, ee = N;
        while (K-b>0) {
            oo=oo-1>>1;
            LL ee1=ee-1>>1, ee2=ee>>1;
            LL NEV = ((!(oo&1))?(OD << 1):0) + EV;
            LL NOD = ((oo&1)?(OD << 1):0) + EV;
            EV = NEV, OD = NOD;
            if (oo==ee1) {
                if (oo&1) ee = ee2; else ee=oo, oo=ee2;
            }
            else {
                if (oo&1) ee = ee1; else ee=oo, oo=ee1;
            }
            flag = oo>ee;
            K-=b;
            b<<=1;
        }
        if (flag) {
            if (K<=OD) {
                flag = true;
            }
            else flag = false;
        } else {
            if (K<=EV) flag = false;
            else flag = true;
        }
        N = (flag?oo:ee);
        cout<<(N>>1)<<" "<<(N-1>>1)<<endl;
    }
    return 0;
}
