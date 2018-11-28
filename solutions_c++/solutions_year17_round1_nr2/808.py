#pragma comment(linker, "/STACK:16777216")
#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <ctime>
#include <stack>
#include <algorithm>
#include <numeric>
#include <complex>
#include <functional>
#include <list>
#include <iostream>
using namespace std;

#define C(_a, _v) memset(_a,_v,sizeof(_a))
#define ALL(_obj) (_obj).begin(),(_obj).end()
#define FORB(_i,_a,_b) for((_i)=(_a);(_i)<(_b);++(_i))
#define FORE(_i,_a,_b) for((_i)=(_a);(_i)<=(_b);++(_i))
#define FOR(_i,_n) FORB(_i,0,_n)
#define FORS(_i,_obj) FOR(_i,(_obj).size())
#define ADJ(_i,_v) for((_i)=kick[_v];(_i)>=0;(_i)=foll[_i])
#define X first
#define Y second
#define I64 "%lld"
#define pb push_back
#define ppb pop_back
#define mp make_pair

typedef long long i64;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<i64, i64> pii64;
typedef vector<pii> vpii;

template<typename T>inline bool remin(T&c,const T&n){if(n<c){c=n;return 1;}return 0;}
template<typename T>inline bool remin2(T&c,const T&n){if(c<0||n<c){c=n;return 1;}return 0;}
template<typename T>inline bool remax(T&c,const T&n){if(c<n){c=n;return 1;}return 0;}
template<typename T>inline void addmod(T&c,const T&n,const T&m){c = (c + n) % m;}

int _in;int in(){scanf("%d",&_in);return _in;}

const double EPS = 1e-6;
const int INF = ~(1 << 31);
const i64 LINF = ~(1LL << 63);

#define sqr(x) (x)*(x)

// stuff cutline

bool diff(int a, int target) {
    double del = (1000 * a + 0.0) / target;
    if (del + EPS < 900.0 || del - EPS > 110.0) {
        return false;
    }
    return true;
}

pii lr(int a, int n) {
    int r = ((int)(a * 100.0 / 90.0)) / n;
    int l = (int)ceil(((int)ceil(a * 100.0 / 110.0) / (n + .0) ));
    return mp(l, r);
}

int finda(int a, vector<pii> &vp, int start) {
    int i = start;
    for (; i < vp.size(); i++) {
        if (a >= vp[i].X && a <= vp[i].Y) {
            break;
        }
        if (a < vp[i].X) {
            break;
        }
    }
    return i;
}



int main(){
//#ifndef _DEBUG
    freopen("B-large.in", "r", stdin);
    freopen("test.out", "w", stdout);
//#endif
    //freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    
    int t;
    cin >> t;
    int n, p;
    vector<int> quans;
    for (int q = 1; q <= t; q++) {
        cin >> n >> p;
        quans.assign(n, 0);
        for (int i = 0; i < n; i++) {
            cin >> quans[i];
        }
        vector<vector<int> > v(n, vector<int>(p, 0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                cin >> v[i][j];
            }
        }
        for (int i = 0; i < n; i++) {
            sort(v[i].begin(), v[i].end());
        }
        
        int maxq = 0;
        int minq = INF;
        vector<vector<pii> > vp(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                pii b = lr(v[i][j], quans[i]);
                if (b.X > b.Y) {
                    continue;
                }
                remax(maxq, b.Y);
                remin(minq, b.X);
                vp[i].pb(b);
//                cout << b.X << "," << b.Y << "; ";
            }
//            cout << "\n";
        }
        
        vector<int> pnt(n, 0);
        int ans = 0;
        bool stahp = false;
        for (int cnt = minq; cnt < maxq + 5; cnt++) {
            if (stahp) {
                break;
            }
            while (true) {
                int lfound = true;
                for (int i = 0; i < n; i++) {
                    pnt[i] = finda(cnt, vp[i], pnt[i]);
                    if (pnt[i] >= vp[i].size() || !(cnt <= vp[i][pnt[i]].Y && cnt >= vp[i][pnt[i]].X)) {
                        lfound = false;
                    }
                }
                if (!lfound) {
                    break;
                }
                ans++;
                for (int i = 0; i < n; i++) {
                    pnt[i]++;
                    if (pnt[i] == vp[i].size()) {
                        stahp = true;
                    }
                }
            }
        }
        
        cout << "Case #" << q << ": " << ans << "\n";
    }
    
    return 0;
}



