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

int n,p, g[111];

void solve()
{
    scanf("%d %d", &n, &p);
    REP(i,n)scanf("%d", g+i);

    int res = 0;
    REP(i,n)if(g[i]%p==0)++res, g[i]=333;

    sort(g,g+n);
    while(n>0&&g[n-1]==333)--n;

    int cnt[4] = {0};
    REP(i,n)++cnt[g[i]%p];

    if (p==2)
    {
        int mn = (cnt[1]+1)/2;
        res += mn;
    }

    if (p==3)
    {
        int mn = min(cnt[1], cnt[2]);
        res += mn;
        cnt[1] -= mn;
        cnt[2] -= mn;

        if (cnt[1] > 0)
        {
            mn = cnt[1]/3;
            res += mn;
            cnt[1] -= 3*mn;
        }

        if(cnt[2] > 0)
        {
            mn = cnt[2]/3;
            res += mn;
            cnt[2] -= 3*mn;
        }

        res += min(cnt[1]+cnt[2], 1);
    }

    if (p==4)
    {
        int mn = min(cnt[1], cnt[3]);
        res += mn;
        cnt[1] -= mn;
        cnt[3] -= mn;

        mn = min(cnt[2], cnt[1]/2);
        res += mn;
        cnt[2] -= mn;
        cnt[1] -= 2*mn;

        mn = min(cnt[2], cnt[3]/2);
        res += mn;
        cnt[2] -= mn;
        cnt[3] -= 2*mn;

        mn = cnt[2]/2;
        res += mn;
        cnt[2] -= 2*mn;

        mn = cnt[1]/4;
        res += mn;
        cnt[1] -= 4*mn;

        mn = cnt[3]/4;
        res += mn;
        cnt[3] -= 4*mn;

        res += min(cnt[1] + cnt[2] + cnt[3], 1);
    }

    printf("%d\n", res);
}


int main()
{
    freopen("../input.txt", "r", stdin);
    //freopen("../data/A-small-attempt1.in", "r", stdin);
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
