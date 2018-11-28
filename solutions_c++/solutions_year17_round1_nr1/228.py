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

int R, C;

char tab[30][30];

int jest[30], x0[30], Y0[30], x1[30], Y1[30];

void bt(int x, int y) {
    if (x==R) {
        x = 0;
        ++y;
    }
    while (y<C) {
        if (tab[x][y]=='?')
            break;
        ++x;
        if (x==R) {
            x = 0;
            ++y;
        }
    }
    if (y==C)
        throw 0;
    REP(c, 26) {
        if (!jest[c])
            continue;
        int newx0 = min(x0[c], x);
        int newY0 = min(Y0[c], y);
        int newx1 = max(x1[c], x);
        int newY1 = max(Y1[c], y);
        FOR(xx, newx0, newx1)
            FOR(yy, newY0, newY1)
                if (tab[xx][yy]!='?' && tab[xx][yy]!=c+'A')
                    goto dalej;
        FOR(xx, newx0, newx1)
            FOR(yy, newY0, newY1)
                tab[xx][yy] = c+'A';
        swap(newx0, x0[c]);
        swap(newx1, x1[c]);
        swap(newY0, Y0[c]);
        swap(newY1, Y1[c]);
        bt(x+1, y);
        swap(newx0, x0[c]);
        swap(newx1, x1[c]);
        swap(newY0, Y0[c]);
        swap(newY1, Y1[c]);
        FOR(xx, newx0, newx1)
            FOR(yy, newY0, newY1)
                if (xx<x0[c] || xx>x1[c] || yy<Y0[c] || yy>Y1[c])
                    tab[xx][yy] = '?';
        dalej:;
    }
}

void licz() {
    scanf("%d%d", &R, &C);
    REP(x, R)
        scanf("%s", tab[x]);
    REP(a, 26)
        jest[a] = 0;
    REP(x, R) REP(y, C)
        if (tab[x][y]!='?') {
            int c = tab[x][y]-'A';
            x0[c] = x1[c] = x;
            Y0[c] = Y1[c] = y;
            jest[c] = 1;
        }
    try {
        bt(0,0);
    }
    catch (...) {}
    REP(a, R)
        printf("%s\n", tab[a]);
}

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        printf("Case #%d:\n", (tt+1));
        licz();
    }
}


