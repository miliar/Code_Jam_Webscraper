#include <bits/stdc++.h>
using namespace std;
typedef long long ll;




int main()
{
//    freopen("input.txt", "r", stdin);
//    freopen("output.txt", "w", stdin);

    int t;
    cin >> t;

    for (int i = 1; i <= t; i++) {
        int n, k;
        cin >> n >> k;

        map<int, int> mp;
        mp[n]++;

        int a, b;
        for (int i = 0; i < k; i++) {
            auto it = prev(mp.end());
            int mx = it->first;
            a = mx / 2, b = (mx - 1) / 2;
            if (it->second == 1)
                mp.erase(it);
            else
                it->second--;
            mp[a]++;
            mp[b]++;
        }
        cout << "Case #" << i << ": " << a << " " << b << endl;
    }
}