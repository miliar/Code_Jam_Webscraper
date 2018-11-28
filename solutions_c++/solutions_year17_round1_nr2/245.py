#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int r[50];
vector <int> q[50];

int main() {
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int n, p, ans = 0, j, k;
        
        scanf("%d %d", &n, &p);
        
        for (j = 0; j < n; j++) scanf("%d", &r[j]);
        
        for (j = 0; j < n; j++) {
            q[j].clear();
            
            for (k = 0; k < p; k++) {
                int x;
                
                scanf("%d", &x);
                
                q[j].push_back(x);
            }
            
            sort(q[j].begin(), q[j].end());
            reverse(q[j].begin(), q[j].end());
        }
        
        while (1) {
            int m1 = 1e9, m2 = 0;
            
            for (j = 0; j < n; j++) {
                int x, c1, c2;
                
                if (q[j].size() == 0) break;
                
                x = q[j].back() * 100;
                
                c1 = x / (r[j] * 90);
                c2 = (x + r[j] * 110 - 1) / (r[j] * 110);
                
                if (c1 < c2) {
                    q[j].pop_back();
                    j--;
                    continue;
                }
                
                m1 = min(m1, c1);
                m2 = max(m2, c2);
            }
            
            if (j < n) break;
            
            if (m2 <= m1) {
                ans++;
                
                for (j = 0; j < n; j++) q[j].pop_back();
            } else {
                for (j = 0; j < n; j++) {
                    int x = q[j].back() * 100;
                    if (x / (r[j] * 90) < m2) q[j].pop_back();
                }
            }
        }
        
        printf("Case #%d: %d\n", i + 1, ans);
    }
    
    return 0;
}
