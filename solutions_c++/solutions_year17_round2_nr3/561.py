#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <utility>
using namespace std;

#define fi(i,a,b) for(int i=(a);i<(b); ++i)
#define fd(i,a,b) for(int i=(a);i>(b); --i)
#define fie(i,a,b) for(int i=(a);i<=(b); ++i)
#define fde(i,a,b) for(int i=(a);i>=(b); --i)
#define mp(a,b) make_pair(a,b)
#define pb(x) push_back(x)
#define all(x) x.begin(), x.end()
#define rall(s) (s).rbegin(),(s).rend()
#define C(u) memset((u),0,sizeof((u)))
#define inf 1000000000
typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi > vvi;
typedef pair<int, int> pii;

#define INP_FILE "C-large.in"
#define OUT_FILE "output.txt"
struct Horse {
    double time; int city, dur; Horse() {}
    Horse(double time, int city, int dur):time(time), city(city),dur(dur) {}
    bool operator<(const Horse& h) const {
        return time < h.time;
    }
};

struct Solution{
    int n, q;
    vector<double> v;
    vector<ll> e;
    vvi d;
    vector<vector<double> > time1;
    void calcTime(int nod) {
        double sp = v[nod];
        priority_queue<Horse> q;
        q.push(Horse(0.0, nod, e[nod]));
        while (!q.empty()) {
            Horse h = q.top(); q.pop();
            if (h.time > time1[nod][h.city]) continue;
            fi(i, 0, n) if (d[h.city][i] > 0 && d[h.city][i]<=h.dur) {
                double eta = h.time + d[h.city][i] / sp;
                if (eta >= time1[nod][i]) continue;
                time1[nod][i] = eta;
                q.push(Horse(eta, i, h.dur - d[h.city][i]));
            }
        }
    }
    void solve() {
        cin >> n >> q;
        v.resize(n); e.resize(n); fi(i, 0, n) cin >> e[i] >> v[i];
        d.resize(n, vi(n)); fi(i, 0, n) fi(j, 0, n) cin >> d[i][j];
        time1.resize(n, vector<double>(n, 1e13));
        fi(i, 0, n) calcTime(i);
        fi(k, 0, n) fi(i, 0, n) fi(j, 0, n) {
            time1[i][j] = min(time1[i][j],time1[i][k] + time1[k][j]);
        }
        fi(i, 0, q) {
            int u, w; cin >> u >> w; --u; --w;
            printf(" %.6lf", time1[u][w]);
        }
    }
};

/**
void solve1() {
    int n, q; cin >> n >> q;
    vector<double> v(n);
    vector<ll> e(n); fi(i, 0, n)cin >> e[i]>>v[i];
    vvi d(n, vi(n)); fi(i, 0, n) fi(j, 0, n) cin>>d[i][j];
    vector<ll> ac; ac.push_back(0); fi(i, 0, n - 1) ac.push_back(ac.back()+d[i][i+1]);
    int u, w; cin >> u >> w;
    vector<double> tm(n, 0);
    fde(i, n - 2, 0) {
        double t = d[i][i + 1] + tm[i+1];
        fi(j, i + 1, n) {
            ll delta = ac[j] - ac[i];
            if (e[i] <delta) break;
            t = min(t, delta/v[i] + tm[j]);
        }
        tm[i] = t;
    }

    printf(" %.6lf\n",tm[0]);
}*/

int main()
{
    freopen(INP_FILE, "r", stdin);
    freopen(OUT_FILE, "w", stdout);
    int tstCnt; cin >> tstCnt;
    for (int tst = 1; tst <= tstCnt; tst++)
    {
        printf("Case #%d:", tst);
        Solution s; s.solve(); printf("\n");
        //solve1();
    }

    return 0;
}