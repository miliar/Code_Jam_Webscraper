#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define all(c) (c).begin(), (c).end()
#define D(a) cerr << #a << "=" << a << endl;
#define pb push_back
#define eb emplace_back
#define mp make_pair

typedef long long int ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    int T; cin >> T;
    forn(cas,T) {
        cout << "Case #" << cas+1 << ": ";

        ll n,k; cin >> n >> k;
        map<ll,ll> cnt, ans; 
        cnt[n] = 1;
        while (!cnt.empty()) {
            auto it = cnt.rbegin();
            if (it->first == 0) break;
            ans[it->first] = it->second;
            cnt[it->first/2] += it->second;
            cnt[(it->first-1)/2] += it->second;
            cnt.erase(it->first);
        }

        ll last;
        for (;;) {
            auto it = ans.rbegin();
            if (k > it->second) k -= it->second;
            else {
                last = it->first;
                break;
            }
            ans.erase(it->first);
        }
        cout << (last/2) << ' ' << (last-1)/2 << endl;
    }

    return 0;
}
