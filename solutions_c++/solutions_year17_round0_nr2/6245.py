#include <bits/stdc++.h>
using namespace std;

char s[1000];
int d[1000];

int main() {
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    int cas = 0;
    while(t --) {
        scanf("%s", s);
        int n = strlen(s);
        for(int i = 0; s[i]; i ++) {
            d[i] = s[i]-'0';
        }
        int se = 0;
        int fi = 0;
        for(int i = 1; i < n; i ++) {
            if(d[i] == d[i-1]) {
                se ++;
                continue;
            }
            if(d[i] < d[i-1]) {            
                for(int j = i-se; j < n; j ++) d[j] = 9;
                d[i-se-1] --;
                if(!d[i-se-1]) fi = 1;
                break;
            }
            se = 0;
        }
        printf("Case #%d: ", ++cas);
        for(int i = fi; i < n; i ++) {
            printf("%d", d[i]);
        }   puts("");
    }
}
