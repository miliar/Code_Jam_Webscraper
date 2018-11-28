// Enjoy your stay. Code by evima on 2017/04/08

#include <bits/stdc++.h>

#define LOOPVAR_TYPE long

#define all(x) (x).begin(), (x).end()
#define sz(x) ((LOOPVAR_TYPE)(x).size())
#define foreach(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)
#define GET_MACRO(_1, _2, _3, NAME, ...) NAME
#define _rep(i, n) _rep2(i, 0, n)
#define _rep2(i, a, b) for(LOOPVAR_TYPE i = (LOOPVAR_TYPE)(a); i < (LOOPVAR_TYPE)(b); i++)
#define rep(...) GET_MACRO(__VA_ARGS__, _rep2, _rep)(__VA_ARGS__)

#define fir first
#define sec second
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back

const double EPS = 1e-9;
const double PI = 3.141592653589793238462;
const long INF = 1070000000LL;
const long MOD = 1000000007LL;

using namespace std;

long N, K;

void solve(){
    cin >> N >> K;
    map<long, long> M;
    M[N] = 1;
    while(1){
        long l, c;
        tie(l, c) = *M.rbegin();
        M.erase(--M.end());
        if(K <= c){
            cout << l/2 << " " << (l-1)/2 << endl;
            return;
        }
        K -= c;
        M[l/2] += c;
        M[(l-1)/2] += c;
    }
}

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    rep(num, 1, T+1){
        cout << "Case #" << num << ": ";
        solve();
    }
}
