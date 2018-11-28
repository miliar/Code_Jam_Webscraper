#include <bits/stdc++.h>
using namespace std;
typedef long long ll;


ll solve(ll n) {
    vector<int> v;
    while (n) {
        v.push_back(n % 10);
        n /= 10;
    }
    for (int i = 0; i < v.size() - 1; i++) {
        if (v[i] == -1) {
            v[i] = 9;
            v[i + 1]--;
        } else if (v[i] < v[i + 1]) {
            v[i + 1]--;
            for (int j = 0; j <= i; j++)
                v[j] = 9;
        }
    }
    reverse(v.begin(), v.end());
    for (ll i : v)
        n = n * 10 + i;
    return n;
}

int main()
{
//    freopen("input.txt", "r", stdin);
//    freopen("output.txt", "w", stdin);
    int t;
    cin >> t;

    for (int i = 1; i <= t; i++) {
        ll n;
        cin >> n;
        cout << "Case #" << i << ": " << solve(n) << endl;
    }
}