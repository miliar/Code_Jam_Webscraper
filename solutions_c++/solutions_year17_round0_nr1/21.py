#include<bits/stdc++.h>
#define FOR(i,a,b) for (int i=(a),_b=(b);i<=_b;i=i+1)
#define FORD(i,b,a) for (int i=(b),_a=(a);i>=_a;i=i-1)
#define REP(i,n) for (int i=0,_n=(n);i<_n;i=i+1)
#define FORE(i,v) for (__typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
#define ALL(v) (v).begin(),(v).end()
#define fi   first
#define se   second
#define MASK(i) (1LL<<(i))
#define BIT(x,i) (((x)>>(i))&1)
#define div   ___div
#define next   ___next
#define prev   ___prev
#define left   ___left
#define right   ___right
#define __builtin_popcount __builtin_popcountll
using namespace std;
template<class X,class Y>
    void minimize(X &x,const Y &y) {
        if (x>y) x=y;
    }
template<class X,class Y>
    void maximize(X &x,const Y &y) {
        if (x<y) x=y;
    }
template<class T>
    T Abs(const T &x) {
        return (x<0?-x:x);
    }

/* Author: Van Hanh Pham */

/** END OF TEMPLATE - ACTUAL SOLUTION COMES HERE **/

const string NO_ANSWER = "IMPOSSIBLE";

int solve(string s, int k) {
    int n = s.size();
    int res = 0;
    REP(i, n - k + 1) if (s[i] == '-') {
        res++;
        REP(j, k) s[i + j] ^= '+' ^ '-';
    }
    FORE(it, s) if (*it == '-') return -1;
    return res;
}

int main(void) {
    int t; cin >> t;
    REP(love, t) {
        string s; int k; cin >> s >> k;
        printf("Case #%d: ", love + 1);
        if (solve(s, k) < 0) printf("%s\n", NO_ANSWER.c_str()); else printf("%d\n", solve(s, k));
    }
    return 0;
}

/*** LOOK AT MY CODE. MY CODE IS AMAZING :D ***/
