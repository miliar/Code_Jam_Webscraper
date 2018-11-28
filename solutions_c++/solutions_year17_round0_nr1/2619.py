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

int k;
char s[1010];

void solve()
{
    scanf("%s %d", s, &k);
    int res = 0, n = strlen(s);

    REP(i, n-k+1)if(s[i]=='-')
    {
        ++res;
        FOR(j,i,i+k)
            s[j]=(s[j]=='-')?'+':'-';
    }

    if (find(s+(n-k), s+n, '-') != s+n)
        printf("IMPOSSIBLE\n");
    else
        printf("%d\n", res);
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
