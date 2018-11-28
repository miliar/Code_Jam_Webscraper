#include <algorithm>
#include <iostream>
#include <cstdio>
#include <string.h>
#include <vector>
#include <set>

using namespace std;

set <pair<pair<long long, long long>, long long>> s;

void add(long long L, long long R)
{
    if (L == R) return;

    long long x  = (L + R) / 2;
    long long ls = x - L - 1;
    long long rs = R - x - 1;

    s.insert({{-ls, -rs}, x});
}

void solve()
{
    int n, k;
    cin >> n >> k;

    s.clear();

    add(0, n + 1);

    long long x, ls, rs;
    for (int i = 0; i < k; i++) {
        x = s.begin() -> second;
        ls = -(s.begin() -> first.first);
        rs = -(s.begin() -> first.second);
        s.erase(s.begin());

        add(x - ls - 1, x);
        add(x, x + rs + 1);
    }

    cout << max(ls, rs) << " " << min(ls, rs) << "\n";
}

int main()
{
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int cntTests;
    cin >> cntTests;
    for (int numTest = 1; numTest <= cntTests; numTest++) {
        cout << "Case #" << numTest << ": ";
        solve();
    }
}
