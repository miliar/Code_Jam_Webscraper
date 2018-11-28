#include <bits/stdc++.h>
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
typedef long long ll;
typedef long double ld;
using namespace std;

int main() {
    //ios_base::sync_with_stdio(false)
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        ll n, k;
        cin >> n >> k;
        map<ll, ll> cnt;
        cnt[n] = 1;
        ll a = -1, b = -1;
        while(k > 0) {
            map<ll, ll> temp;
            auto it = cnt.end();
            do {
                --it;
                if(k - it->second <= 0) {
                    a = it->first / 2;
                    b = (it->first - 1) / 2;
                    break;
                }
                k -= it->second;
                temp[(it->first - 1) / 2] += it->second;
                temp[it->first / 2] += it->second;
            } while(it != cnt.begin());
            cnt = temp;
            if(a != -1)
                break;
        }
        cout << "Case " << "#" << t << ": ";
        cout << a << " " << b << "\n";
    }
    return 0;
}