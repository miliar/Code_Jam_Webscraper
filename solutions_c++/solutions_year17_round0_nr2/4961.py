#include <bits/stdc++.h>
#define ll long long
#define int long long
#define F first
#define S second
using namespace std;

const int N = 1e5 + 10;

ll n, k, val;

void solve() {
    cin >> val;
    if(val <= 9) {
        cout << val << endl;
        return;
    }
    vector <int> v;
    int q = 0;
    while(val) {
        v.push_back(val % 10);
        val /= 10;
    }
    reverse(v.begin(), v.end());
    for(int i = 0; i < v.size() - 1; i++) {
        if(v[i] > v[i + 1]) {
            int idx = 0;
            for(int j = 0; j <= i; j++) {
                if(v[i] == v[j]) {
                    idx = j;
                    break;
                }
            }
            for(int j = idx + 1; j < v.size(); j++) {
                v[j] = 9;
            }
            v[idx]--;
            if(v[idx] == 0) {
                for(int i = 1; i < v.size(); i++) {
                    cout << 9;
                }
                cout << endl;
                return;
            }
            break;
        }
    }
    for(auto x: v) {
        cout << x;
    }
    cout << endl;
}

main() {
    ios_base::sync_with_stdio(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> n;
    for(int i = 1; i <= n; i++) {
        cout << "Case #" << i << ": ";
        solve();
    }
}
