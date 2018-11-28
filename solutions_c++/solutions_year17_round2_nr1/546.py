#include<bits/stdc++.h>
#define mp make_pair
#define PII pair<int,int>
#define fi first
#define se second
#define pb push_back
#define ll long long
#define ull unsigned long long
#define ui unsigned int
#define sci(x) scanf("%d",&x)
#define scs(s) scanf("%s",s)
#define scc(c) scanf("%c",c)
#define scd(d) scanf("%lf",&d)
#define scld(ld) scanf("%Lf",&ld)
#define int long long
using namespace std;

//********************************************
//Error tracking
#define show(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }

vector<string> split(const string& s, char c) {
    vector<string> v;
    stringstream ss(s);
    string x;
    while (getline(ss, x, c))
        v.emplace_back(x);
    return move(v);
}

void err(vector<string>::iterator it) {}
template<typename T, typename... Args>
void err(vector<string>::iterator it, T a, Args... args) {
    cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << '\n';
    err(++it, args...);
}
//********************************************

const double eps = 0.0000000001;
const int NMAX = 1005;

int t, n, D;
PII a[NMAX];
double timp[NMAX], arrival[NMAX];

double Max(double A, double B)
{
    if (B - A > eps) return B;
    return A;
}

double Min(double A, double B)
{
    if (A - B > eps) return B;
    return A;
}


int32_t main()
{
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    cin.sync_with_stdio(false);
    
    cout << setprecision(8) << fixed;
    cin >> t;
    for (int jj = 1; jj <= t; jj++)
    {
        cout << "Case #" << jj << ": ";

        cin >> D >> n;
        for (int i = 1; i <= n; i++) cin >> a[i].fi >> a[i].se;
        sort(a + 1, a + n + 1);

        for (int i = 1; i <= n; i++) timp[i] = (double)(D - a[i].fi) / a[i].se;

        for (int i = 1; i <= n; i++)
        {
            double mx = timp[i];
            for (int j = i + 1; j <= n; j++)
                if (timp[j] - timp[i] > eps)
                    mx = Max(mx, timp[j]);
            arrival[i] = mx;
        }

        double st = 1, dr = 1LL<<60, ans;
        for (int steps = 1; steps <= 4000; steps++)
        {
            double mij = (st + dr) / 2;

            double arrive = D / mij;
            int ok = 1;
            for (int i = 1; i <= n; i++)
                if (arrival[i] - arrive > eps)
                    ok = 0;

            if (ok)
            {
                ans = mij;
                st = mij + eps;
            }
            else dr = mij - eps;
        }

        cout << ans << "\n";
       // cout << n << " " << D << "\n";
       // for (int i = 1; i <= n; i++) cout << a[i].fi << " " << a[i].se << "\n";
       // for (int i = 1; i <= n; i++) cout << arrival[i] << "\n";
    }
    return 0;   
}