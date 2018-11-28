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

int N, P;
int ile[5];

void licz() {
    scanf("%d%d", &N, &P);
    int res = 0;
    REP(a, 5) ile[a] = 0;
    REP(a, N) {
        int b;
        scanf("%d", &b);
        ++ile[b%P];
    }
    res += ile[0];
    if (P==2) {
        res += (ile[1]+1)/2;
    }
    if (P==3) {
        int x = min(ile[1], ile[2]);
        int y = max(ile[1], ile[2])-x;
        res += x;
        res += (y+2)/3;
    }
    if (P==4) {
        int x = min(ile[1], ile[3]);
        int y = max(ile[1], ile[3])-x;
        res += x;
        res += ile[2]/2;
        if (ile[2]%2)
            res += (y+5)/4;
        else
            res += (y+3)/4;
        
    }
    printf("%d\n", res);
}

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        printf("Case #%d: ", (tt+1));
        licz();
    }
}


