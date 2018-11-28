#include <algorithm>
#include <cmath>
#include <ctime>
#include <iostream>
#include <iomanip>
#include <map>
#include <string>
#include <vector>

using namespace std;

void solution();

int main()
{
    ios::sync_with_stdio(false);
#ifdef HOME
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    clock_t start = clock();
#endif // HOME
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t)
    {
        cout << "Case #" << t + 1 << ": ";
        cerr << "Case #" << t + 1 << endl;
        solution();
    }
#ifdef HOME
    clock_t finish = clock();
    cerr << "Total time: " << fixed << setprecision(3) << double(finish - start) / double(CLOCKS_PER_SEC) << endl;
#endif // HOME
    return EXIT_SUCCESS;
}

typedef long long ll;
typedef long long ld;
template <typename T> inline T sqr(T x) { return x * x; }
#define int ll
#define EPS 1e-9

#define N 100
int n, p, g[N];

void solution()
{
    cin >> n >> p;
    for (int i = 0; i < n; ++i)
        cin >> g[i];
    sort(g, g + n);
    vector<int> c[4];
    int ans = 0;
    for (int i = 0; i < n; ++i)
    {
        if (g[i] % p == 0)
            ++ans;
        else
            c[g[i] % p].push_back(g[i]);
    }
    if (p == 2)
    {
        while (c[1].size() > 1)
        {
            c[1].pop_back();
            c[1].pop_back();
            ++ans;
        }
        if (c[1].size())
            ++ans;
    }
    else if (p == 3)
    {
        while (c[1].size() && c[2].size())
        {
            c[1].pop_back();
            c[2].pop_back();
            ++ans;
        }
        while (c[2].size() > 2)
        {
            c[2].pop_back();
            c[2].pop_back();
            c[2].pop_back();
            ++ans;
        }
        while (c[1].size() > 2)
        {
            c[1].pop_back();
            c[1].pop_back();
            c[1].pop_back();
            ++ans;
        }
        if (c[1].size() || c[2].size())
            ++ans;
    }
    else if (p == 4)
    {
        while (c[1].size() && c[3].size())
        {
            c[1].pop_back();
            c[3].pop_back();
            ++ans;
        }
        while (c[2].size() > 1)
        {
            c[2].pop_back();
            c[2].pop_back();
            ++ans;
        }
        while (c[2].size() && c[1].size() > 1)
        {
            c[2].pop_back();
            c[1].pop_back();
            c[1].pop_back();
            ++ans;
        }
        while (c[2].size() && c[3].size() > 1)
        {
            c[2].pop_back();
            c[3].pop_back();
            c[3].pop_back();
            ++ans;
        }
        while (c[1].size() > 3)
        {
            c[1].pop_back();
            c[1].pop_back();
            c[1].pop_back();
            c[1].pop_back();
            ++ans;
        }
        while (c[3].size() > 3)
        {
            c[3].pop_back();
            c[3].pop_back();
            c[3].pop_back();
            c[3].pop_back();
            ++ans;
        }
        if (c[1].size() || c[2].size() || c[3].size())
            ++ans;
    }
    cout << ans << endl;
    cerr << ans << endl;
}
