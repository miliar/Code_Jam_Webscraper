#include <bits/stdtr1c++.h>

#define clr(ar) memset(ar, 0, sizeof(ar))
#define read() freopen("lol.txt", "r", stdin)
#define write() freopen("out.txt", "w", stdout)
#define dbg(x) cout << #x << " = " << x << endl
#define ran(a, b) ((((rand() << 15) ^ rand()) % ((b) - (a) + 1)) + (a))

using namespace std;

const long double PI = 2.0 * acos(0.0);

int n, k;
bool visited[1010][1010];
long double dp[1010][1010];
long long R[1010], H[1010];
pair<long long, long long> ar[1010];

long double F(int i, int k){
    if (k == 0) return 0.0;
    if (i == n) return -1e100;
    if (visited[i][k]) return dp[i][k];

    long double res = F(i + 1, k);
    long double x = F(i + 1, k - 1) + (PI * 2 * R[i] * H[i]);
    if (x > res) res = x;

    visited[i][k] = 1;
    return (dp[i][k] = res);
}

int main(){
    read();
    write();
    int T = 0, t, i, j, r, h;

    scanf("%d", &t);
    while (t--){
        scanf("%d %d", &n, &k);
        for (i = 0; i < n; i++){
            scanf("%d %d", &r, &h);
            ar[i] = make_pair(-r, -h);
        }
        sort(ar, ar + n);
        for (i = 0; i < n; i++) R[i] = -ar[i].first;
        for (i = 0; i < n; i++) H[i] = -ar[i].second;

        clr(visited);
        long double res = 0.0;
        for (i = 0; i < n; i++){
            long double x = PI * R[i] * R[i] + (PI * 2 * R[i] * H[i]);
            x = x + F(i + 1, k - 1);
            if (x > res) res = x;
        }

        printf("Case #%d: %0.12f\n", ++T, (double)res + 1e-15);
    }
    return 0;
}
