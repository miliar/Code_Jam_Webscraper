#include <iostream>
#include <cmath>

#define MAX_T 100
using namespace std;

long long n, k;

void init()
{
    cin >> n >> k;
}

void solve()
{
    long long depth = (long long )floor(log2(k));
    long long n_remain = n - (1 << depth) + 1;
    long long k_remain = k - (1 << depth) + 1;
    long long total_partition = 1 << depth;
    long long value = n_remain / total_partition;
    if (k_remain <= (n_remain % total_partition))
        value++;
    cout << value / 2 << ' ' << (value - 1) / 2;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        init();
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
