#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>

#define debug(x) (cerr << #x << ": " << (x) << endl)

typedef long long ll;
typedef boost::multiprecision::checked_cpp_int bigint;

using namespace std;

void solve(int)
{
    string n;
    cin >> n;

    for (int i = n.size() - 2; i >= 0; --i) {
        if (n[i] > n[i + 1]) {
            n[i]--;
            assert(n[i] >= '0');
            for (int j = i + 1; j < n.size(); ++j) n[j] = '9';
        }
    }

    while (n.front() == '0') n = n.substr(1);

    cout << n << "\n";
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
