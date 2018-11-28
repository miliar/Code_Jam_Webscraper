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
vector<ii> v;
double f[1111][1111];
int r[1111], h[1111];
double PI = 3.14159265358979323846;
int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    scanf("%d", &nTest);
    for (int test = 1; test <= nTest; test++){
        printf("Case #%d: ", test);
        int n, k;
        scanf("%d %d", &n, &k);
        for (int i = 0; i <= k; i++){
            for (int j = 0; j <= n; j++){
                f[i][j] = 0.0;
            }
        }
        v.clear();
        for (int i = 1; i <= n; i++){
            scanf("%d %d", r + i, h + i);
            v.push_back(ii(r[i], h[i]));
        }
        sort(v.begin(), v.end());

        for (int i = n - 1; i >= 0; i--){
            r[n - i] = v[i].first;
            h[n - i] = v[i].second;
            // printf("1\n");
        }

        double ans = 0.0;
        for (int i = 1; i <= k; i++){
            for (int j = i; j <= n; j ++){
                if (i == 1){
                    double S = PI * r[j] * r[j];
                    double P = 2.0 * PI * r[j];
                    f[i][j] = max(f[i][j - 1], S + P * h[j]);
                } else {
                    double P = 2.0 * PI * r[j];
                    f[i][j] = max(f[i][j - 1], f[i - 1][j - 1] + P * h[j]);
                }
                // printf("%.9lf ", f[i][j]);
                ans = max(ans, f[i][j]);
            }
            // printf("\n");
        }
        // printf("\n");
        printf("%.9lf\n", ans);
    }
}