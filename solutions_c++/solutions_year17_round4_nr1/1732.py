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
//    ios::sync_with_stdio(false);
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
    int n, p;
    cin >> n >> p;
    int* a = new int[p];
    for(int i = 0;i < p;i++)
        a[i] = 0;
    for(int i = 0;i < n;i++)
    {
        int t;
        cin >> t;
        a[t % p]++;
    }
    int res = a[0];
    switch(p)
    {
        case 2:res+= (a[1] + 1) / 2;
        break;
        case 3:
        {
            int t = min(a[1], a[2]);
            res+= t;
            a[1]-= t;
            a[2]-= t;
            res+= (a[1] + 2) / 3;
            res+= (a[2] + 2) / 3;
        }
        break;
        case 4:
        {
            int t = min(a[1], a[3]);
            res+= t;
            a[1]-= t;
            a[2]-= t;
            res+= (a[2] + 1) / 2;
            a[2]%= 2;
            if(a[1] > 0)
            {
                res+= a[2];
                a[1] = max(0, a[1] - 2 * a[2]);
                res+= (a[1] + 2) / 3;
            }
            if(a[3] > 0)
            {
                res+= a[2];
                a[3] = max(0, a[3] - 2 * a[2]);
                res+= (a[3] + 2) / 3;
            }
        }
        break;
    }
    cout << res << endl;
}
