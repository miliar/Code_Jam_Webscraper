#include <bits/stdc++.h>
using namespace std;
#pragma GCC diagnostic ignored "-Wmissing-declarations"

#define FINAL_OUT(x) {cout << (x) << '\n'; exit(0);}


void solve(int numtest)
{
    long long n,k;
    cin >> n >> k;

    map<long long, long long> cnt = {{n, 1}};

    for(;;)
    {
        auto it = cnt.end();
        --it;
        long long len = it->first;
        if (k <= it->second)
        {
            cout << "Case #" << numtest << ": " << len / 2 << ' ' << (len - 1) / 2 << '\n';
            return;
        }

        k -= it->second;
        cnt[len / 2] += it->second;
        cnt[(len - 1) / 2] += it->second;
        cnt.erase(it);
    }

}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    ios_base::sync_with_stdio(false);

    //cout << fixed << setprecision(10);

    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i)
        solve(i);
}
