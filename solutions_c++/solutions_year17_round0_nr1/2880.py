#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <deque>

using namespace std;

int t;

int main()
{
    ifstream cin("A-large.in");
    ofstream cout("A-small-attempt2.out");
    ios_base::sync_with_stdio(false), cin.tie(nullptr);

    cin >> t;
    for (int num = 0; num < t; num++)
    {
        string s;
        int k, n, ans = 0;
        bool open = false;
        deque <int> d;

        cin >> s >> k;
        n = s.size();
        cout << "Case #" << num + 1 << ": ";

        for (int i = 0; i < n; i++)
        {
            while (!d.empty() && d.front() == i)
            {
                open ^= true;
                d.pop_front();
            }

            if ((s[i] == '-' && !open) || (s[i] == '+' && open))
            {
                if (n - i < k)
                {
                    cout << "IMPOSSIBLE\n";
                    break;
                }

                ans++;
                open ^= true;
                d.push_back(i + k);
            }

            if (i == n - 1)
                cout << ans << '\n';
        }
    }
    return 0;
}
