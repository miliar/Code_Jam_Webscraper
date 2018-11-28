#include <bits/stdc++.h>

using namespace std;
#define X first
#define Y second
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

#define debug(x) cerr << #x << " = " << (x) << endl;
template<typename T>
ostream& operator<<(ostream& o, vector<T>& v) {
    for (auto& x : v) o << x << ' ';
    return o;
}

int n, p;
map<vi, int> memo;
int dp(vi &v){
    if (memo.count(v)) return memo[v];
    int& res = memo[v];
    if (v[1] == n) return res = 0;
    res = 0;
    for (int i = 0; i < p; i++){
        if (v[2+i]){
            vi nv = v;
            nv[2+i]--;
            nv[0] = (((p - (i - v[0])) % p) + p) % p;
            nv[1]++;
            res = max(res, (v[0] == 0) + dp(nv));
        }
    }
    return res;
}
void solve(){
    cin >> n >> p;
    memo.clear();
    vi cnt(p, 0);
    for (int i = 0; i < n; i++){
        int d; cin >> d;
        cnt[d%p]++;
    }
    vi v = {0, 0};
    for (int i = 0; i < p; i++) v.push_back(cnt[i]);
    int res = dp(v);
    cout << res << endl;
}

int main(){
    std::ios_base::sync_with_stdio(false); cin.tie(0);
    int tc; cin >> tc;
    for (int cs = 1; cs <= tc; cs++){
        cout << "Case #" << cs << ": ";
        solve();
    }

}
