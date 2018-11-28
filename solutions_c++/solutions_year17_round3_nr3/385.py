#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <utility>
#include <map>
#include <cstring>
#include <vector>
using namespace std;

int nTest;
typedef pair<int,int> ii;
double a[55];
int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    scanf("%d", &nTest);
    for (int test = 1; test <= nTest; test++){
        printf("Case #%d: ", test);
        int n, k;
        scanf("%d %d", &n, &k);
        double u;
        scanf("%lf", &u);
        for (int i = 0; i < n; i++){
            scanf("%lf", a + i);
        }
        a[n] = 1.0;
        sort(a, a + n + 1);
        double lowest = a[0];
        for (int i = 1; i <= n; i++){
            double last = a[i - 1] * (double)i;
            double curr = a[i] * (double)i;

            if (u > curr - last || abs(u - (curr - last)) < 1E-8){
                u -= curr - last;
                lowest = a[i];
                continue;
            } else {
                lowest = (u + last) / (double)i;
                break;
            }
        }
        for (int i = 0; i < n; i++)
            if (a[i] < lowest) 
                a[i] = lowest;


        double ans = 1.0;
        for (int i = 0; i < n; i++){
            ans *= a[i];
        }
        printf("%.9lf\n", ans);
    }
}