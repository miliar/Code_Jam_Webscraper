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

char tab[100000];
int K;

void licz() {
    int ile = 0;
    scanf("%s%d", tab, &K);
    int N = strlen(tab);
    REP(a, N) {
        if (tab[a]=='+') continue;
        ++ile;
        REP(b, K) {
            if (a+b>=N) {
                printf("IMPOSSIBLE\n");
                return;
            }
            tab[a+b] = (tab[a+b]=='-') ? '+' : '-';
        }
    }
    printf("%d\n", ile);
}

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        printf("Case #%d: ", (tt+1));
        licz();
    }
}


