#include <cstdio>
#include <cmath>
#include <set>
#include <utility>
#include <vector>
#include <algorithm>

#define PB push_back
#define MP make_pair

using namespace std;

typedef pair<double, double> pdd;

const double PI = acos(-1);

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int ct = 1; ct <= T; ct++)
    {
        int N, K;
        vector<pdd> v;
        vector<double> h;

        scanf("%d%d", &N, &K);
        for(int i = 0; i < N; i++)
        {
            int R, H;
            scanf("%d%d", &R, &H);
            v.PB(MP(R, H));
        }

        sort(v.begin(), v.end());   //tri par rayon croissant

        double ans = 0;
        for(int i = 0; i < N; i++)
        {
            double aire = PI*v[i].first*v[i].first; //vu du dessus
            double aire_lat = 2*PI*v[i].first*v[i].second;
            aire += aire_lat;

            for(int j = i-1; j >= max(0, i-K+1); j--)
                aire += h[j];

            ans = max(ans, aire);

            h.PB(aire_lat);
            sort(h.begin(), h.end());
        }

        printf("Case #%d: %.08f\n", ct, ans);
    }

    return 0;
}
