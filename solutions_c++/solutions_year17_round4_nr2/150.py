#include <cstdio>
#include <algorithm>

using namespace std;

int a[1000][2];
int b[1000];
int d[1000];

int main() {
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int n, c, m, p = 0, ans = 0, sum = 0, j;
        
        scanf("%d %d %d", &n, &c, &m);
        
        for (j = 0; j < m; j++) scanf("%d %d", &a[j][0], &a[j][1]);
        
        for (j = 0; j < n; j++) b[j] = 0;
        for (j = 0; j < c; j++) d[j] = 0;
        
        for (j = 0; j < m; j++) {
            b[a[j][0] - 1]++;
            d[a[j][1] - 1]++;
        }
        
        ans = max(ans, (m + n - 1) / n);
        for (j = 0; j < c; j++) ans = max(ans, d[j]);
        
        for (j = 0; j < n; j++) {
            p += b[j];
            ans = max(ans, (p + j) / (j + 1));
        }
        
        for (j = 0; j < n; j++) sum += max(b[j] - ans, 0);
        
        printf("Case #%d: %d %d\n", i + 1, ans, sum);
    }
    
    return 0;
}
