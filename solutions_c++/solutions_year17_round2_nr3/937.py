#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cstring>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <utility>
#include <algorithm>
#include <map>
#include <set>
#include <complex>
#include <cmath>
#include <limits>
#include <cfloat>
#include <climits>
#include <ctime>
#include <cassert>
using namespace std;

#define rep(i,a,n) for(int (i)=(a); (i)<(n); (i)++)
#define repq(i,a,n) for(int (i)=(a); (i)<=(n); (i)++)
#define repr(i,a,n) for(int (i)=(a); (i)>=(n); (i)--)
#define all(v) begin(v), end(v)
#define pb(a) push_back(a)
#define fr first
#define sc second
#define INF 2000000000
#define int long long int

#define X real()
#define Y imag()
#define EPS (1e-10)
#define EQ(a,b) (abs((a) - (b)) < EPS)
#define EQV(a,b) ( EQ((a).X, (b).X) && EQ((a).Y, (b).Y) )
#define LE(n, m) ((n) < (m) + EPS)
#define LEQ(n, m) ((n) <= (m) + EPS)
#define GE(n, m) ((n) + EPS > (m))
#define GEQ(n, m) ((n) + EPS >= (m))

typedef vector<int> VI;
typedef vector<VI> MAT;
typedef pair<int, int> pii;
typedef long long ll;

typedef complex<double> P;
typedef pair<P, P> L;
typedef pair<P, double> C;

int dx[]={1, -1, 0, 0};
int dy[]={0, 0, 1, -1};
int const MOD = 1000000007;
ll mod_pow(ll x, ll n) {return (!n)?1:(mod_pow((x*x)%MOD,n/2)*((n&1)?x:1))%MOD;}
int madd(int a, int b) {return (a + b) % MOD;}
int msub(int a, int b) {return (a - b + MOD) % MOD;}
int mmul(int a, int b) {return (a * b) % MOD;}
int minv(int a) {return mod_pow(a, MOD-2);}
int mdiv(int a, int b) {return mmul(a, minv(b));}

namespace std {
    bool operator<(const P& a, const P& b) {
        return a.X != b.X ? a.X < b.X : a.Y < b.Y;
    }
}

struct Elem {
    int city, horse, dist;
    double cost;
    Elem(int a, int b, int c, double d) : city(a), horse(b), dist(c), cost(d) {}
};

bool operator<(const Elem &a, const Elem &b) {
    return a.cost > b.cost;
}

int e[110], s[110];
int mat[110][110];
signed main() {
    int t; cin >> t;
    repq(cs,1,t) {
        int N, Q; cin >> N >> Q;
        rep(i,0,N) cin >> e[i] >> s[i];
        rep(i,0,N) rep(j,0,N) cin >> mat[i][j];
        printf("Case #%lld:", cs);
        rep(i,0,Q) {
            // city, horse, dist
            map<int, map<int, map<int, double> > > rec;
            int u, v; cin >> u >> v;
            double ans = INF;
            u--; v--;
            priority_queue<Elem> q;
            q.push(Elem(u, u, 0, 0.0));
            while(!q.empty()) {
                Elem pick = q.top(); q.pop();
                int from = pick.city, d = pick.dist, usg = pick.horse;
                // printf("from = %lld, d = %lld, usg = %lld\n", from, d, usg);
                if(from == v) {
                    ans = pick.cost;
                    break;
                }
                rep(to,0,N) {
                    if(mat[from][to] == -1) continue;
                    if(d + mat[from][to] > e[usg]) continue;
                    int nd = d + mat[from][to];
                    double c = (double)mat[from][to] / s[usg];
                    if(rec[to][usg][nd] == 0.0 || rec[to][usg][nd] > rec[from][usg][d] + c) {
                        rec[to][usg][nd] = rec[from][usg][d] + c;
                        // printf("rec[%lld][%lld][%lld] = %lf\n", to, usg, nd, rec[to][usg][nd]);
                        q.push(Elem(to, usg, nd, rec[to][usg][nd]));
                    }
                    if(rec[to][to][0] == 0.0 || rec[to][to][0] > rec[from][usg][d] + c) {
                        rec[to][to][0] = rec[from][usg][d] + c;
                        // printf("rec[%lld][%lld][0] = %lf\n", to, to, rec[to][to][0]);
                        q.push(Elem(to, to, 0.0, rec[to][usg][nd]));
                    }
                }
            }
            printf(" %.12lf", ans);
        }
        cout << endl;
    }
    return 0;
}