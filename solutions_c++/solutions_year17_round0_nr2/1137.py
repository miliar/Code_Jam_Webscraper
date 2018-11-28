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
#define K 23333
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

char s[100];

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
        scanf("%s",s);
        n = strlen(s);
        bool flag = false;
        for (int i = 1; i < n; ++i) {
            if (flag) s[i] = '9';
            else {
                while (i>=1&&s[i]<s[i-1]) {
                    --s[--i];
                    flag = true;
                }
            }
        }
        int t = 0;
        while (s[t]=='0') ++t;
        printf("Case #%d: ",ci);
        puts(s+t);
    }
    return 0;
}
