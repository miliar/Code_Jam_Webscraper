#include <bits/stdc++.h>
using namespace std;

using pii = pair<int,int>;
using ll = long long;
#define rep(i, j) for(int i=0; i < (int)(j); i++)
#define repeat(i, j, k) for(int i = (j); i < (int)(k); i++)
#define all(v) v.begin(),v.end()
#define debug(x) cerr << #x << " : " << x << endl

template<class T> bool set_min(T &a, const T &b) { return a > b  ? a = b, true : false; }
template<class T> bool set_max(T &a, const T &b) { return a < b  ? a = b, true : false; }
// vector
template<class T> istream& operator >> (istream &is , vector<T> &v) { for(T &a : v) is >> a; return is; }
template<class T> ostream& operator << (ostream &os , const vector<T> &v) { for(const T &t : v) os << "\t" << t; return os << endl; }
// pair
template<class T, class U> ostream& operator << (ostream &os , const pair<T, U> &v) { return os << "<" << v.first << ", " << v.second << ">"; }

const int INF = 1 << 30;
const ll INFL = 1LL << 60;


class Solver {
  public:
    bool solve(int T) {
        int D, N; cin >> D >> N;        
        vector<ll> K(N), S(N);
        rep(i, N) cin >> K[i] >> S[i];

        double last_time = -1;
        rep(i, N) {
            set_max(last_time, (double)(D - K[i]) / S[i]);
        }
        printf("Case #%d: %.9lf\n",T + 1,  D / last_time);
        return 0;
    }
};

int main() {
    int T; cin >> T;
    rep(i, T) {
        Solver s;
        s.solve(i);
    }
    return 0;
}

