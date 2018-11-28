#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cassert>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define int long long

#undef int
int main()
{
#define int long long
    int t; cin >> t;
    for (int tt = 1; tt <= t; tt++)
    {
        cerr << "Executing Case #" << tt << "\n";
        string s; int k;
        cin >> s >> k;
        int n = s.size();
        int a[n];
        for (int i = 0; i < n; i++)
            a[i] = (s[i] == '-' ? 0 : 1);
        int ret = 0;
        for (int i = 0; i + k - 1 < n; i++)
            if (a[i] == 0)
            {
                ret++;
                for (int j = i; j < i + k; j++)
                    a[j] ^= 1;
            }
        int can = 1;
        for (int i = 0; i < n; i++)
            if (a[i] == 0)
                can = 0;
        cout << "Case #" << tt << ": ";
        if (can == 0) cout << "IMPOSSIBLE\n";
        else cout << ret << "\n";
    }
    return 0;
}
