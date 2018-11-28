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
#include <cstring>
#include <unordered_map>
using namespace std;
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) (int)(a).size()
#define FOR(i,s,n) for(int i=(s);i<(n);++i)
#define REP(i,n) FOR(i,0,(n))
#define PB(x) push_back((x))
#define CLR(a,v) memset((a),(v),sizeof((a)))
typedef long long ll;

int E[101], S[101], D[101];
double f[101];

void solve()
{
    int n,q;
    scanf("%d %d", &n,&q);

    REP(i,n)scanf("%d %d",E+i, S+i);

    int tmp;
    REP(i,n)REP(j,n)if(i+1!=j)scanf("%d",&tmp);else scanf("%d",D+i);
    REP(i,q)scanf("%d %d",&tmp, &tmp);

    f[n-1]=0;

    for(int i=n-2;i>=0; --i)
    {
        f[i]=1e300;
        ll d = 0;
        FOR(j,i+1,n)
        {
            d += D[j-1];
            if(d>E[i])break;
            f[i]=min(f[i],d/double(S[i])+f[j]);
        }
    }

    printf("%.8f\n",f[0]);
}


int main()
{
    //freopen("../input.txt", "r", stdin);
    freopen("../data/C-small-attempt0.in", "r", stdin);
    //freopen("../data/C-large.in", "r", stdin);

    freopen("../output.txt", "w+", stdout);

    int T;
    scanf("%d", &T);
    REP(i, T)
    {
        printf("Case #%d: ", i+1);
        solve();
    }

    return 0;
}
