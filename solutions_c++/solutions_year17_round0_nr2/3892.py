#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define FIN freopen("B-large.in", "r", stdin)
#define FOUT freopen("B-large.out", "w", stdout)

void print_s(char *s) {
    if(s[0] == '0') {
        puts(s + 1);
    }
    else {
        puts(s);
    }
}

int main() {
    FIN;
    FOUT;
    int T, ncase = 0;
    long long x;
    scanf("%d", &T);
    while(T--) {
        char s[20], ss[20];
        scanf("%I64d", &x);
        sprintf(s,"%I64d", x);
        int change_pos = -1;
        int last_max = -1;
        for(int i = 0; s[i]; ++i) {
            if(s[i] > last_max) {
                last_max = s[i];
                change_pos = i;
            }
            else if(s[i] < last_max) {
                s[change_pos] -= 1;
                for(int j = change_pos + 1; s[j]; ++j) {
                    s[j] = '9';
                }
                break;
            }
        }
        printf("Case #%d: ", ++ncase);
        print_s(s);
    }
    return 0;
}
