#include <bits/stdc++.h>

#define rep(i,n) for(i=0; i<n; i++)
#define repl(i,n) for(i=1; i<=n; i++)

#define sz(x) (int) x.size()
#define pb push_back
#define all(x) x.begin(),x.end()
#define uu first
#define vv second
#define mem(x, y) memset(x, y, sizeof(x))
#define un(x) x.erase(unique(all(x)), x.end())

#define sdi(x) scanf("%d", &x)
#define sdii(x, y) scanf("%d %d", &x, &y)
#define sdiii(x, y, z) scanf("%d %d %d", &x, &y, &z)
#define sdl(x) scanf("%lld", &x)
#define sdll(x, y) scanf("%lld %lld", &x, &y)
#define sdlll(x, y, z) scanf("%lld %lld %lld", &x, &y, &z)
#define sds(x) scanf("%s", x)
#define pfi(x) printf("%d\n", x)
#define pfii(x, y) printf("%d %d\n", x, y)
#define pfiii(x, y, z) printf("%d %d %d\n", x, y, z)
#define pfl(x) printf("%lld\n", x)
#define pfll(x, y) printf("%lld %lld\n", x, y)
#define pflll(x, y, z) printf("%lld %lld %lld\n", x, y, z)

#define eps 1e-9
#define OK cerr << "ok\n"
#define DB(x) cerr << #x << " = " << x << endl

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair <int, int> pii;

inline int setBit(int N, int pos) { return N=N | (1<<pos); }
inline int resetBit(int N, int pos) { return N= N & ~(1<<pos); }
inline bool checkBit(int N, int pos) { return (bool)(N & (1<<pos)); }

//int kx[] = {+2, +1, -1, -2, -2, -1, +1, +2};
//int ky[] = {+1, +2, +2, +1, -1, -2, -2, -1}; //Knight Direction
//int fx[] = {+0, +0, +1, -1, -1, +1, -1, +1};
//int fy[] = {-1, +1, +0, +0, +1, +1, -1, -1}; //Four & Eight Direction

int r, c;
char str[30][30];
vector <pii> v[30];

inline void cover(pii a, pii b, bool flag=false) {
    for(int i=min(a.uu, b.uu); i<=max(a.uu, b.uu); i++) {
        for(int j=min(a.vv, b.vv); j<=max(a.vv, b.vv); j++) {
            str[i][j] = str[a.uu][a.vv];
            if(flag) v[ str[a.uu][a.vv]-'A' ].pb({ i, j });
        }
    }
    if(flag) {
        sort(all(v[ str[a.uu][a.vv]-'A' ]));
        un(v[str[a.uu][a.vv]-'A']);
    }
}

inline void step1() {
    int i, j, k;
    rep(i, 26) {
        int siz = sz(v[i]);
        if(siz > 1) {
            rep(j, siz) {
                for(k=j+1; k<siz; k++) {
                    cover(v[i][j], v[i][k]);
                }
            }
        }
    }
}

inline bool canCover(pii a, pii b, int c) {
    for(int i=min(a.uu, b.uu); i<=max(a.uu, b.uu); i++) {
        for(int j=min(a.vv, b.vv); j<=max(a.vv, b.vv); j++) {
            if(str[i][j] == '?') continue;
            if(str[i][j]-'A' != c) return false;
        }
    }
    return true;
}

inline bool check(int x, int y, int c) {
    if(sz(v[c]) == 0) return false;
    for(auto now:v[c]) {
        if(!canCover({x, y}, now, c)) return false;
    }
    return true;
}

inline void step2() {
    int i, j, k;
    rep(i, r) {
        rep(j, c) {
            if(str[i][j] == '?') {
                rep(k, 26) {
                    if(sz(v[k]) == 0) continue;
                    if(check(i, j, k)) {
                        for(auto now:v[k]) {
                            cover(now, {i, j}, true);
                        }
                        break;
                    }
                }
            }
        }
    }
}

int main() {
//    assert(freopen("in.txt","r",stdin));
//    assert(freopen("out.txt","w",stdout));
    assert(freopen("A-small.in","r",stdin));
    assert(freopen("A-small.out","w",stdout));

    int test, kase=1, i, j, k, l;

    sdi(test);
    while(test--) {
        cerr << kase << endl;
        rep(i, 26) v[i].clear();

        sdii(r, c);
        rep(i, r) sds(str[i]);
        rep(i, r) {
            rep(j, c) {
                if(str[i][j] != '?') {
                    v[ str[i][j]-'A' ].pb({ i, j });
                }
            }
        }

        step1();
        step2();

//        rep(i, r) puts(str[i]);

        rep(i, r) {
            rep(j, c) {
                assert(str[i][j] != '?');
            }
        }

        rep(i, r) {
            rep(j, c) {
                rep(k, r) {
                    rep(l, c) {
                        if(str[i][j] == str[k][l]) {
                            assert(canCover({i, j}, {k, l}, str[i][j]-'A'));
                        }
                    }
                }
            }
        }

        printf("Case #%d:\n", kase++);
        rep(i, r) puts(str[i]);
    }

    return 0;
}
