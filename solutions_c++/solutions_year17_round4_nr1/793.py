// another fine solution by misof
// #includes {{{
#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

#include <cassert>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <cmath>
#include <complex>
using namespace std;
// }}}

/////////////////// PRE-WRITTEN CODE FOLLOWS, LOOK DOWN FOR THE SOLUTION ////////////////////////////////

// pre-written code {{{
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

int N, P;
map< vector<int>, int > memo;

int solve(const vector<int> &zvysky) {
    if (memo.count(zvysky)) return memo[zvysky];
    int &res = memo[zvysky];
    res = 0;
    if (zvysky != vector<int>(P,0)) res = 1;
    vector<int> to = zvysky;
    // vsetky dvojice, trojice, stvorice
    for (int a=1; a<P; ++a) for (int b=a; b<P; ++b) if ((a+b)%P == 0) {
        bool ok = true;
        for (int x : {a,b}) { --to[x]; if (to[x] < 0) ok = false; }
        if (ok) res = max( res, 1 + solve(to) );
        for (int x : {a,b}) ++to[x];
    }
    for (int a=1; a<P; ++a) for (int b=a; b<P; ++b) for (int c=b; c<P; ++c) if ((a+b+c)%P == 0) {
        bool ok = true;
        for (int x : {a,b,c}) { --to[x]; if (to[x] < 0) ok = false; }
        if (ok) res = max( res, 1 + solve(to) );
        for (int x : {a,b,c}) ++to[x];
    }
    for (int a=1; a<P; ++a) for (int b=a; b<P; ++b) for (int c=b; c<P; ++c) for (int d=c; d<P; ++d) if ((a+b+c+d)%P == 0) {
        bool ok = true;
        for (int x : {a,b,c,d}) { --to[x]; if (to[x] < 0) ok = false; }
        if (ok) res = max( res, 1 + solve(to) );
        for (int x : {a,b,c,d}) ++to[x];
    }
    return res;
}

int main() {
    int T;
    cin >> T;
    for (int t=1; t<=T; ++t) {
        cin >> N >> P;
        vector<int> zvysky(P,0);
        for (int n=0; n<N; ++n) {
            int g; cin >> g;
            ++zvysky[g%P];
        }
        int answer = zvysky[0];
        zvysky[0] = 0;
        memo.clear();
        answer += solve(zvysky);
        cout << "Case #" << t << ": " << answer << endl;
    }

}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
