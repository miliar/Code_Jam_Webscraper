#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn = 20;
int T, Case = 1, n;
char s[maxn], q[maxn];
int f[maxn], g[maxn];

int main()
{
    scanf("%d", &T);
    while(T--) {
        printf("Case #%d: ", Case++);
        scanf("%s", s);
        n = strlen(s);
        f[n-1] = s[n-1]; g[n-1] = n-1;
        s[n] = 127;
        for(int i = n-2; i >= 0; i--) {
            if(s[i] < f[i+1]) {
                f[i] = s[i];
                g[i] = i+1;
            }
            else {
                f[i] = f[i+1];
                g[i] = g[i+1];
            }
        }
        int i;
        for(i = 0; i < n; i++) {
            q[i] = s[i];
            if(s[i] > s[i+1]) {
                while(i >= 1 && s[i-1] == s[i]) 
                    i--;
                q[i] = q[i]-1;
                for(i=i+1; i < n; i++)
                    q[i] = '9';
                break;
            }
        }
        for(i = 0; i < n; i++) {
            if(i == 0 && q[i] == '0') continue;
            printf("%c", q[i]);
        }
        printf("\n");
    }
    return 0;
}