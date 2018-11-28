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
void solve(){
    ll n, k;
    cin >> n >> k;
    priority_queue<pll> pq;
    pq.emplace(n, 1);
    while (1){
        pll p = pq.top(); pq.pop();
        while (!pq.empty() && pq.top().X == p.X) {
            p.Y += pq.top().Y;
            pq.pop();
        }
        ll y = p.X / 2, z = (p.X - 1) / 2;
        if (p.Y >= k) {
            cout << y << ' ' << z << endl;
            return;
        }
        k -= p.Y;
        if (y) pq.emplace(y, p.Y);
        if (z) pq.emplace(z, p.Y);
    }
}

int main(){
    std::ios_base::sync_with_stdio(false); cin.tie(0);
    int tc; cin >> tc;
    for (int cs = 1; cs <= tc; cs++){
        cout << "Case #" << cs << ": ";
        solve();
    }


}
