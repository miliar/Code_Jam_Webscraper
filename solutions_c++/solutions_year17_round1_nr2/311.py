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

typedef pair<ll, ll> pll;

bool isless(ll x, ll y){
    y = (y * 11) / 10;
    return x <= y;
}

bool ismore(ll x, ll y){
    y = ((y * 9) + 9) / 10;
    return x >= y;
}

pll range(ll pack, ll serve){
    pll ans;
    ll lo = 0, hi = INT_MAX;
    while (lo < hi) {
        ll mid = (lo + hi) / 2;
        if (ismore(pack, serve * mid)) lo = mid + 1;
        else hi = mid;
    }
    ans.X = lo - 1;
    lo = 0; hi = INT_MAX;
    while (lo < hi) {
        ll mid = (lo + hi) / 2;
        if (!isless(pack, serve * mid)) lo = mid + 1;
        else hi = mid;
    }
    ans.Y = lo;
    return ans;
}

int solve(){
    int n, m; cin >> n >> m;
    vector<ll> serve(n);
    for (int i = 0; i < n; i++) cin >> serve[i];
    vector<vector<ll>> arr(n, vector<ll>(m));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> arr[i][j];
    for (int i = 0; i < n; i++)
        sort(arr[i].begin(), arr[i].end());

    int res = 0;
    vi ptr(n, 0);
    for (;;) {
        ll mlo = LLONG_MAX, mhi = LLONG_MIN;
        for (int i = 0; i < n; i++){
            if (ptr[i] == m) return res;
            pll b = range(arr[i][ptr[i]], serve[i]);
            mlo = min(mlo, b.X);
            mhi = max(mhi, b.Y);
        }
        if (mlo >= mhi) {
            res++;
            for (int i = 0; i < n; i++) ptr[i]++;
        } else {
            for (int i = 0; i < n; i++){
                pll b = range(arr[i][ptr[i]], serve[i]);
                if (b.X < mhi)
                    ptr[i]++;
            }
        }
    }
    return res;
}


void test(){
    auto p = range(1500, 500);
    cout << p.X << ' ' << p.Y << endl;
    p = range(809, 300);
    cout << p.X << ' ' << p.Y << endl;

}

int main(){
    std::ios_base::sync_with_stdio(false); cin.tie(0);
    int tc; cin >> tc;
    for (int cs = 1; cs <= tc; cs++) {
        cout << "Case #" << cs << ": ";
        cout << solve() << endl;
    }

}
