#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stack>
#include <functional>
#include <set>
#include <queue>
#include <string>
#include <map>
#include <iomanip>
#include <cassert>

using namespace std;

#define mp make_pair
#define sqr(x) ((x)*(x))

typedef long long i64;

int main() {

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; test++)
    {
        cout << "Case #" << test << ": ";

        vector<string> names = { "R", "O", "Y", "G", "B", "V" };

        int n, r, o, y, g, b, v;
        vector<int> colors(6);
        cin >> n;

        for (int i = 0; i < 6; i++)
        {
            cin >> colors[i];
        }

        string ans;
        bool impos = false;
        int prev = -1;
        for (int i = 0; i < n; i++)
        {
            int idx = -1;
            for (int j = 0; j < 6; j++)
            {
                if (colors[j] > 0 && j != prev)
                    idx = j;
            }
            if (idx == -1)
            {
                ans = "IMPOSSIBLE";
                impos = true;
                break;
            }
            for (int j = 0; j < 6; j++)
            {
                if (colors[j] > 0 && colors[j] > colors[idx] && j != prev)
                    idx = j;
            }
            colors[idx]--;
            prev = idx;
            ans += names[idx];
        }

        if (impos) {
            cout << ans << endl;
            continue;
        }

        for (int i = 1; i < n; i++)
        {
            if (ans[i] == ans[i - 1])
            {
                ans = "IMPOSSIBLE";
                impos = true;
                break;
            }
        }

        if (impos) {
            cout << ans << endl;
            continue;
        }

        if (ans[0] == ans[n - 1])
        {
            bool art = false;
            for (int i = 1; i < n - 1; i++)
            {
                if (ans[i] != ans[0] && (i == n - 2 || ans[i] != ans[n - 2]))
                    if (i - 1 == n - 1 || ans[i - 1] != ans[n - 1])
                        if (i + 1 == n - 1 || ans[i + 1] != ans[n - 1])
                        {
                            swap(ans[i], ans[n - 1]);
                            art = true;
                            break;
                        }
            }
            if (!art) ans = "IMPOSSIBLE";
        }


        cout << ans << endl;
    }
}