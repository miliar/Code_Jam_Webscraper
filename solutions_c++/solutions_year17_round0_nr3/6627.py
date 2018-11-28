#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>

using namespace std;

int n;
vector <bool> s;
vector <int> sl, smax, smin, sr;

int main()
{
    bool smin_unique;
    int choice, i, j, k, l, pos_max, pos_min, r, s_max, s_min, t, x, y, z;
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    cin >> t;
    for (x = 1; x <= t; x++)
    {
        cin >> n; cin >> k;

        s.resize(n + 2); s[0] = true; s[n + 1] = true;
        for (i = 1; i <= n; i++) s[i] = false;
        sl.resize(n + 2); smax.resize(n + 2); smin.resize(n + 2); sr.resize(n + 2);

        for (i = 0; i < k; i++)
        {
            l = -1;
            for (j = 1; j <= n; j++)
            {
                if (s[j]) l = -1;
                else l++;
                sl[j] = l;
            }
            r = -1;
            for (j = n; j >= 1; j--)
            {
                if (s[j]) r = -1;
                else r++;
                sr[j] = r;
            }
            for (j = 1; j <= n; j++)
            {
                if (!s[j])
                {
                    l = sl[j]; r = sr[j];
                    if (l > r) { smax[j] = l; smin[j] = r; }
                    else { smax[j] = r; smin[j] = l; }
                }
            }
            s_max = -1; s_min = -1; choice = -1;
            for (j = 1; j <= n; j++)
            {
                if (!s[j])
                {
                    if (smin[j] > s_min) { s_min = smin[j]; pos_min = j; smin_unique = true; }
                    if (smin[j] == s_min) smin_unique = false;
                }
            }
            if (smin_unique) {
                choice = pos_min;
                s_max = smax[j];
            }
            else {
                for (j = 1; j <= n; j++)
                {
                    if ((!s[j]) && (smin[j] == s_min))
                    {
                        if (smax[j] > s_max) { s_max = smax[j]; pos_max = j; }
                    }
                }
                choice = pos_max;
            }
            s[choice] = true;
        }
        y = s_max; z = s_min;

        //display results
        cout << "Case #" << x << ": " << y << " " << z << endl;
    }
    return 0;
}
