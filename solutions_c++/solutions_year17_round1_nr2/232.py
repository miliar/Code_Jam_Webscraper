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

int N, P, potrzeba[50], paczki[50][50], zuzyte[50];

void licz() {
    scanf("%d%d", &N, &P);
    REP(a, N)
        scanf("%d", &potrzeba[a]);
    REP(s, N) {
        REP(a, P)
            scanf("%d", &paczki[s][a]);
        sort(paczki[s], paczki[s]+P);
        zuzyte[s] = 0;
    }
    int ile = 0;
    FOR(c, 1, INF) {
        REP(s, N) {
            while (zuzyte[s]<P && 10*paczki[s][zuzyte[s]]<9*potrzeba[s]*c)
                ++zuzyte[s];
            if (zuzyte[s]==P) {
                printf("%d\n", ile);
                return;
            }
            if (10*paczki[s][zuzyte[s]]>11*potrzeba[s]*c)
                goto dalej;
        }
        REP(s, N)
            ++zuzyte[s];
        ++ile;
        --c;
    dalej:;
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


