#include<iostream>
#include<vector>
#include<sstream>
#include<set>
#include<map>
#include<algorithm>
#include<tuple>

using namespace std;

int n;
int p;
int count[4];

map<tuple<int, int, int>, int> d;

const int INF = 2000000000;

int f(int n1, int n2, int n3)
{
    if (n1 < 0 || n2 < 0 || n3 < 0)
        return -INF;
    if (n1 == 0 && n2 == 0 && n3 == 0)
        return 0;
    if (d.count({n1, n2, n3}))
        return d[{n1, n2, n3}];
    int ans = 1;
    for (int c3 = 0; c3 <= p && c3 <= n3; ++c3) 
    for (int c2 = 0; c2 <= p && c2 <= n2; ++c2)
    for (int c1 = 0; c1 <= p && c1 <= n1; ++c1)
    {
        if ((c3 * 3 + c2 * 2 + c1) % p == 0 && (c1 + c2 + c3) > 0)
        {
            ans = max(ans, 1 + f(n1 - c1, n2 - c2, n3 - c3));
        }
    }
    d[{n1, n2, n3}] = ans;
    return ans;
}

int solve()
{
    cin >> n >> p;
    int count[4] = {0, 0, 0, 0};
    d.clear();
    d[{0, 0, 0}] = 0;
    for (int i = 0; i < n; ++i)
    {
        int gi;
        cin >> gi;
        count[gi % p]++;
    }
    return count[0] + f(count[1], count[2], count[3]);
}

int main()
{
    int T, t;
    cin >> T;
    cout.precision(20);
    for (t = 1; t <= T; ++t)
    {
        cout << "Case #" << t << ": " << solve() << endl;
    }
    return 0;
}

