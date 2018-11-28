#include <iostream>
#include <queue>

using namespace std;
typedef long long ll;

ll solve (ll n) {
    string s = to_string(n);

    s += 127;
    int pos = 0;
    for (int i = 0; i < (int)s.size(); ++i) {
        if (s[pos] > s[i])
            break;
        if (s[pos] < s[i])
            pos = i;
    }
    s.pop_back();

    if (pos < (int)s.size()) {
        s[pos]--;
        for (int i = pos + 1; i < (int)s.size(); ++i) {
            s[i] = '9';
        }
    }

    return strtoll(s.c_str(), nullptr, 10);
}


int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;

    for (int i = 1; i <= t; ++i) {
        ll n;
        cin >> n;
        cout << "Case #" << i << ": " << solve(n) << "\n";
    }

    return 0;
}
