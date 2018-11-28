#include <bits/stdc++.h>

using namespace std;

typedef long long ll;


void solve(int case_number) {
    int n, k;
    cin >> n >> k;
    vector<int> v(n+2, 0);
    v[0] = 1;
    v[n+1] = 1;

    int mn, mx, l, r, pos;
    for (int _=0; _<k; ++_) {
        mn = -1;
        mx = -1;
        pos = -1;
        l = 0;
        r = 1;
        while (v[r] == 0)
            ++r;

        for (int i=1; i<n+2; ++i) {
            if (v[i] == 1) {
                l = i;
                ++r;
                while (v[r] == 0)
                    ++r;
            } else if (mn < min(i-l-1, r-i-1)) {
                mn = min(i-l-1, r-i-1);
                mx = max(i-l-1, r-i-1);
                pos = i;
            } else if (mn == min(i-l-1, r-i-1) && mx < max(i-l-1, r-i-1)) {
                mn = min(i-l-1, r-i-1);
                mx = max(i-l-1, r-i-1);
                pos = i;
            }
        }

        v[pos] = 1;
    }

    cout << "Case #" << case_number << ": " << mx << " " << mn << endl;
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;

    for (int t=1; t<=T; ++t) {
        solve(t);
    }


    return 0;
}

