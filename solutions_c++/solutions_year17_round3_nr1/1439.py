#include <bits/stdc++.h>
#define MAX 1024
#define PI acos(-1.0)

using namespace std;

pair<double, int> p[MAX];
pair<int, int> v[MAX];

int main() {

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T, n, k;

    scanf("%d", &T);
    for(int ncase=1; ncase<=T; ncase++) {
        scanf("%d %d", &n, &k);
        for(int i=0; i<n; i++) {
            scanf("%d %d", &v[i].first, &v[i].second);
            p[i].second = i;
            p[i].first = 2.0 * (double)v[i].first * PI * (double)v[i].second;
        }
        sort(p, p+n, greater< pair<double,int> >());

        double areaL = 0.0;
        int maxR = 0, secMaxR = 0, newR = 0;
        double totalArea = 0.0, newArea = 0.0;

        for(int i=0; i<k-1; i++) {
            int idx = p[i].second;
            if (v[idx].first >= maxR) {
                secMaxR = maxR;
                maxR = v[idx].first;
            }
            areaL += p[i].first;
        }
        totalArea = areaL + maxR*maxR*PI;

        for(int i=k-1; i<n; i++) {
            int idx = p[i].second;
            newR = max(maxR, v[idx].first);
            totalArea = max(totalArea, areaL + p[i].first + (double)(newR) * (double)(newR) * PI);
        }

        printf("Case #%d: %.8f\n", ncase, totalArea);
    }

    return 0;
}
