#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>

#define debug(x) (cerr << #x << ": " << (x) << endl)

typedef long long ll;
typedef boost::multiprecision::checked_cpp_int bigint;

using namespace std;

void solve(int)
{
    int n, p;
    cin >> n >> p;
    vector<int> s(n);
    vector<int> cnt(p, 0);
    for (int& i: s) {
        cin >> i;
        i %= p;
        ++cnt[i];
    }

    int result = cnt[0];
    cnt[0] = 0;

    if (p == 2) {
        result += (cnt[1] + 1) / 2;
    } else if (p == 3) {
        int t = min(cnt[1], cnt[2]);
        result += t;
        cnt[1] -= t;
        cnt[2] -= t;
        result += (cnt[1] + cnt[2] + 2) / 3;
    } else if (p == 4) {
        int t = min(cnt[1], cnt[3]);
        result += t;
        cnt[1] -= t;
        cnt[3] -= t;
        t = cnt[2] / 2;
        result += t;
        cnt[2] -= 2 * t;
        for (int i: {1, 3}) {
            if (cnt[2] && cnt[i] >= 2) {
                ++result;
                cnt[2] = 0;
                cnt[i] -= 2;
            }
        }
        result += (cnt[1] + cnt[3]) / 4;
        result += ((cnt[1] + cnt[3]) % 4) + cnt[2] > 0;
    } else assert(false);

    cout << result << endl;
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
