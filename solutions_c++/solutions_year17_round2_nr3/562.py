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
const int inf = 1LL << 50;
const int NMAX = 105;

int t, N, Q;
int maxdist[NMAX], sp[NMAX];
int dist[NMAX][NMAX];
double disthorse[NMAX][NMAX];

double Min(double A, double B)
{
    if (A - B > eps) return B;
    return A;
}

void Roy()
{
    for (int k = 1; k <= N; k++)
        for (int i = 1; i <= N; i++)
            for (int j = 1; j <= N; j++)
                if (dist[i][k] > 0 && dist[k][j] > 0)
                {
                    if (dist[i][j] == -1) dist[i][j] = dist[i][k] + dist[k][j];
                    else dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
}

void RoyHorse()
{
    //make atomic paths
    for (int i = 1; i <= N; i++)
        for (int j = 1; j <= N; j++)
            {
                if (dist[i][j] > 0 && maxdist[i] >= dist[i][j])
                    disthorse[i][j] = (double)dist[i][j] / sp[i];
                if (disthorse[i][j] == 0)
                    disthorse[i][j] = inf;
                //cout << i << " " << j << " " << disthorse[i][j] << "\n";
            }

    for (int k = 1; k <= N; k++)
        for (int i = 1; i <= N; i++)
            for (int j = 1; j <= N; j++)
                disthorse[i][j] = Min(disthorse[i][j], disthorse[i][k] + disthorse[k][j]);
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

        cin >> N >> Q;
        for (int i = 1; i <= N; i++) cin >> maxdist[i] >> sp[i];
        for (int i = 1; i <= N; i++)
            for (int j = 1; j <= N; j++)
                cin >> dist[i][j];

        //normal roy-floyd
        Roy();

        //roy-floyd with horses
        RoyHorse();

        while (Q--)
        {
            int x, y;
            cin >> x >> y;
            cout << disthorse[x][y] << " ";
        }

        cout << "\n";

        //clean
        for (int i = 1; i <= N; i++)
            for (int j = 1; j <= N; j++)
                dist[i][j] = disthorse[i][j] = 0;
    }
    
    return 0;   
}