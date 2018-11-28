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

char ca[100][100];

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
        for (int i=0;i<n;++i) {
            scanf("%s",ca[i]);
        }
        for (int i=0;i<n;++i) {
            char p='?';
            for (int j=0;j<m;++j) {
                if (ca[i][j]=='?') {
                    ca[i][j]=p;
                } else {
                    p=ca[i][j];
                }
            }
        }
        for (int i=0;i<n;++i) {
            char p='?';
            for (int j=m-1;j>=0;--j) {
                if (ca[i][j]=='?') {
                    ca[i][j]=p;
                } else {
                    p=ca[i][j];
                }
            }
        }
        for (int j=0;j<m;++j) {
            char p='?';
            for (int i=0;i<n;++i) {
                if (ca[i][j]=='?') {
                    ca[i][j]=p;
                } else {
                    p=ca[i][j];
                }
            }

        }
        for (int j=0;j<m;++j) {
            char p='?';
            for (int i=n-1;i>=0;--i) {
                if (ca[i][j]=='?') {
                    ca[i][j]=p;
                } else {
                    p=ca[i][j];
                }
            }

        }
        printf("Case #%d: ",ci);
        puts("");
        for (int i=0;i<n;++i) printf("%s\n",ca[i]);
    }
    return 0;
}
