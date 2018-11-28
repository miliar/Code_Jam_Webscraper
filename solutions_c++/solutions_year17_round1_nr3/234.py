#include <string>
#include <cassert>
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

int B, D;

int estim(int A, int H) {
/*    if (!H)
        return 0;
    int z = ceil(sqrt(H*4LL))-A;
    return max(1, z);
  */
  return 0;  
}

map<pair<pii, pii>, int> wyn;
priority_queue<pair<int, pair<pii, pii> > > Q;

inline void popr(int Hd, int Ad, int Hk, int Ak, int dist) {
    if (Hd<=0)
        return;
    pair<pii, pii> P = MP(MP(Hd, Ad), MP(Hk, Ak));
    if (wyn.find(P)!=wyn.end())
        return;
    wyn[P] = dist;
    Q.push(MP(-dist-estim(Ad, Hk), P));
}

int Hd, Ad, Hk, Ak, Hd_orig;

void licz() {
    wyn.clear();
    while (!Q.empty())
        Q.pop();
    scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);
    Hd_orig = Hd;
    popr(Hd, Ad, Hk, Ak, 0);
    while (!Q.empty()) {
        Hd = Q.top().second.first.first;
        Ad = Q.top().second.first.second;
        Hk = Q.top().second.second.first;
        Ak = Q.top().second.second.second;
        int dist = wyn[Q.top().second];
        Q.pop();
        if (Hk-Ad<=0) {
            printf("%d\n", dist+1);
            return;
        }
        popr(Hd-Ak, Ad, Hk-Ad, Ak, dist+1);
        popr(Hd-Ak, Ad+B, Hk, Ak, dist+1);
        popr(Hd_orig-Ak, Ad, Hk, Ak, dist+1);
        int N = max(0, Ak-D);
        popr(Hd-N, Ad, Hk, N, dist+1);
    }
    printf("IMPOSSIBLE\n");
}

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        printf("Case #%d: ", (tt+1));
        licz();
    }
}


