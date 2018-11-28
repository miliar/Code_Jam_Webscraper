#include <stdio.h>
#include <string.h>

#define LARGE

using namespace std;

int T;
char S[25];

char* tidy(char s[]) {
    int len = strlen(s);
    if (len == 1) return s;
    for (int i=1; i<len; i++) {
        if (s[i] < s[i-1])
        {
            for (int j=i; j<len; j++) s[j] = '9';
            s[i-1] --;
            for (int j=i - 1; j>0; j--)
            {
                if ( s[j] < s[j-1] )
                {
                    s[j] = '9';
                    s[j-1] --;
                }
                else break;
            }
            break;
        }
    }
    if (s[0] == '0') return s+1;
    return s;
}

int main () {
    freopen("sol.out", "w", stdout);
    #if defined CUSTOM
    freopen("sol.in", "r", stdin);
    #elif defined SMALL
    freopen("B-small-attempt0.in", "r", stdin);
    #elif defined LARGE
    freopen("B-large.in", "r", stdin);
    #endif

    scanf("%d", &T);

    for (int i=1; i<=T; i++) {
        printf("Case #%d: ", i);
        scanf("%s",S);
        char* tmp = tidy(S);
        printf("%s\n", tmp);
    }
    return 0;
}
