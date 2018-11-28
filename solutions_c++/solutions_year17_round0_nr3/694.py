#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
ll n, k;

void go(ll n) {
    n --;
    cout << n-n/2 << " " << n/2 << endl;
}

int main() {
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int T;
    cin >> T;
    for(int kase = 1; kase <= T; kase ++) {
        cin >> n >> k;
        printf("Case #%d: ", kase);
        ll cur = 0;
        map<ll, ll> M;
        M[n] = 1;
        while(1) {
            ll sum = 0;
            for(auto& i : M) sum += i.second;
            if(cur + sum >= k) {
                vector<pair<ll, ll>> tmp;
                for(auto&i : M) {
                    tmp.push_back(make_pair(i.first, i.second));
                }
                reverse(tmp.begin(), tmp.end());
                if(cur + tmp[0].second >= k) {
                    go(tmp[0].first);
                } else {
                    go(tmp[1].first);
                }
                break;
            }
            map<ll, ll> MM;
            sum = 0;
            for(auto& i : M) {
                ll nn = i.first;
                nn --;
                MM[nn/2] += i.second;
                MM[nn-nn/2] += i.second;
                sum += i.second;
            }
            cur += sum;
            M = MM;
        }

    }

    return 0;
}
