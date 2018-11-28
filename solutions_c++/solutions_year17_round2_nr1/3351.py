#include <iostream>
#include <iomanip>
#include <string>
#include <map>
#include <math.h>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <deque>
#include <memory.h>
#include <cassert>
#include <ctime>
#include <climits>
#include <time.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define pb push_back
#define mp make_pair
#define FILE "file"
#define lc v << 1
#define rc (v << 1) + 1
#define inf 1e+9
#define linf ll(4 * 1e+18)
#define classname MakePalindrome

void solve()
{
    double d;
    int n;
    cin >> d;
    cin >> n;
    double ans = 1e+14;
    for(int i = 0; i < n; i++)
    {
        double k, s;
        cin >> k >> s;
        ans = min(ans, d * s / (d - k));
    }
    cout << setprecision(14) << ans;
    return;
}

void gcj()
{
    int t;
    cin >> t;
    for(int step = 0; step < t; step++)
    {
        cout << "Case #" << step + 1 << ": ";
        solve();
        cout << "\n";
    }
}

int main()
{
    //ios_base::sync_with_stdio(false);cin.tie(0), cout.tie(0);
    freopen("A-large.in", "r", stdin);freopen(FILE ".out", "w", stdout);
    //freopen(FILE ".in", "r", stdin);freopen(FILE ".out", "w", stdout);
    gcj();
    return 0;
}
