#include <bits/stdc++.h>
#define file
using namespace std;

const double pi = acos(-1.0);
int f = 0;
int t;
int n, k;
double arr[55];

int main() {
    #ifdef file
    freopen("C-small-1-attempt2.in", "r", stdin);
    freopen("1out.txt", "w", stdout);
    #endif // file
    scanf("%d", &t);
    while(t--) {
        scanf("%d%d", &n, &k);
        double xx;
        scanf("%lf", &xx);
        double mx, mi;
        mx = 0, mi = 1;

        for(int i = 0; i < n; i++)
            scanf("%lf", &arr[i]), mx = max(mx, arr[i]), mi = min(mi, arr[i]);
        sort(arr, arr + n);
        arr[n] = 1e10;
        double res = 0, sum = 0;
        for(int i = 0; i < n; i++) {
            sum += arr[i];
            double ans = 1;
            double d = (sum + xx)/(i+1);
            bool sign = 0;
            for(int j = 0; j <= i; j++) {
                ans *= d;
                if(arr[j] > d)
                    sign = 1;
            }
            if(sign) continue;
            for(int j = i + 1; j < n; j++)
                ans *= arr[j];
            res = max(res, ans);
        }
        printf("Case #%d: %.10f\n", ++f, res);
    }
    return 0;
}
