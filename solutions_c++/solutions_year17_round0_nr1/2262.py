#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <cstring>

#define ll long long
#define f first
#define s second
#define INF (int)(1e9 + 7)
#define EPS (1e-6)
#define pb push_back
#define mp make_pair

using namespace std;
int m, n, ans, k;
bool was;
string s;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        cin >> s >> k;

        m = s.length();
        was = false;
        ans = 0;
        for (int j = 0; j < m; j++)
        {
            if (s[j] == '-')
            {
                //cout << j << "!!!" << endl;
                if (j + k - 1 >= m)
                {
                    was = true;
                    break;
                }
                ans++;
                for (int g = j; g < j + k; g++)
                    if (s[g] == '-')
                        s[g] = '+';
                    else
                        s[g] = '-';
            }
        }

        for (int j = 0; j < m; j++)
            if (s[j] == '-')
                was = true;

        //cout << s << endl;
        if (was == false)
        {
            cout << "Case #" << i << ": " << ans << endl;
        }
        else
            cout << "Case #" << i << ": IMPOSSIBLE" << endl;

    }

    return 0;
}
