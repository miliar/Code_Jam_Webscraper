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


char dgs[22];

ll to_number(char* first, char* last)
{
    ll res = 0;
    while(first != last)res=10*res + *first++;
    return res;
}

ll calculate_last_tidy(ll n)
{
    int m=0;
    do {
        dgs[m++]=n%10;
        n /= 10;
    } while(n);
    reverse(dgs, dgs+m);

    FOR(i,1,m)if(dgs[i] < dgs[i-1])
    {
        ll res = calculate_last_tidy(to_number(dgs, dgs+i)-1LL);
        FOR(j,i,m)res=10*res+9;
        return res;
    }

    return to_number(dgs, dgs+m);
}

void solve()
{
    ll n;
    scanf("%lld", &n);
    printf("%lld\n", calculate_last_tidy(n));
}


int main()
{
    //freopen("../input.txt", "r", stdin);
    //freopen("../data/B-small-attempt0.in", "r", stdin);
    freopen("../data/B-large.in", "r", stdin);

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
