#include <bits/stdc++.h>

#define f(_i, _n) for (auto _i = 0; _i < _n; _i++)
#define F(_i, _k, _n) for (auto _i = _k; _i < _n; _i++)
#define fr(_i, _k, _n) for (auto _i = _k; _i < _n; _i++)
#define r(_t, _n)     _t _n;     cin >> _n;
#define ra(_type, _name, _len)_type _name[_len]; f(_i, _len)    cin >> _name[_len];
#define mp make_pair
#define re return
#define takedown re 0;
#define fi first
#define se second
#define in(_name) freopen(_name, "r", stdin);
#define out(_name) freopen(_name, "w", stdout);
#define err(_name) freopen(_name, "w", stderr);
#ifdef FairlyLocal
    #define deb cerr
#else
    #define deb GetCE :(
#endif
#define pb push_back
#define fill(_a, _n) memset(_a, _n, sizeof(_a))
#define all(_v) _v.begin(), _v.end()
#define vi std::vector<int>
using namespace std;
typedef pair<int,int> pii;
typedef long long ll;

#ifndef FairlyLocal
    // class fastio {
    // public:
    //     fastio() {
    //         ios::sync_with_stdio(false);
    //         cin.tie(nullptr);
    //     }
    // } __fastio;
#endif

int cnt[4];

void solve(int i){
    int n, c, m;
    int v[2];
    v[0] = v[1] = 0;
    int p[1005];
    f(i, 1005) p[i] = 0;
    cin >> n >> c >> m;
    f(i, m){
        int a, b;
        cin >> a >> b;
        --b;
        --a;
        v[b]++;
        p[a]++;
    }
    int mx = 0, mxp;
    f(i, n){
        if(mx < p[i]){
            mx = p[i];
            mxp = 0;
        }
    }
    // deb << i << " : " << v[0] << ' ' << v[1] << ' ' << mx << ' ' << p[0] << endl;
    if(v[0] < v[1]) swap(v[0], v[1]);
    if(v[0] >= p[0]){
        cout << "Case #" << i << ": " << v[0] << ' ' << max(0, mx-v[0]) << '\n';
    }
    else{
        cout << "Case #" << i << ": " << p[0] << ' ' << 0 << '\n';
    }
}

int main(){
//    #ifdef FairlyLocal
        in(".input");
        out(".output");
        err(".debug");
//    #endif
    int t;
    cin >> t;
    f(i, t){
        solve(i+1);
    }
}
