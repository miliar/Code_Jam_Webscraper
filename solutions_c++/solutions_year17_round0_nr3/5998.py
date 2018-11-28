#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<long long int, long long int> pii;
typedef vector<pii > vii;
typedef vector<vector<int> > vvi;
typedef vector<vector<pair<int, int> > > vvii;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define rep(i,s,e) for(int i=(s);i<(e);++i)
#define repr(i,s,e) for(int i=(e);i>(s);--i)

const ll MOD = 1e9+7;
const ll INF = 1e14;
const ll TE3 = 1005;
const ll TE5 = 100005;

auto cmp = [](pii l, pii r) {
    ll mid1 = (l.first + l.second)/2;
    ll mid2 = (r.first + r.second)/2;
    if(l.second-l.first == r.second-r.first) {
        return l.first > r.first;
    }
    if(mid1-l.first == mid2-r.first) {
        return l.second-mid1 < r.second-mid2;
    }
    return mid1-l.first < mid2-r.first;
};

int main() {
    ios::sync_with_stdio(false);
    int t;
    cin>>t;
    pii p;
    ll mid;
    unsigned long long int n, k;
    rep(i, 1, t+1) {
        cin>>n>>k;
        priority_queue <pii, vector<pii >, decltype(cmp)> q(cmp);
        q.push(mp(2, n+1));
        rep(j, 0, k) {
            p = q.top();
            q.pop();
            mid = (p.first + p.second)/2;
            if(mid-p.first >= 1)
                q.push(mp(p.first, mid-1));
            if(p.second-mid >= 1)
                q.push(mp(mid+1, p.second));
        }
        cout<<"Case #"<<i<<": "<<p.second-mid<<' '<<mid-p.first<<'\n';
    }
    return 0;
}