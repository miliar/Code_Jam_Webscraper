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

int n,k;
pair<int,int> p[1010];

const double pi = 3.14159265359;
ll f[1010][1010];

ll area(int i)
{
    return p[i].first*1LL*p[i].first + 2*p[i].first*1LL*p[i].second;
}

ll area(int i, int j)
{
    if(i>j)swap(i,j);
    return area(i)-p[j].first*1LL*p[j].first;
}

void solve()
{
    scanf("%d %d", &n, &k);
    REP(i,n)scanf("%d %d", &p[i].first, &p[i].second);
    sort(p,p+n);
    reverse(p,p+n);

    REP(i,1010)REP(j,1010)f[i][j]=0;

    f[n-1][1] = area(n-1);
    for (int i = n-2; i>=0; --i)
    {
        f[i][1] = area(i);
        for (int j=2; j<=k; ++j)FOR(t,i+1,n)
        {
            f[i][j]=max(f[i][j],f[t][j-1]+area(i,t));
        }
    }

    ll res = 0;
    REP(i,n)res=max(res, f[i][k]);

    printf("%.10f\n",pi*res);
}


int main()
{
    //freopen("../input.txt", "r", stdin);
    //freopen("../data/A-small-attempt0.in", "r", stdin);
    freopen("../data/A-large.in", "r", stdin);

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
