#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>

#define debug(x) (cerr << #x << ": " << (x) << endl)

typedef long long ll;
typedef boost::multiprecision::checked_cpp_int bigint;

using namespace std;

void flip(char& c)
{
    if (c == '-') c = '+';
    else c = '-';
}

void solve(int)
{
    string s;
    int k;
    cin >> s >> k;
    int cnt = 0;
    for (int i = 0; i < s.size(); ++i) {
        char c = s[i];
        if (c == '-') {
            if (i + k > s.size()) {
                cout << "IMPOSSIBLE\n";
                return;
            }
            ++cnt;
            for (int j = i; j < i + k; ++j) {
                flip(s[j]);
            }
        }
    }
    cout << cnt << "\n";
}

int32_t main()
{
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        solve(i);
    }
}
