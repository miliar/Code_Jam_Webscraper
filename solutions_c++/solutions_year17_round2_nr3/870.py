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
    //ios::sync_with_stdio(false);
#ifdef _HOME_
    freopen("input.txt", "r", stdin);
    start_t();
#else
//    freopen("input.txt", "r", stdin);
//    freopen("output.txt", "w", stdout);
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
    int n, q;
    cin >> n >> q;
    pll* a = new pll[n];
    for(int i = 0;i < n;i++)
        cin >> a[i].X >> a[i].Y;
    ll** g = new ll*[n];
    for(int i = 0;i < n;i++)
    {
        g[i] = new ll[n];
        for(int j = 0;j < n;j++)
            cin >> g[i][j];
    }
    for(int t = 0;t < q;t++)
    {
        int s, r;
        cin >> s >> r;
        if(s != 1)
        {
            cout << "FAILED!!!!!!!!!";
            return;
        }
        if(r != n)
        {
            cout << "FAILED!!!!!!!!!";
            return;
        }
        ld* dp = new ld[n];
        dp[0] = 0;
        for(int i = 1;i < n;i++)
        {
            dp[i] = -1;
            ll s = 0;
            for(int j = i - 1;j >= 0;j--)
            {
                s+= g[j][j + 1];
                //cout << s << ' ' << j << ':' << a[j].X << endl;
                if(s <= a[j].X)
                {
                    //cout << a[j].Y << ' ' << dp[j] << endl;
                    dp[i] = dp[j] + s * 1.0L / a[j].Y;
                }
            }
//            cout << dp[i] << ' ';
            if(dp[i] != -1)
            {
                s = 0;
                for(int j = i - 1;j >= 0;j--)
                {
                    s+= g[j][j + 1];
//                    cout << s << ' ' << j << ':' << a[j].X << endl;
                    if(s <= a[j].X)
                    {
//                        cout << a[j].Y << ' ' << dp[j] << endl;
//                        cout << dp[i] << ';' << dp[j] + s * 1.0L / a[j].Y << endl;
                        dp[i] = min(dp[i], dp[j] + s * 1.0L / a[j].Y);
                    }
                }
            }
        }
        printf("%.6Lf\n", dp[n - 1]);
    }
}
