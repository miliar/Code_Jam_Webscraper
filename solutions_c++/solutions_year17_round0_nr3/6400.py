#include<stdio.h>
#define N (1010)
int l[N], r[N], v[N];
int main(){
    int T;
    scanf("%d",&T);
    for (int tc= 1; tc <= T; tc++){
        int n, k;
        printf("Case #%d: ",tc);
        scanf("%d %d",&n, &k);
        v[0] = v[n + 1] = 1;
        for (int i=1;i<=n;i++){
            l[i] = i - 1;
            r[i] = n - i;
            v[i] = 0;
        }
        int cmin, cmax, xmin, xmax, pos;
        for (int i = 1; i <= k; i++){
            cmin = -1, cmax = -1;
            for (int j = 1;j<=n;j++)
            if (!v[j]){
                if (l[j] < r[j]){
                    xmin = l[j];
                    xmax = r[j];
                }
                else {
                    xmin = r[j];
                    xmax = l[j];
                }
                if (xmin > cmin || xmin == cmin && xmax > cmax){
                    pos = j;
                    cmin = xmin;
                    cmax = xmax;
                }
            }
            v[pos] = 1; 
            for (int u = pos + 1; !v[u]; u++){
                l[u] = u - pos - 1;
            }
            for (int u = pos - 1; !v[u]; u--){
                r[u] = pos - u - 1;
            }
        }
        printf("%d %d\n",cmax, cmin);
    }
}
