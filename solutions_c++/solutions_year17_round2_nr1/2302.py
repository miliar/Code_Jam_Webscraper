#include <bits/stdc++.h>
#define ex(a) { cout << a; exit(0); }
#define wcase(a,b) cout << "Case #" << a << ": " << fixed << b << endl
#define finput freopen("input.txt", "r", stdin)
#define foutput freopen("output.txt", "w", stdout)
using namespace std;
int input()
{
    int res = 0; char c = ' ';
    while (c > '9' || c < '0') c = getchar();
    while (c >= '0' && c <= '9') res = res * 10 + (c - '0'), c = getchar();
    return res;
}
typedef long long ll;
typedef long double ld;
const int N = 1e5 + 10;

int main()
{
    finput, foutput;
    int t = input();
    cout.precision(7);
    for (int test = 1; test <= t; ++ test)
    {
        ld d = input(), n = input();
        vector <pair <ld, ld> > x(n);
        for (int i = 0; i < n; ++ i)
            x[i].first = input(), x[i].second = input();
        sort(x.begin(), x.end());
        ld cur = 0;
        for (int i = x.size() - 1; i >= 0; -- i)
            cur = max(cur, (d - x[i].first) / x[i].second);
        wcase(test, d / cur);
    }
}
