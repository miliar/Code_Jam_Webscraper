#include<bits/stdc++.h>
using namespace std;

char s[555];

int main() {

    int n,i,tr,ima0;

    int ttt;
    scanf("%d", &ttt);
    for(int tt=1; tt<=ttt; tt++) {
        printf("Case #%d: ", tt);

        scanf("%s", &s);
        n = strlen(s);

        tr = 0;
        for(i=1; i<n; i++) {
            if (s[i] == s[i-1]) continue;
            if (s[i] > s[i-1]) {
                for(;tr<i; tr++) printf("%c", s[tr]);
            } else {
                if (s[tr]>'1') printf("%c", s[tr]-1);
                tr++;
                for(;tr<n;tr++) printf("9");
                break;
            }
        }
        for(;tr<n; tr++) printf("%c", s[tr]);

        printf("\n");
    }

    return 0;
}
