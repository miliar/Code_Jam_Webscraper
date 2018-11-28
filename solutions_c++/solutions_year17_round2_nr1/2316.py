#include<bits/stdc++.h>
using namespace std;
int t, cs = 1, m, n;
double x, y, z, p, q, r;
pair < double, double > ara[300000];

int main()
{
    freopen("cruselarge.txt", "r", stdin);
    freopen("cruselargeout.txt", "w", stdout);
    cin >> t;

    while(t--){

        scanf("%lf %d", &p, &n);
        double tm = 0;

        for(int i = 1; i <= n; i++){
            scanf("%lf %lf", &x, &y);

            double tmp = (p - x) / y;
            tm = max(tm, tmp);

        }

        double ans = p / tm;

        printf("Case #%d: %.10lf\n", cs++, ans);

    }


    return 0;
}
