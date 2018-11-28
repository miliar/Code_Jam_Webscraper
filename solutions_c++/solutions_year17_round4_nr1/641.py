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
    f(i, 4) cnt[i] = 0;
    int n, p;
    cin >> n >> p;
    f(i, n){
        int a;
        cin >> a;
        cnt[a%p]++;
    }
    int cc = n;
    // deb << "case " << i <<' ' << n << ' ' <<  cnt[0] << ' ' << cnt[1] << ' ' << cnt[2] << ' ' << cnt[3] <<endl;
    if(p == 2){
        int ans = cnt[0] + (cnt[1]+1)/2;
        cout << "Case #" << i << ": " << ans << '\n';
        re;
    }
    if(p == 3){
        int ans = cnt[0];
        deb << i << ' ' << cnt[0] << ' ' << cnt[1] << ' ' << cnt[2] << ' ';
        int val = min(cnt[2], cnt[1]);
        ans+=val;
        cnt[2]-=val;
        cnt[1]-=val;
        ans+=cnt[1]/3;
        cnt[1]%=3;
        ans+=cnt[2]/3;
        cnt[2]%=3;
        if(cnt[1] > 0 || cnt[2] > 0 || cnt[3] > 0) ans++;
        // deb << ans << endl;
        cout << "Case #" << i << ": " << ans << '\n';
        re;
    }
    if(p == 4){
        int ans = cnt[0];
        cc-=cnt[0];
        ans+=cnt[2]/2;
        cc-=cnt[2]/2*2;
        cnt[2]%=2;
        int val = min(cnt[3], cnt[1]);
        ans+=val;
        cnt[3]-=val;
        cnt[1]-=val;
        if(cnt[1]>1 && cnt[2]>0){
            ans++;
            cnt[1]-=2;
            cnt[2]--;
            cc-=3;
        }
        if(cnt[2]>0 && cnt[3]>1){
            ans++;
            cnt[2]--;
            cnt[3]-=2;
            cc-=3;
        }
        ans+=cnt[1]/4;
        cnt[1]%=4;
        ans+=cnt[3]/4;
        cnt[3]%=4;
        if(cnt[1] > 0 || cnt[2] > 0 || cnt[3] > 0) ans++;
        cout << "Case #" << i << ": " << ans << '\n';
    }
}

int main(){
    #ifdef FairlyLocal
        in(".input");
        out(".output");
        err(".debug");
    #endif
    int t;
    cin >> t;
    f(i, t){
        solve(i+1);
    }
}
