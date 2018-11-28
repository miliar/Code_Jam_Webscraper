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

void licz() {
    scanf("%s", tab);
    int N = strlen(tab);
    int start = -1; 
    char last_dig = '0';
    REP(a, N)
        if (tab[a]>last_dig) {
            last_dig = tab[a];
            start = a;
        }
        else if (tab[a]<last_dig) {
            --tab[start];
            FOR(b, start+1, N-1)
                tab[b] = '9';
            break;
        }
    printf("%s\n", tab[0]=='0' ? tab+1 : tab);
}

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        printf("Case #%d: ", (tt+1));
        licz();
    }
}


