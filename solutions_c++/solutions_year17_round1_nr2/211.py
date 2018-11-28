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

ll need[100];
    // have[100][100];

bool cmp(const pair<ll,ll> &a, const pair<ll,ll> &b) {
    return a.second < b.second;
}

int main() {
    int ts;
    cin >> ts;
    rep(t,0,ts) {
        int n, p;
        cin >> n >> p;
        rep(i,0,n) {
            cin >> need[i];
        }
        vector<vector<pair<ll,ll> > > arr(n);
        rep(i,0,n) {
            rep(j,0,p) {
                ll x;
                cin >> x;
                ll mx = 100*x/90/need[i];
                ll mn = (100*x + (ll)need[i]*110 - 1)/((ll)need[i]*110);
                // k * need[i] * 90/100 <= x <= k * need[i] * 110/100
                // k * need[i] * 90/100 <= x <= k * need[i] * 110/100
                if (mn <= mx) {
                    arr[i].push_back(make_pair(mn,mx));
                }
                // cout << x << " " << need[i] << " " << mn << " " << mx << " " << mn*need[i] << " " << mx*need[i] << endl;
            }
        }
        rep(i,0,n) {
            sort(arr[i].begin(), arr[i].end(), cmp);
            // cout << size(arr[i]) << endl;
        }
        ll DINF = 1000000000000000000LL;
        int cnt = 0;
        while (true) {
            ll mn = DINF;
            rep(i,0,n) {
                iter(it,arr[i]) {
                    mn = min(mn, it->second);
                }
            }
            if (mn == DINF) {
                break;
            }
            bool all = true;
            rep(i,0,n) {
                bool any = false;
                iter(it,arr[i]) {
                    if (it->first <= mn && mn <= it->second) {
                        any = true;
                        break;
                    }
                }
                if (!any) {
                    all = false;
                    break;
                }
            }
            if (!all) {
                rep(i,0,n) {
                    iter(it,arr[i]) {
                        if (it->second == mn) {
                            arr[i].erase(it);
                            goto cont;
                        }
                    }
                }
cont:
                continue;
            } else {
                rep(i,0,n) {
                    iter(it,arr[i]) {
                        if (it->first <= mn && mn <= it->second) {
                            arr[i].erase(it);
                            break;
                        }
                    }
                }
                cnt++;
            }
        }
        cout << "Case #" << (t+1) << ": " << cnt << endl;
    }
    return 0;
}

