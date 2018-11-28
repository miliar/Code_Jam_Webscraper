#include <bits/stdc++.h>
#define f first
#define s second

using namespace std;

int const N = 1005;
double const pi = 3.14159265;

int n, k;
long long DP[N][N];
pair < long long , long long > a[N];

int main()
{
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for(int _=1; _<=T; _++){


        cout << "Case #" << _ << ": ";
        cin >> n >> k;

        for(int i=0; i<=n; i++)
            for(int j=0; j<=k; j++)
                DP[i][j] = 0;

        for(int i=1; i<=n; i++){
            cin >> a[i].f >> a[i].s;
        }
        sort(a+1, a+n+1);
        for(int i=1; i<=n; i++)
            for(int p=1; p<=k; p++)
                for(int j=0; j<i; j++){
                    DP[i][p] = max(DP[i][p], DP[j][p-1] + (a[i].f * a[i].f - a[j].f * a[j].f) + a[i].f * a[i].s * 2);
                }
        double ans = 0;
        for(int i=1; i<=n; i++)
            ans = max(ans, 1.0 * DP[i][k]);
        printf("%0.9f\n", ans * pi);
    }
}
