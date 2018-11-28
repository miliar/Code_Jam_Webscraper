#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define fio ios_base::sync_with_stdio(false)
#define MOD 1000000007
#define INF 1000000000
#define INFLL 1000000000000000000LL
#define range(a, b, c) (a>=b && a<c)
#define stlfor(a, b) for(auto a=b.begin(); a!=b.end(); a++)
#define rstlfor(a, b) for(auto a=b.rbegin(); a!=b.rend(); a++)
#define mp make_pair
#define pb push_back
#define ff first
#define ss second
using namespace std;
using namespace __gnu_pbds;
typedef pair<int, int> pii;
typedef priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> min_pq;
typedef tree<pii, null_type, less<pii>, rb_tree_tag, tree_order_statistics_node_update> OST;

const int N = 101;
const double one = 1;

int e[N], s[N];
long long d[N][N];
double t[N][N];

int main()
{
    fio;
    cout << fixed << setprecision(10);
    int tt;
    cin >> tt;
    for(int tc=1; tc<=tt; tc++)
    {
        int n, q;
        cin >> n >> q;
        for(int i=1; i<=n; i++)
        {
            cin >> e[i] >> s[i];
        }
        for(int i=1; i<=n; i++)
        {
            for(int j=1; j<=n; j++)
            {
                t[i][j] = INFLL;
                cin >> d[i][j];
                if(d[i][j] == -1)
                    d[i][j] = INFLL;
            }
            t[i][i] = 0;
        }
        for(int k=1; k<=n; k++)
        {
            for(int i=1; i<=n; i++)
            {
                for(int j=1; j<=n; j++)
                {
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
                    t[i][j] = min(t[i][j], t[i][k] + t[k][j]);
                    if(d[i][j] <= e[i])
                        t[i][j] = min(t[i][j], (d[i][j] * one) / s[i]);
                }
            }
        }
        for(int k=1; k<=n; k++)
        {
            for(int i=1; i<=n; i++)
            {
                for(int j=1; j<=n; j++)
                {
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
                    t[i][j] = min(t[i][j], t[i][k] + t[k][j]);
                    if(d[i][j] <= e[i])
                        t[i][j] = min(t[i][j], (d[i][j] * one) / s[i]);
                }
            }
        }
        cout << "Case #" << tc << ": ";
        while(q--)
        {
            int u, v;
            cin >> u >> v;
            cout << t[u][v] << ' ';
        }
        cout << endl;
    }
}