#include<iostream>
#include<cstdio>
#include<queue>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

#define FOR(i,l,h) for(int i = (l); i <= (h); i++)

int a[100][100], l[100][100], r[100][100], p[100], R[100];
int n, m;

bool check()
{
    int maxl = 0, minr = 100000000;
    FOR(i,0,n-1)
    {
        maxl = max(maxl, l[i][p[i]]);
        minr = min(minr, r[i][p[i]]);
    }
    return maxl <= minr;
}

int main()
{
    freopen("B-large.in-2.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cout << "Case #" << t << ": ";
        cin >> n >> m;
        FOR(i,0,n-1)
            cin >> R[i];
        FOR(i,0,n-1)
        {
            FOR(j,0,m-1)
                cin >> a[i][j];
            sort(a[i], a[i] + m);
        }
        FOR(i,0,n-1)
            FOR(j,0,m-1)
            {
                l[i][j] = int(ceil(a[i][j] / 1.1 / R[i]));
                r[i][j] = int(a[i][j] / 0.9 / R[i]);
            }
        memset(p, 0, sizeof(p));
        int ans = 0;
        while (true)
        {
            if (check())
            {
                bool flag = true;
                FOR(i,0,n-1)
                    if (p[i] <= m-2)
                        p[i]++;
                    else
                        flag = false;
                ans++;
                if (!flag) break;
            }
            else
            {
                int minl_i = 0;
                FOR(i,1,n-1)
                    if (l[i][p[i]] < l[minl_i][p[minl_i]])
                        minl_i = i;
                if (p[minl_i] <= m-2)
                    p[minl_i]++;
                else
                    break;
            }
        }
        cout << ans << endl;
    }
    return 0;
}
