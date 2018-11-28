#include <bits/stdc++.h>
using namespace std;

#define x first
#define y second
typedef long long ll;
typedef pair<int,int> pt;
const double base = 1000000007;
const int maxn = 2002;
const double pi = M_PI;

struct pt3{
    double r,h;
    double sideA, faceA;
    pt3() {};
    pt3(int a,int b) {
        r = a; h = b;
        faceA = double(r)*r*pi;
        sideA = 2*pi*r*h;
    }

    bool operator < (const pt3& b) const {
        return (r > b.r) || (r==b.r && h>b.h);
    }
};

int n, K;
pt3 a[maxn];
double f[1002][1002], res;

void solve(int test) {
    int i,j,k,u,v;

    scanf("%d%d",&n,&K);
    for (i=1;i<=n;i++) {
        scanf("%d%d",&u,&v);
        a[i] = pt3(u,v);
    }

    sort(a+1,a+n+1);
    for (i=0;i<=n;i++)
        for (j=0;j<=K;j++) f[i][j] = -base;
    f[0][0] = 0;

    res = 0;
    for (i=1;i<=n;i++) {
        f[i][1] = max(f[i-1][1], a[i].sideA + a[i].faceA);
        for (j=2;j<=min(i,K);j++) f[i][j] = max(f[i-1][j], f[i-1][j-1] - a[i].faceA + a[i].faceA + a[i].sideA);
        res = max(res, f[i][K]);
    }

    printf("Case #%d: %.9lf\n",test,res);
}

int main()
{
    int i,t;
    freopen("A2.in","r",stdin);
    freopen("A.out","w",stdout);

    scanf("%d",&t);
    for (i=1;i<=t;i++) solve(i);

    return 0;
}
