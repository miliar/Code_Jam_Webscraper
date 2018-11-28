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
#define FORD(a,b,c) for(int a=(b); a>=(c); --a)
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

int M,K,B;
int ile[1000]; // [kli]
int chce[1000]; // [poz]

void licz() {
    scanf("%d%d%d", &M, &K, &B);
    REP(a, K)
        ile[a] = 0;
    REP(b, M)
        chce[b] = 0;
    REP(a, B) {
        int poz, kli;
        scanf("%d%d", &poz, &kli);
        --poz; --kli;
        ++ile[kli];
        ++chce[poz];
    }
    int musze = 0;
    REP(k, K)
        musze = max(musze, ile[k]);
    int razem = 0;
    REP(p, M) {
        razem += chce[p];
        int m = p+1;
        musze = max(musze, (razem+m-1)/m);
    }
    
    int upgr = 0;
    REP(p, M)
        upgr += max(0, chce[p]-musze);
    
    printf("%d %d\n", musze, upgr);
}

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        printf("Case #%d: ", (tt+1));
        licz();
    }
}


