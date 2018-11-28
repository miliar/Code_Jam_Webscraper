//
//  C.cpp
//  Minesweeper Master
//
//  Created by McKrisch on 12.04.13.
//

#include <iostream>
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <assert.h>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)



//#define TEST
#define SMALL

//#define COUT

#ifdef TEST
const char *kIn  = "C-test.in";
#else
#ifdef SMALL
const char *kIn  = "C-small.in";
const char *kOut = "C-small.out";
#else
const char *kIn  = "C-large.in";
const char *kOut = "C-large.out";
#endif
#endif

typedef set<int> cont;
typedef cont::iterator iter;
typedef cont::reverse_iterator riter;
typedef cont::const_iterator citer;
typedef cont::const_reverse_iterator criter;

struct Stall {
    int L, R, idx;
    Stall() :L(0),R(0),idx(-1) {}
    Stall(int _idx) :L(0),R(0),idx(_idx) {}
    
    void minMax() {
        int a = min(L, R);
        int b = max(L, R);
        L = a;
        R = b;
    }
    
    bool operator<(const Stall &o) const {
        if (L != o.L) return L > o.L;
        if (R != o.R) return R > o.R;
        return idx < o.idx;
    }
};

void calc(int N, int K) {
    vector<bool> A(N);
    rep (t, K) {
        vector<Stall> S;
        rep (i, N) {
            if (!A[i]) {
                Stall s(i);
                for (int j = i-1; j >= 0 && !A[j]; j--) s.L++;
                for (int j = i+1; j < N && !A[j]; j++) s.R++;
                s.minMax();
                S.push_back(s);
            }
        }
        sort(S.begin(), S.end());
        A[S[0].idx] = true;
        if (t == K-1) {
            cout << S[0].R << " " << S[0].L << endl;
        }
    }
}

void workCase() {
    int N, K;
    cin >> N >> K;
    calc(N, K);
}

int main(int argc, const char * argv[]) {
    if (!freopen(kIn, "rt", stdin)) {
        return 1;
    }
#if !defined(COUT) && !defined(TEST)
    if (!freopen(kOut, "wt", stdout)) {
        return 2;
    }
#endif
    int N;
    cin >> N;
    rep (i, N) {
        cout << "Case #" << i+1 << ": ";
        workCase();
    }
    return 0;
}
