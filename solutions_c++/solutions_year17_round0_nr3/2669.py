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


void solve()
{
    ll n, k, rL, rR;
    scanf("%lld %lld", &n, &k);

    ll stalls_taken=0, actions_on_next_level=1, sum_on_next_level=n;
    while(stalls_taken+actions_on_next_level<k)
    {
        sum_on_next_level -= actions_on_next_level;
        stalls_taken+=actions_on_next_level;
        actions_on_next_level*=2;
    }

    ll remain_actions=k-stalls_taken;
    ll gap_size = sum_on_next_level/actions_on_next_level;
    if(remain_actions<=sum_on_next_level%actions_on_next_level)++gap_size;

    printf("%lld %lld\n", gap_size/2, (gap_size-1)/2);
}


int main()
{
    //freopen("../input.txt", "r", stdin);
    //freopen("../data/C-small-2-attempt0.in", "r", stdin);
    freopen("../data/C-large.in", "r", stdin);

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
