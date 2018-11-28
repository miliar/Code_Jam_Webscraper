#include <bits/stdc++.h>
using namespace std;

#ifdef LOCAL
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define print_var(x) cerr << #x << " = " << x << endl
#define print_array(arr, len) {cerr << #arr << " = "; for (int i = 0; i < len; i++) cerr << arr[i] << " "; cerr << endl;}
#define print_iterable(it) {cerr << #it << " = "; for (const auto &e : it) cerr << e << " "; cerr << endl;}
#else
#define eprintf(...) (void)0
#define print_var(x) (void)0
#define print_array(arr, len) (void)0
#define print_iterable(it) (void)0
#endif

typedef long long ll;

char buf[105];
string scan_token()
{
    scanf("%s", buf);
    return buf;
}

void solve()
{
    string s = scan_token();

    while (true)
    {
        int p = 0;
        while (p + 1 < (int)s.length() && s[p] <= s[p + 1])
            p++;
        if (p == (int)s.length() - 1)
            break;
        for (int i = p + 1; i < (int)s.length(); i++)
            s[i] = '9';
        if (s[p] == '0')
            throw;
        s[p]--;
        while (s[0] == '0')
            s = s.substr(1);
    }

    printf("%s\n", s.c_str());
}

int main()
{
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }

    eprintf("\n\ntime = %.3lf\n", (double)clock() / CLOCKS_PER_SEC);
}
