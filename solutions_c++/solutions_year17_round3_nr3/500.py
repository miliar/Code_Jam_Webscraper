#include <set>
#include <cmath>
#include <stack>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <numeric>
#include <vector>
#include <ctime>
#include <queue>
#include <list>
#include <map>
#define pi acos(-1.0)
#define INF 0x3f3f3f3f
#define clr(x)  memset(x,0,sizeof(x));
#define clrto(x,siz,y)  for(int xx=0;xx<=siz;xx++)  x[xx]=y;
#define clrset(x,siz)  for(int xx=0;xx<=siz;xx++)  x[xx]=xx;
#define clr_1(x) memset(x,-1,sizeof(x));
#define clrmax(x) memset(x,0x3f,sizeof(x));
#define clrvec(x,siz) for(int xx=0;xx<=siz;xx++)  x[xx].clear();
#define fop2   freopen(".in","r",stdin); //freopen(".out","w",stdout);
#define fop   freopen("in.txt","r",stdin);//freopen("out.txt","w",stdout);
#define getfile char fin[11], fout[11]; sprintf(fin, "%d.in", i); sprintf(fout, "%d.out", i); freopen(fin, "r", stdin); freopen(fout, "w", stdout);
#define makefile char fout[11]; sprintf(fout, "%d.in", i); freopen(fout, "w", stdout);
#define myprogram By_135678942570
#define clrcpy(x,siz,y)  for(int xx=0;xx<siz;xx++)  x[xx]=y[xx];
#define pb push_back
using namespace std;


const double eps = 1e-8;
int n, k;
double u;
double p[500];
bool ok(double x)
{
    double sum = 0.0;
    for(int i = 0; i < n; i++)
    {
        sum += max(0.0, x - p[i]);
    }
    return sum < u;
}
int main()
{
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("C-small-1-attempt0.out", "w", stdout);
    int t, cas = 1;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d%lf", &n, &k, &u);
        for(int i = 0; i < n; i++)
            scanf("%lf", p + i);
        double l = 0.0, r = 1.0, mid;
        while(r - l > eps)
        {
            mid = (l + r) * 0.5;
            if(ok(mid))
                l = mid;
            else
                r = mid;
        }
        double ans = 1.0;
        for(int i = 0; i < n; i++)
            ans *= max(l, p[i]);
        printf("Case #%d: %.8f\n", cas++, ans);
    }
    return 0;
}

