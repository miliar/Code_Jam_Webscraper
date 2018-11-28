#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll, ll> par;
#define len first
#define cnt second

struct segment {
  ll len, cnt;
  ll i;
};

ll a[5];
ll b[2];

vector<par> V;

void split(ll len) {
    V.clear();
    if (len == 0) return;
    V.push_back({len+1, 0});
    V.push_back({len, 1});
    for (ll i = 0; i < (ll)V.size(); i += 2) {
        ll n_len1 = V[i].len / 2, n_cnt1 = V[i].cnt;
        ll n_len2 = (V[i+1].len-1) / 2, n_cnt2 = V[i+1].cnt;
        V[i+1].len/2 == n_len1 ? n_cnt1 += V[i+1].cnt : n_cnt2 += V[i+1].cnt;
        (V[i].len-1)/2 == n_len1 ? n_cnt1 += V[i].cnt : n_cnt2 += V[i].cnt;
        if (n_len1 == 0 && n_len2 == 0) break;
        V.push_back({n_len1, n_cnt1});
        V.push_back({n_len2, n_cnt2});
    }
    while (V.size() && V.back().first == 0) V.pop_back();
    ll cnt1 = 0;
    while (V.size() && V.back().first == 1) {
        cnt1 += V.back().cnt;
        V.pop_back();
    }
    if (cnt1 > 0) V.push_back({1, cnt1});
}

pair<ll,ll> query(ll i, ll n_len, ll n_ind) {
    ll pos = a[i] + 1;
    ll len = a[i+1] - a[i] - 1;
    while (len > n_len) {
        split((len - 1) / 2);
        ll cnt = 0;
        for (auto &p: V)
        if (p.len == n_len) cnt += p.cnt;
        if (cnt >= n_ind) {
            len = (len - 1) / 2;
        }
        else {
            pos += 1 + (len - 1) / 2;
            len = len / 2;
            n_ind -= cnt;
        }
    }
    return make_pair(pos + (len-1)/2,len);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("C-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
    ll m, n, k, T;
    cin >> T;
    for (ll j = 1; j <= T; ++j){
        cin >> n >> k;
        cout << "Case #" << j << ": ";
        a[0] = 0, a[1] = n + 1;
        vector<segment> segments;
        split(n);
        for (auto &p: V)
            if (p.len > 0 && p.cnt > 0) segments.push_back({p.len, p.cnt, 0});
        sort(segments.begin(), segments.end(), [&] (const segment &a, const segment &b){if (a.len != b.len) return a.len > b.len;return a.i < b.i;});
        b[0] = k;
        ll q = 0;
        ll cur = 1;
        pair<ll,ll> p1,p2;
        for (segment &g: segments) {
            while (q < 1 && b[q] < cur + g.cnt) {
                if (q == 0) p1 = query(g.i, g.len, b[q] - cur + 1);
                q++;
            }
            cur += g.cnt;
        }
        cout << p1.second/2 << ' ' << (p1.second-1)/2 << '\n';
    }
    return 0;
}
