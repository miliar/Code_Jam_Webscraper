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
    pair<pii, char>* a = new pair<pii, char>[n + k];
    int time[2] = {720, 720};
    for(int i = 0;i < n + k;i++)
    {
        cin >> a[i].X.X >> a[i].X.Y;
        if(i < n)
            a[i].Y = 0;
        else
            a[i].Y = 1;
        time[a[i].Y]-= (a[i].X.Y - a[i].X.X);
    }
    sort(a, a + n + k);
    vi c[2];
    int res = 0;
    for(int i = 0;i < n + k;i++)
        if(a[i].Y == a[(i + 1) % (n + k)].Y)
        {
            int t = a[(i + 1) % (n + k)].X.X - a[i].X.Y;
            if(t < 0)
                t+= 60 * 24;
            c[a[i].Y].push_back(t);
        }
        else
            res++;
    sort(c[0].begin(), c[0].end());
    sort(c[1].begin(), c[1].end());
    //cout << time[0] << ' ' << res << ':';
    for(int i : c[0])
    {
        if(time[0] >= i)
            time[0]-= i;
        else
        {
            time[0] = -1;
            res+= 2;
        }
    }
//    cout << endl;
//    cout << time[1] << ' ' << res << ':';
    for(int i : c[1])
    {
        if(time[1] >= i)
            time[1]-= i;
        else
        {
            time[1] = -1;
            res+= 2;
        }
    }
    cout << res << endl;
//    cout << endl;
}
