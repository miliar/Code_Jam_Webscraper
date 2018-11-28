#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <string.h>
#include <set>
using namespace std;

#define EPS 1e-8
#define mod 1000000007

typedef long long ll;

const double pi = acos(-1.0);

double a[55];

int main(int argc, const char * argv[]) {
    freopen("/Users/dergach007/Desktop/FacebookHackerCup/FacebookHackerCup/C-small-1-attempt0.in.txt", "r", stdin);
    freopen("/Users/dergach007/Desktop/FacebookHackerCup/FacebookHackerCup/C-small-1-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++)
    {
        int n, k;
        scanf("%d %d", &n, &k);
        double u;
        scanf("%lf", &u);
        for(int i = 0; i < n; i++)
            scanf("%lf", &a[i]);
        sort(a, a + n);
        a[n++] = 1.0;
        for(int i = 1; i < n && u > 0; i++)
        {
            double x = min(u / i, a[i] - a[i-1]);
            u -= i * x;
            for(int j = 0; j < i; j++)
                a[j] += x;
        }
        double res = 1;
        for(int i = 0; i < n; i++)
            res *= a[i];
        printf("Case #%d: %.10lf\n", t, res);
    }
    return 0;
}
