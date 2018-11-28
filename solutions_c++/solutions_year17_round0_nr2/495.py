#include <cstdio>
#include <cstring>

using namespace std;

int TC, tc;
char s[18 + 5];

int main() {
    freopen("i.in", "r", stdin);
    freopen("o.out", "w", stdout);
    scanf("%d", &TC);
    while(TC--) {
        scanf("%s", s);
        int N = strlen(s);
        int l = -1;
        for(int i = N - 1; i >= 1; i--)
            if(s[i-1]>s[i])
                l = i;

        printf("Case #%d: ", ++tc);
        if(l < 0)
            printf("%s\n", s);
        else {
            for( ; l > 0 && s[l - 1] > s[l]; l--)
                s[l-1]--;
            for(l++; l < N; l++)
                s[l] = '9';
            printf("%s\n", s + (s[0] == '0' ? 1 : 0));
        }
    }
}
