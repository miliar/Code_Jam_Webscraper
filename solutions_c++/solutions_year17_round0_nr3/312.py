#include <iostream>
#include <map>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++)
    {
        long long n, k;
        cin >> n >> k;

        map<long long, long long> m;
        m[n] = 1;

        for (; m.rbegin()->second < k; )
        {
            long long s = m.rbegin()->first;
            long long x = m.rbegin()->second;
            m.erase(--m.end());
            m[(s - 1) / 2] += x;
            m[s / 2] += x;
            k -= x;
        }

        cout << "Case #" << tt << ": " << m.rbegin()->first / 2 << " " << (m.rbegin()->first - 1) / 2 << endl;
    }

    return 0;
}
