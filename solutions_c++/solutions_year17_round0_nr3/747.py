#include <string>
#include <cstring>
#include <vector>
#include <cmath> 
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
 
using namespace std;
 
#define REP(a,n) for(int a=0; a<(n); ++a)
#define FOR(a,b,c) for(int a=(b); a<=(c); ++a)
#define INIT(a, v) __typeof(v) a = (v)
#define FOREACH(a, v) for (INIT(a, (v).begin()); a!=(v).end(); ++a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long LL;

#define INF 1000000000
#define PB push_back
#define MP make_pair
 
//////////////////////////////////////////

LL N, K;

void licz() {
    scanf("%lld%lld", &N, &K);
    priority_queue<pair<LL, LL> > Q;
    Q.push(MP(N, 1));
    LL a = 0;
    for(;;) {
        LL z = Q.top().first;
        LL ile = Q.top().second;
        Q.pop();
        while (!Q.empty() && Q.top().first==z) {
            ile += Q.top().second;
            Q.pop();
        }
        --z;
        LL z1 = z/2;
        LL z2 = z-z1;
        Q.push(MP(z1, ile));
        Q.push(MP(z2, ile));
        a += ile;
        if (a>=K) {
            printf("%lld %lld\n", z2, z1);
            break;
        }
    }
}

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        printf("Case #%d: ", (tt+1));
        licz();
    }
}


