#include <cstdio>
#include <cstring>
using namespace std;

const int SLEN = 1010;
char str[SLEN];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, k, cse = 1;
    scanf("%d", &T);
    while(T--) {
        scanf("%s%d", str, &k);
        int len = strlen(str), cnt = 0;
        for(int i = 0; i < len; i++) {
            if(str[i] == '-') {
                if(i + k > len) continue;
                for(int j = i; j < i + k; j++) {
                    if(str[j] == '+') str[j] = '-';
                    else str[j] = '+';
                }
                cnt++;
            }
        }
        bool flag = true;
        for(int i = 0; i < len; i++) {
            if(str[i] == '-') {
                flag = false;
                break;
            }
        }
        printf("Case #%d: ", cse++);
        if(!flag) puts("IMPOSSIBLE");
        else printf("%d\n", cnt);
    }
    return 0;
}
