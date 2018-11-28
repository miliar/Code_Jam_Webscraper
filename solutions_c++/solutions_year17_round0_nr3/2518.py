#include <bits/stdc++.h>
#define INF 100000000000005
#define MAXN 2000
#define mod 1000000007
#pragma comment(lib, "user32")

using namespace std;

#define F first
#define S second
#define MP make_pair
#define all(x) (x).begin(), (x).end()

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

ll n, k;

int find_level(const ll& n) {
    ll kd = 1; int res = 1;
    while(true) {
        if(n <= kd) break;
        kd += (1ll << res);
        res += 1;
    }
    return res;
}

ll find_real_index(ll k, int level) {

    ll t = k - 1;
    ll x = (1ll << (level - 1) ), res = 1;
    for(int i = 0; i < level; ++i) {
        if(k % 2) {
            k -= t / 2;
            t = t / 2 + t % 2;
        }
        else {
            k -= (t / 2 + t % 2);
            t = t / 2;
            res += x;
        }
        x /= 2;
    }
    return res;
}

int main() {
        freopen("C-large.in", "r", stdin);
        freopen("outc.txt", "w", stdout);
        int t; cin >> t;

        for(int z = 0; z < t; ++z) {
                cin >> n >> k;
                int level = find_level(k);
                int main_level = find_level(n);
                if(level == main_level) {
                    cout << "Case #" << z + 1 << ": " << "0 0" << endl;
                    continue;
                }
                ll res = n;
                ll on_level = (1ll << (level - 1));


                ll pre_level = on_level - 1;
                ll t = on_level;

                k = find_real_index(k - pre_level, level-1);
                //cout << k << endl;
                //vector <char> vi;
                ll vich = on_level / 2;
                for(int i = 0; i < level-1; ++i) {
                    ll left_ = t / 2 + t % 2, right_ = t / 2;
                    if(left_ >= k) {
                        //vi.push_back('L');
                        res -= 1;
                        res = res / 2 + res % 2;
                        t = left_;
                    }
                    else {
                        //vi.push_back('R');
                        res -= 1;
                        res = res / 2;
                        t = right_;
                        k -= vich;
                    }
                    vich /= 2;
                }
                //for(int i = 0; i < vi.size(); ++i) cout << vi[i]; cout << endl;
                res -= 1;
                cout << "Case #" << z + 1 << ": " << max(res / 2, res / 2 + res % 2) << " " << min(res / 2, res / 2 + res % 2) << endl;
        }
}
