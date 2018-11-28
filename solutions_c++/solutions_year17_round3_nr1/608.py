#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector <int> vi;
typedef vector <ll> vll;
typedef pair <int, int> pii;
typedef pair <double, double> pdd;
typedef pair <ll, ll> pll;
typedef vector <pii> vii;
typedef vector <double> vd;
 
#define SQR(x) ((x) * (x))
#define CUBE(x) ((x) * (x) * (x))
#define MP(a, b) make_pair((a), (b))
#define TASK "rmq"
#define MOD 1000000007LL
#define X first
#define Y second
#define EPS 1e-10
#define TESTING3
#define LAT 26
#define CYR 33
#define N 1000004
#define INF 1000000000
#define PI (acos(-1.0L))
#define double long double
#define MULTI
 
void solution();
 
stack <clock_t> times;
 
void start_t()
{
    times.push(clock());
}
 
void stop_t(string out)
{
    clock_t now = clock();
    clock_t past = times.top();
    times.pop();
    double delta = now - past;
    cout << out << ": " << fixed << delta / (double)CLOCKS_PER_SEC << endl;
}
 
int main()
{
//    ios::sync_with_stdio(false);
#ifdef _HOME_
    freopen("input.txt", "r", stdin);
    start_t();
#else
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif // _HOME_
#ifdef MULTI
    int n;
    //scanf("%ld", &n);
    cin >> n;
    for(int i = 0;i < n;i++)
    {
        cout << "Case #" << i + 1 << ": ";
#endif
    solution();
    }
#ifdef _HOME_
    stop_t("Total time");
#endif // _HOME_
    return 0;
}
 
void solution()
{
    int n, k;
    cin >> n >> k;
    pll* a = new pll[n];
    for(int i = 0;i < n;i++)
        cin >> a[i].X >> a[i].Y;
    sort(a, a + n);
    reverse(a, a + n);
    ll vmax = 0;
    for(int i = 0;i + k <= n;i++)
    {
        ll t = a[i].X * a[i].X + 2 * a[i].X * a[i].Y;
//        cout << t << endl;
        ll* b = new ll[n - i - 1];
        for(int j = i + 1;j < n;j++)
            b[j - i - 1] = a[j].X * a[j].Y;
        sort(b, b + n - i - 1);
        for(int l = 0;l < k - 1;l++)
            t+= 2 * b[n - i - 2 - l];
//        cout << t << endl;
        vmax = max(vmax, t);
    }
    ld r = vmax;
    r*= PI;
    printf("%.7Lf\n", r);
}
