#include <iostream>
#include <map>


using namespace std;


pair<long long, long long> div(long long n)
{
    return {n / 2, (n - 1) / 2};
}


pair<long long, long long> solve()
{
    long long n, k;
    cin >> n >> k;
    map<long long, long long> kek;
    kek[n] = 1;
    long long t = 0;
    long long last = n;

    while (t < k)
    {
        pair<long long, long long> pll = div(kek.rbegin()->first);
        kek[pll.first] += kek.rbegin()->second;
        kek[pll.second] += kek.rbegin()->second;
        t += kek.rbegin()->second;
        last = kek.rbegin()->first;
        kek.erase(kek.rbegin()->first);
    }
    return div(last);
}


int main()
{
    freopen("C.in", "r", stdin);
    freopen("Cf.out", "w", stdout);
    int n;
    cin >> n;
    for (int ncase = 1; ncase <= n; ++ncase)
    {
        pair<long long, long long> ans = solve();
        cout << "Case #" << ncase << ": " << ans.first << ' ' << ans.second << endl;
        cerr << "Case #" << ncase << ": " << ans.first << ' ' << ans.second << endl;
    }
}