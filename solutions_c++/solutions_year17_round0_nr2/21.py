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

#define NUM_DIGIT   25
long long f[NUM_DIGIT + 3][10][2];

long long countNumber(long long n) {
    int digits[NUM_DIGIT];
    REP(i, NUM_DIGIT) {
        digits[i] = n % 10;
        n /= 10;
    }

    memset(f, 0, sizeof f);
    f[0][9][1] = 1;
    REP(i, NUM_DIGIT) REP(j, 10) REP(k, 2) if (f[i][j][k] > 0)
        REP(t, j + 1) {
            int newK = t != digits[i] ? t < digits[i] : k;
            f[i + 1][t][newK] += f[i][j][k];
        }

    long long res = 0;
    REP(i, 10) res += f[NUM_DIGIT][i][1];
    return res;
}

long long solve(long long n) {
    long long cnt = countNumber(n);
    long long L = 0;
    long long R = n;

    while (true) {
        if (L == R) return L;
        if (R - L == 1) return countNumber(L) >= cnt ? L : R;
        long long M = (L + R) >> 1;
        if (countNumber(M) >= cnt) R = M; else L = M + 1;
    }
}

int main(void) {
    int t; cin >> t;
    REP(love, t) {
        long long n; cin >> n;
        printf("Case #%d: %lld\n", love + 1, solve(n));
    }
    return 0;
}

/*** LOOK AT MY CODE. MY CODE IS AMAZING :D ***/
