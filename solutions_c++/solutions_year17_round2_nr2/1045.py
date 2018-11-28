#include <bits/stdc++.h>

#define ll long long

using namespace std;

void solve(int test_number) {
    string ans = "";
    vector<int> v(6);
    vector<string> c = {"R", "O", "Y", "G", "B", "V"};
//    r - 0
//    o - 1
//    y - 2
//    g - 3
//    b - 4
//    v - 5
    int n;
    cin >> n >> v[0] >> v[1] >> v[2] >> v[3] >> v[4] >> v[5];

    int start, real_start;
    if (v[0] >= v[2] && v[0] >= v[4])
        start = 0;
    else if (v[2] >= v[0] && v[2] >= v[4])
        start = 2;
    else
        start = 4;
    real_start = start;

    while (v[start] > 0) {
        ans += c[start];
        --v[start];
        if (start == 0) {
            if (real_start == 4) {
                if (v[2] > v[4])
                    start = 2;
                else
                    start = 4;
            } else {
                if (v[2] >= v[4])
                    start = 2;
                else
                    start = 4;
            }
        } else if (start == 2) {
            if (real_start == 4) {
                if (v[0] > v[4])
                    start = 0;
                else
                    start = 4;
            } else {
                if (v[0] >= v[4])
                    start = 0;
                else
                    start = 4;
            }
        } else {
            if (real_start == 2) {
                if (v[0] > v[2])
                    start = 0;
                else
                    start = 2;
            } else {
                if (v[0] >= v[2])
                    start = 0;
                else
                    start = 2;
            }
        }
    }
    for (int i=0; i<6; ++i)
        if (v[i] > 0)
            ans = "IMPOSSIBLE";
    if (ans[0] == ans[n-1])
        ans = "IMPOSSIBLE";

    cout << "Case #" << test_number << ": " << ans << endl;
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t=1; t<=T; ++t)
        solve(t);

    return 0;
}
