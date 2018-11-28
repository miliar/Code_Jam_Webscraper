#include <cstdio>
#include <iostream>

using namespace std;

typedef long long LL;

class Data{
public:
    LL n1, c1, c2;
    Data() {}
    Data(LL _n1, LL _c1, LL _c2): n1(_n1), c1(_c1), c2(_c2) {}
};
/// n1 -> bigger,      n2 -> smaller(n1-1)
/// c1 -> count of n1, c2 -> count of n2
/// cnt -> current sum of guys

LL N, K, ans1, ans2; /// ans1 -> max, ans2 -> min

void getans(LL n) {
    ans1 = n/2;
    ans2 = (n-1)/2;
}

void solve(Data cur, LL cnt) {
    //printf("level (%d,%d,%d,%d)\n",cur.n1,cur.c1,cur.c2,cnt);
    if ((cnt+cur.c1) >= K) {
        getans(cur.n1);
        return;
    }

    if ((cnt+cur.c1+cur.c2) >= K) {
        getans(cur.n1-1);
        return;
    }

    Data next;
    next.n1 = cur.n1 / 2;
    if ((cur.n1-1) % 2 == 0) { /// split in to two same blocks
        next.c1 = cur.c1 * 2 + cur.c2;
        next.c2 = cur.c2;
    }
    else { /// two size
        next.c1 = cur.c1;
        next.c2 = cur.c1 + cur.c2 * 2;
    }

    solve(next,cnt+cur.c1+cur.c2);
}

int main() {
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int test;
    scanf("%d",&test);
    for(int t = 1; t <= test; ++t) {
        scanf("%lld%lld",&N,&K);
        solve(Data(N,1,0),0);
        printf("Case #%d: %lld %lld\n",t,ans1,ans2);
    }
    return 0;
}
