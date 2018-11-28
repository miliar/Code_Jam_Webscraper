#include <iostream>
#include <cstdlib>
#include <set>
#include <map>
using namespace std;

void solve()
{
    long long n, k;
    cin >> n >> k;
    set<long long> s;
    s.insert(n);
    map<long long, long long> cnt;
    cnt[n] = 1;

    while (true)
    {
        auto ritr = s.rbegin();
        long long t = *ritr;
        s.erase(t);
        long long left = (t-1)/2;
        long long right = t/2;
        long long num = cnt[t];
        if (k <= num)
        {
            cout << right << " " << left << endl;
            return;
        }
        if (left != 0)
        {
            s.insert(left);
            cnt[left] += num;
        }
        if (right != 0)
        {
            s.insert(right);
            cnt[right] += num;
        }
        k -= num;
    }
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
