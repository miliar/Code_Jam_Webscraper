#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

const int maxn = 1100;
int T, k, Case = 1, n;
char s[maxn];
bool a[maxn];

const int inf = 0x3f3f3f3f;

int f[maxn][2];
int test(int m) {
    f[0][a[0]] = 0;
    f[0][1-a[0]] = inf;
    for(int i = 1; i < m; i++) {
        if(a[i]) {
            f[i][0] = f[i-1][1] + 1;
            f[i][1] = f[i-1][0];
        }
        else {
            f[i][0] = f[i-1][0];
            f[i][1] = f[i-1][1] + 1;
        }
    }
    return f[m-1][0] >= inf ? -1 : f[m-1][0];
}

int main()
{
    scanf("%d", &T);
    while(T--) {
        printf("Case #%d: ", Case++);
        scanf("%s%d", s, &k);
        n = strlen(s);
        bool init_flip = 0;
        for(int i = 0; i < n; i++)
            s[i] = s[i] == '+';
        if(s[0] == 0) {
            init_flip = 1;
            for(int i = 0; i < k; i++)
                s[i] = !s[i];
        }
        for(int i = 0; i < n-1; i++)
            s[i] = s[i] ^ s[i+1];
        int ans = 0;        
        for(int i = 0; i < k && ans != -1; i++) {
            //printf("i=%d\n", i);
            int j = 0, p = i;
            /* construct */
            //if(i == k-1) j++;
            while(p < n-1) {
                a[j++] = s[p];
                p += k;
            }
            /*
            if(i == k-1) {
                a[0] = 0; update(j);
                a[0] = 1; update(j);
            }
            */
            if(p == n-1) {
                int acc1, acc2;
                a[j] = 0; acc1 = test(j+1);
                a[j] = 1; acc2 = test(j+1);
                if(acc1 == -1)
                    if(acc2 == -1) ans = -1;
                    else ans += acc2;
                else
                    if(acc2 == -1) ans += acc1;
                    else ans += min(acc1, acc2);
            }
            else {
                int acc = test(j);
                if(acc == -1) ans = -1;
                else ans += acc;
            }
        }
        if(ans == -1)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", ans + init_flip);
    }
    return 0;
}