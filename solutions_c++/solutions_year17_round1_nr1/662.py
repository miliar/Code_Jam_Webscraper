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

void colorString(string& s) {
    int n = s.size();
    rep(i, n - 1) {
        if (s[i + 1] == '?') s[i + 1] = s[i];
    }
    reverse(all(s));
    rep(i, n - 1) {
        if (s[i + 1] == '?') s[i + 1] = s[i];
    }
    reverse(all(s));
}

vector<string> transpose(vector<string> s) {
    int n = s.size();
    int m = s[0].size();
    vector<string> t(m, string(n, '?'));
    rep(i, n) {
        rep(j, m) {
            t[j][i] = s[i][j];
        }
    }
    return t;
}

signed main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    int T;
    cin >> T;
    rep(testcase, T) {
        int H, W;
        cin >> H >> W;
        vector<string> s(H);
        rep(i, H) cin >> s[i];
        rep(i, H) {
            colorString(s[i]);
        }
        s = transpose(s);
        rep(j, W) {
            colorString(s[j]);
        }
        s = transpose(s);
        cout << "Case #" << testcase + 1 << ":" << endl;
        rep(i, H) cout << s[i] << endl;
    }
}
