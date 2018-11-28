#include <bits/stdc++.h>
using namespace std;
template <class T> int size(const T &x) { return x.size(); }
#define rep(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
const int INF = 2147483647;

int main() {
    int ts;
    cin >> ts;
    rep(t,0,ts) {
        cout << "Case #" << (t+1) << ": ";
        ll n, k;
        cin >> n >> k;
        priority_queue<ll> pq;
        map<ll,ll> cnt;
        cnt[n]++;
        pq.push(n);
        while (!pq.empty()) {
            ll cur = pq.top();
            pq.pop();
            if (cnt[cur] >= k) {
                cout << cur / 2 << " " << (cur - 1) / 2 << endl;
                break;
            }
            k -= cnt[cur];
            ll a = (cur - 1) / 2,
               b = cur - 1 - a;
            if (cnt.find(a) == cnt.end()) {
                pq.push(a);
            }
            cnt[a] += cnt[cur];
            if (cnt.find(b) == cnt.end()) {
                pq.push(b);
            }
            cnt[b] += cnt[cur];
            cnt[cur] = 0;
        }
    }



    return 0;
}

