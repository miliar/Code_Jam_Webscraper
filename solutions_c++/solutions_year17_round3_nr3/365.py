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
const int N = 55;

int n, k;
double u;
double prob[N];

double eval(double x)
{
    double cost = 0;
    for (int i = 0; i < n; i++)
        if (prob[i] < x)
            cost += x - prob[i];
    return cost;
}

void solve()
{
    scanf("%d%d", &n, &k);
    scanf("%lf", &u);
    for (int i = 0; i < n; i++)
        scanf("%lf", &prob[i]);

    double left = 0, right = 1;
    for (int it = 0; it < 100; it++)
    {
        double mid = (left + right) / 2;
        if (eval(mid) <= u)
            left = mid;
        else
            right = mid;
    }

    double ans = 1;
    for (int i = 0; i < n; i++)
    {
        if (prob[i] < left)
            ans *= left;
        else
            ans *= prob[i];
    }

    printf("%.10lf\n", ans);
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
