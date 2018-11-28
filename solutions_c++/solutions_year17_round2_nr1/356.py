#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N = 2000;
int n, D;
int pos[N], vel[N];
ll A[N], B[N];
int t[N];
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (int cas=1; cas<=test; cas++){
        scanf("%d %d", &D, &n);
        for (int i=1; i<=n; i++){
            scanf("%d %d", &pos[i], &vel[i]);
            t[i] = i;
        }
//        sort(t+1, t+1+n, cmp);
        for (int i=1; i<=n; i++){
            A[i] = D - pos[i];
            B[i] = vel[i];
        }
        int k = 1;
        for (int i=1; i<=n; i++){

//            if (A[i]/B[i] > A[k]/B[k]) k = i;
            if (A[i] * B[k] > A[k] * B[i]) k = i;
        }
        double ans = 1.0 * D  * B[k] / A[k];
        printf("Case #%d: %.10lf\n", cas, ans);
    }
    fclose(stdout);
    return 0;
}
