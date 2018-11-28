#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>

#define debug(x) (cerr << #x << ": " << (x) << endl)

typedef long long ll;
typedef boost::multiprecision::checked_cpp_int bigint;

using namespace std;

void solve(int)
{
    ll d, n;
    cin >> d >> n;
    double arrival_time = 0;
    for (int i = 0; i < n; ++i) {
        ll k, s;
        cin >> k >> s;
        ll dl = d - k;
        double at = dl / static_cast<double>(s);
        arrival_time = max(arrival_time, at);
    }

    cout << setprecision(30) << d / arrival_time << endl;
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
