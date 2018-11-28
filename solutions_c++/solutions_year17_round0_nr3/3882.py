#include <bits/stdc++.h>
using namespace std;

#define GET_MACRO(_1,_2,_3,_4,NAME,...) NAME
#define REP2(i,n) for(int i=0;i<(int)(n);i++)
#define REP3(i,m,n) for(int i=m;i<(int)(n);i++)
#define REP4(i,m,n,s) for(int i=m;(s>0 and i<(int)(n)) or (s<0 and i>(int)(n));i+=s)
#define REP(...) GET_MACRO(__VA_ARGS__, REP4, REP3, REP2)(__VA_ARGS__)
#define REPIT(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define PIS(x) printf("%d ",x)
#define PRINTIA(a,n) REP(i,n){printf("%d ", *((a)+i));}putchar('\n');
#define PN() putchar('\n')
#define MP make_pair
#define PB push_back

typedef pair<int,int> PII;
typedef long long LL;
typedef unsigned long long ULL;

void RI() {}
template<typename... T>
void RI( int& head, T&... tail ) {
    scanf("%d",&head);
    RI(tail...);
}
void PI() {putchar('\n');}
template<typename... T>
void PI(const int head, T... tail ) {
    printf("%d ", head);
    PI(tail...);
}

priority_queue<pair<LL, LL> > q;

void solve() {
    q = priority_queue<pair<LL, LL> >();

    LL n, k;
    scanf("%lld%lld", &n, &k);
    q.push(MP(n, 1LL));
    while(k > q.top().second) {
        LL space = q.top().first;
        LL number = q.top().second;
        q.pop();
        k -= number;
        if(space % 2 == 1) {
            q.push(MP(space/2, number*2));
        } else {
            q.push(MP(space/2, number));
            q.push(MP(space/2-1, number));
        }
    }
    LL space = q.top().first;
    if(space % 2 == 1) {
        printf("%lld %lld\n", space/2, space/2);
        return;
    }
    printf("%lld %lld\n", space/2, space/2-1);
}

int main()
{
    int T;
    RI(T);
    REP(i, T) {
        printf("Case #%d: ", i+1);
        solve();
    }

    return 0;
}
