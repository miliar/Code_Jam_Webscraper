#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<cstring>
#include<string>
#include<cmath>
#include<complex>
#include<ctime>
#include<functional>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pii;
typedef vector<ll> vi;
typedef vi::iterator vit;
typedef set<ll> si;
typedef si::iterator sit;
typedef vector<pii> vpi;
typedef pair<int, char> pci;
typedef vector<pci> vpci;

#define sq(x) ((x)*(x))
#define all(x) (x).begin(),(x).end()
#define cl(x) memset(x,0,sizeof(x))
//#define LL "%I64d"
#define LL "%lld"
#define RLL(x) scanf(LL,&(x))

int n,q;
ll dst[100][100];
double times[100][100];
int e[100];
int s[100];

void test(int T)
{
    scanf("%d%d", &n, &q);
    for(int i = 0; i < n; ++i)
        scanf("%d%d",e+i,s+i);
    for(int i=0; i<n; ++i)
        for(int j=0; j<n; ++j)
        {
            scanf("%lld", &dst[i][j]);
            if(dst[i][j] == -1)
                dst[i][j] = 1e15;
        }
    for(int k=0; k<n; ++k)
        for(int i=0; i<n; ++i)
            for(int j=0; j<n; ++j)
                dst[i][j] = min(dst[i][j], dst[i][k]+dst[k][j]);
    for(int i=0; i<n; ++i)
        for(int j=0; j<n; ++j)
            if(e[i] >= dst[i][j])
                times[i][j] = dst[i][j] / double(s[i]);
            else
                times[i][j] = 1e15;
    for(int k=0; k<n; ++k)
        for(int i=0; i<n; ++i)
            for(int j=0; j<n; ++j)
                times[i][j] = min(times[i][j], times[i][k]+times[k][j]);
    printf("Case #%d:", T);
    for(int i=0; i<q; ++i)
    {
        int u,v;
        scanf("%d%d",&u,&v);
        --u;--v;
        double t = times[u][v];
        //if(t > 5e14)
        //    t = -1;
        printf(" %.10lf", t);
    }
    printf("\n");
}

int main()
{
    freopen("/Users/olpet/Downloads/GCJ/d.in", "r", stdin);
    freopen("/Users/olpet/Downloads/GCJ/d.out", "w", stdout);
    int n;
    cin>>n;
    for(int i = 0; i < n; ++i)
        test(i+1);
    return 0;
}
