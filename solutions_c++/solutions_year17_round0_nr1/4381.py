#include<cstdio>
#include<cstring>
using namespace std;

char s[1001];
int k, T;

int main()
{
    scanf("%d", &T);
    int cas = 0;
    while(T--) {
        scanf("%s %d", s, &k);
        int ans = 0, len = strlen(s);
        for (int i = 0; i < len; i++) {
            if (s[i] == '-'){
                if (i <= len - k) {
                    ans ++;
                    for (int j = i; j < i+k; j++)
                        s[j] = s[j]=='+'?'-':'+';
                }
                else{
                    ans = -1;
                    break;
                }
            }
        }
        if (ans == -1)
            printf("Case #%d: IMPOSSIBLE\n", ++cas);
        else
            printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}
