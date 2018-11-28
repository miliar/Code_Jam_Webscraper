#include <cstdio>
#include <algorithm>
#include <utility>
#include <cmath>
#include <vector>

using namespace std;
#define MAXN 1001
int radii[MAXN], heights[MAXN];
double dyn[MAXN][MAXN];

struct Panc
{
    long long height;
    long long rad;
    Panc(long long h, long long r) : height(h), rad(r)
        {
        }
};


    bool operator< (const Panc &p1, const Panc &p2)
        {
            if (p1.rad > p2.rad)
            {
                return true;
            }

            if (p1.rad < p2.rad)
            {
                return false;
            }

            if (p1.height > p2.height)
            {
                return true;
            }
            return false;
        }


int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out","w", stdout);

    int t;
    scanf("%d", &t);

    for (int i = 1; i <= t; ++i)
    {
        int n, k;
        double smax = 0;
        vector<Panc> pc;
        scanf("%d%d", &n, &k);

        for (int j = 1; j <= n; ++j)
        {
            long long h, r;
            scanf("%lld%lld", &r, &h);
            pc.push_back(Panc(h, r));
        }

        sort(pc.begin(), pc.end());
        
        for (int j = 1; j <= n; ++j)
        {
            dyn[1][j] = 2 * M_PI * pc[j-1].rad * pc[j-1].height;
            if (dyn[1][j] + M_PI * pc[j-1].rad * pc[j-1].rad > smax)
            {
                smax = dyn[1][j] + M_PI * pc[j-1].rad * pc[j-1].rad;
            }
        }

        for (int j = 2; j <= k; ++j)
        {
            smax = 0;
            for (int l = 1; l <= n - j + 1; ++l)
            {
                int idxmax = l+1;
                for (int l2 = l + 2; l2 <= n-j+2; ++l2)
                {
                    if (dyn[j-1][l2] > dyn[j-1][idxmax])
                    {
                        idxmax = l2;
                    }
                }
                dyn[j][l] = dyn[j-1][idxmax];
                dyn[j][l] += 2 * M_PI * pc[l-1].rad * pc[l-1].height;
                double toparea = M_PI * pc[l-1].rad * pc[l-1].rad;
                if (dyn[j][l] + toparea > smax)
                {
                    smax = dyn[j][l] + toparea;
                }
            }
        }

        printf("Case #%d: %.6lf\n", i, smax);
    }
    
    return 0;
}
