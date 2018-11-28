#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#define F first
#define S second
#define PB push_back
typedef long long ll;
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);

    int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
        string S; cin >> S;
        vector<int> v(S.size());
        for (int i = 0; i < S.size(); ++i)
            v[i] = S[i] - '0';

        for (int i = v.size() - 1; i > 0; --i) {
            if (v[i-1] > v[i]) {
                --v[i-1];
                for (int j = i; j < v.size(); ++j) v[j] = 9;
            }
        }

        cout << "Case #" << t << ": ";
        for (auto x: v) if (x)
            cout << x;
        cout << '\n';
    }

    return 0;
}
