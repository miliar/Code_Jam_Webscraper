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

int f(int i, vector<int> &v) {
    return v[i - 1] + v[i] + v[i + 1];
}

int solo(int i, vector<int> &v) {
    bool v1 = v[i - 1] != 0, v2 = v[i] != 0, v3 = v[i + 1] != 0;
    return (v1 ^ v2 ^ v3) & !(v1 & v2 & v3);
}

int main(){
//#ifndef _DEBUG
    freopen("A-large.in", "r", stdin);
    freopen("test.out", "w", stdout);
//#endif
    //freopen("output.txt", "w", stdout);
//    ios_base::sync_with_stdio(false);
    
    int t;
    scanf("%d", &t);
    
    int d, n;
    for (int tt = 1; tt <= t; tt++) {
        scanf("%d%d", &d, &n);
        double maxt = 0;
        int p, v;
        for (int i = 0; i < n; i++) {
            scanf("%d%d", &p, &v);
            double lt = (d - p + .0) / v;
            if (lt + EPS > maxt) {
                maxt = lt;
            }
        }
        
        double res = d / maxt;
        
        printf("Case #%d: %.8lf\n", tt, res);
    }
    
    return 0;
}



