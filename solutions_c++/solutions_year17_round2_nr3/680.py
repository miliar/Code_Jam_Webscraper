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


const int MAX = 105;
int n, m, horseLim[MAX], horseSpeed[MAX], d[MAX][MAX];
bool visit[MAX];
double cost[MAX][MAX];

struct data {
    int pos, horseTown;
    double dis;
    LL horseDis;

    data() {}
    data(int _pos, int _horseTown, double _dis, LL _horseDis) {
        pos = _pos, horseTown = _horseTown, dis = _dis, horseDis = _horseDis;
    }

    inline bool operator < (const data &p) const {
        if(dis > p.dis) return true;
        else if(fabs(dis-p.dis) < eps) {
            if(horseLim[horseTown]-horseDis < horseLim[p.horseTown]-p.horseDis) return true;
            else return false;
        }
        else return false;
    }
};

inline double dijkstra(int a, int b) {
    priority_queue <data> q;
    int i, j, v;

    repl(i, n) repl(j, n) cost[i][j] = numeric_limits <double>::max();
    q.push(data(a, a, 0.0, 0));
    cost[a][a] = 0.0;

    while(!q.empty()) {
        data u = q.top();
        q.pop();

//        cerr << u.pos << " " << u.dis << endl;

        if(u.pos == b) return u.dis;

        if(u.horseTown != u.pos) q.push(data(u.pos, u.pos, u.dis, 0));

        repl(v, n) {
            if(v == u.pos) continue;
            if(d[u.pos][v] != -1 && u.horseDis+d[u.pos][v] <= horseLim[ u.horseTown ]) {
                double here = (double)d[u.pos][v]/(double)horseSpeed[u.horseTown];
//                DB(here);
                if(u.dis+here < cost[v][u.horseTown]) {
                    cost[v][u.horseTown] = u.dis + here;
//                    if(v == b) return cost[v];
//                    cerr << v << " " << cost[v] << endl;
                    q.push(data(v, u.horseTown, cost[v][u.horseTown], u.horseDis+d[u.pos][v]));
                }
            }
        }
    }
}

int main() {
//    assert(freopen("in.txt","r",stdin));
//    assert(freopen("out.txt","w",stdout));
    assert(freopen("C-large.in","r",stdin));
    assert(freopen("C-large.out","w",stdout));

//    srand(time(NULL));

    int test, kase=1, u, v, i, j;

    sdi(test);
    while(test--) {
        cerr << kase << endl;
        sdii(n, m);
        repl(i, n) {
            sdii(horseLim[i], horseSpeed[i]);
        }
        repl(i, n) {
            repl(j, n) {
                sdi(d[i][j]);
            }
        }
        printf("Case #%d:", kase++);
        while(m--) {
            sdii(u, v);
            printf(" %.8f", dijkstra(u, v));
        }
        puts("");
    }

    return 0;
}
