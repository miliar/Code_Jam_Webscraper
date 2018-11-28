
#include<bits/stdc++.h>
using namespace std;
#define D(x)        cout<<#x " = "<<(x)<<endl
#define un(x)       x.erase(unique(x.begin(),x.end()), x.end())
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define pb          push_back
#define mp          make_pair
#define xx          first
#define yy          second
#define hp          (LL) 999983
#define MAX         1000
#define eps         1e-9
#define pi          acos(-1.00)
typedef long long int LL;
typedef pair<int,int> pii;

int want[MAX+5][MAX+5];
int temp[MAX+5][MAX+5];
int n, c, m;

bool oka(int mid)
{
    int i, j;
    for(i = 1; i <= c; i++)
        for(j = 1; j <= n; j++)
            temp[i][j] = want[i][j];

    int vac = 0;

    for(int clm = 1; clm <= n; clm++)
    {
        int sum = 0;
        for(i = 1; i <= c; i++)
            sum += temp[i][clm];

        if(sum < mid) vac += mid - sum;
        else{
            vac -= sum - mid;
            if(vac < 0) return false;
        }
    }

    return true;
}

int maxrowsum()
{
    int i, j, sum = 0, mx = 0;
    for(i = 1; i <= c; i++)
    {
        sum = 0;
        for(j = 1; j <= n; j++)
            sum += want[i][j];

        mx = max(mx, sum);
    }

    return mx;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int i, j, k, t, cs ;
    int p, b;

    sf(t);
    for(cs = 1; cs <= t; cs++)
    {
        memset(want, 0, sizeof(want));
        sfff(n, c, m);
        for(i = 1; i <= m; i++)
        {
            sff(p,b);
            want[b][p]++;
        }

        int lo = maxrowsum(), hi = m, mid;
        while(lo != hi)
        {
            mid = (lo + hi)/2;
            if(oka(mid)) hi = mid;
            else lo = mid + 1;
        }

        int mc = 0;
        for(int clm = 1; clm <= n; clm++)
        {
            int sum = 0;
            for(i = 1; i <= c; i++)
                sum += want[i][clm];

            if(sum > lo) mc += sum - lo;
        }

        printf("Case #%d: %d %d\n", cs, lo, mc);
    }


    return 0;
}





