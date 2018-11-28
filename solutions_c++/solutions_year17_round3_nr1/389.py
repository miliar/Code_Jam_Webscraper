#include <iostream>
#include <set>
#include <cmath>
#include <algorithm>

using namespace std;

double solve()
{
    int n, k;
    cin >> n >> k;
    pair<long long, long long> all_cakes[n];
    for(int i = 0; i < n; i++)
    {
        long long r, h;
        cin >> r >> h;
        all_cakes[i].first = r * r;
        all_cakes[i].second = r * 2 * h;
    }
    sort(all_cakes, all_cakes + n);
    set<long long> k_cakes;
    long long cake_sum = 0;
    long long max_exp = 0;
    for(int i = 0; i + 1 < k; i++)
    {
        cake_sum += all_cakes[i].second;
        k_cakes.insert(all_cakes[i].second);
    }
    for(int i = k - 1; i < n; i++)
    {
        max_exp = max(max_exp, cake_sum + all_cakes[i].first + all_cakes[i].second);
        cake_sum += all_cakes[i].second;
        k_cakes.insert(all_cakes[i].second);
        cake_sum -= *k_cakes.begin();
        k_cakes.erase(k_cakes.begin());
    }
    return M_PI * max_exp;
}

int main()
{
    int n;
    cin >> n;
    cout.precision(15);
    for(int i = 1; i <= n; i++)
        cout << "Case #" << i << ": " << solve() << endl;
    return 0;
}
