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
const int N = 1005;
const double PI = acos(-1);

int n, k;
double rad[N], hei[N];
int order[N];

double get_side(int i)
{
    return 2 * PI * rad[i] * hei[i];
}

double get_top(int i)
{
    return PI * rad[i] * rad[i];
}

void solve()
{
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; i++)
        scanf("%lf%lf", &rad[i], &hei[i]);

    for (int i = 0; i < n; i++)
        order[i] = i;
    sort(order, order + n, [&] (int a, int b)
        {
            return rad[a] > rad[b];
        });

    double best = 0;

    for (int i1 = 0; i1 < n; i1++)
    {
        int i = order[i1];
        double cur = get_top(i) + get_side(i);

        vector<double> other;
        for (int j1 = i1 + 1; j1 < n; j1++)
        {
            int j = order[j1];
            other.push_back(get_side(j));
        }
        sort(other.begin(), other.end(), greater<double>());

        for (int j = 0; j < min((int)other.size(), k - 1); j++)
            cur += other[j];

        best = max(best, cur);
    }

    printf("%.10lf\n", best);
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
