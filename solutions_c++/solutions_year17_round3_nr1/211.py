
#include<bits/stdc++.h>
using namespace std;
#define D(x)        cout << #x " = " << (x) << endl
#define MAX         1000
typedef long long int LL;

int r[MAX+5], h[MAX+5];
const long double pi = acos(-1.00);

vector<int> current;

bool cmp(int u, int v){ return (LL) u[r] * u[h] > (LL) v[r] * v[h]; }

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int i, j, k, t, cs, n;
    int fix;

    scanf("%d", &t);
    for(cs = 1; cs <= t; cs++)
    {
        scanf("%d %d", &n, &k);
        for(i = 1; i <= n; i++)
            scanf("%d %d", &r[i], &h[i]);

        long double mx = 0;
        for(i = 1; i <= n; i++)
        {
            current.clear();

            fix = i;
            for(j = 1; j <= n; j++)
                if(fix != j && r[j] <= r[fix])
                    current.push_back(j);

            long double A = pi * (LL) r[fix] * r[fix] + 2 * pi * (LL)r[fix] * h[fix];

            if(current.size() + 1 < k) continue;
            sort(current.begin(), current.end(), cmp);
            for(j = 0; j <= k - 2; j++) A += 2 * pi * (LL)r[current[j]] * h[current[j]];

            mx = max(mx, A);
        }

        printf("Case #%d: %0.10f\n", cs, (double) mx);
    }

    return 0;

}
