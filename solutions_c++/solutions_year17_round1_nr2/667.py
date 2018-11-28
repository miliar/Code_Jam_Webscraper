#include <bits/stdc++.h>
using namespace std;
#define int long long   // <-----!!!!!!!!!!!!!!!!!!!

#define rep(i,n) for (int i=0;i<(n);i++)
#define rep2(i,a,b) for (int i=(a);i<(b);i++)
#define rrep(i,n) for (int i=(n)-1;i>=0;i--)
#define rrep2(i,a,b) for (int i=(a)-1;i>=b;i--)
#define chmin(a,b) (a)=min((a),(b));
#define chmax(a,b) (a)=max((a),(b));
#define all(a) (a).begin(),(a).end()
#define rall(a) (a).rbegin(),(a).rend()
#define printV(v) cerr<<(#v)<<":";for(auto(x):(v)){cerr<<" "<<(x);}cerr<<endl;
#define printVS(vs) cerr<<(#vs)<<":"<<endl;for(auto(s):(vs)){cerr<<(s)<< endl;}
#define printVV(vv) cerr<<(#vv)<<":"<<endl;for(auto(v):(vv)){for(auto(x):(v)){cerr<<" "<<(x);}cerr<<endl;}
#define printP(p) cerr<<(#p)<<(p).first<<" "<<(p).second<<endl;
#define printVP(vp) cerr<<(#vp)<<":"<<endl;for(auto(p):(vp)){cerr<<(p).first<<" "<<(p).second<<endl;}

inline void output(){ cerr << endl; }
template<typename First, typename... Rest>
inline void output(const First& first, const Rest&... rest) {
    cerr << first << " "; output(rest...);
}

using ll = long long;
using Pii = pair<int, int>;
using TUPLE = tuple<int, int, int>;
using vi = vector<int>;
using vvi = vector<vi>;
using vvvi = vector<vvi>;
const int inf = 1ll << 60;
const int mod = 1e9 + 7;
using Graph = vector<vector<int>>;

signed main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    int NUM_TEST;
    cin >> NUM_TEST;
    rep(testcase, NUM_TEST) {
        int N, P;
        cin >> N >> P;
        vi r(N);
        rep(i, N) cin >> r[i];
        vvi q(N, vi(P));
        rep(i, N) rep(j, P) cin >> q[i][j];
        rep(i, N) sort(all(q[i]));

        vi itr(N);

        auto success3 = [&](int i, int k) {
            rep2(j, itr[i], P) {
                if (q[i][j] < 0.9 * k * r[i]) {
                    itr[i]++;
                }
                else if (q[i][j] > 1.1 * k * r[i]) {
                    return P;
                }
                else {
                    return j;
                }
            }
            return P;
        };

        auto success2 = [&](int k) {
            vi used(N);
            rep2(i, 1, N) {
                int j = success3(i, k);
                if (j == P) return vi();
                used[i] = j;
            }
            return used;
        };

        auto success = [&](int j0) {
            for (int k = ceil(q[0][j0] / (1.1 * r[0]));
                k <= q[0][j0] / (0.9 * r[0]);
                k++)
            {
                if (k > q[0][j0] / (0.9 * r[0])) continue;
                // output("j0 =", j0, "k =", k);
                auto used = success2(k);
                if (used.empty()) continue;
                rep2(i, 1, N) {
                    itr[i] = used[i] + 1;
                }
                return true;
            }
            return false;
        };

        int ans = 0;
        rep(j, P) if (success(j)) ans++;
        cout << "Case #" << testcase + 1 << ": " << ans << endl;
    }
}
