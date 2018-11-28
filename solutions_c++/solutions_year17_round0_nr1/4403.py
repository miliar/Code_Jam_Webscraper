#include <stdio.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>

using namespace std;

string s;
long long n, t, k;

int main()
{
    freopen("/Users/aleksandra/Documents/problems/-/A-large.in", "r", stdin);
    freopen("/Users/aleksandra/Documents/problems/-/A-large.out", "w", stdout);
    cin >> t;

    for (int j = 0; j < t; ++j)
    {
        cin >> s;
        cin >> k;
        int ans = 0;

        for (int i = 0; i <= s.size() - k; ++i)
        {
            if (s[i] == '-')
            {
                ans++;
                for (int m = i; m < i + k; m++)
                {
                    if (s[m] == '-') s[m] = '+';
                    else s[m] = '-';
                }
            }
        }

        bool fl = false;
        for (int l = s.size() - k; l < s.size(); ++l) {
            if (s[l] == '-') fl = true;
        }
        if (fl) cout <<  "Case #" << j + 1 << ": IMPOSSIBLE"<< endl;
        else cout <<  "Case #" << j + 1 << ": " << ans << endl;


    }

}
