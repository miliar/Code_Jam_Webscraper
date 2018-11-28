#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T; cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cout << "Case #" << t << ": ";
        long long N, K; cin >> N >> K;

        map<long long,long long> mp;
        mp[N] = 1;
        long long it = N, tot = 0;
        while (it > 1)
        {
            tot += mp[it];
            if (tot >= K)
            {
                cout << it/2 << " " << (it-1)/2 << endl;
                break;
            }
            mp[it/2] += mp[it];
            mp[(it-1)/2] += mp[it];
            it = prev(mp.find(it))->first;
        }
        if (tot < K) cout << "0 0" << endl;
    }
}
