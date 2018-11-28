#include <stdio.h>
#include <string.h>



char p[1010];

int main() {
    int t, n;
    scanf("%d", &t);
    for (int o=1; o<=t; o++) {
        int flg;
        scanf("%s", p);
        n = strlen(p);
        flg = false;
        for (int i=0; i<n-1; i++) {
            if (p[i]>p[i+1]) {
                int k;
                for (k=i; k>=0 && p[i]==p[k]; k--)
                    ;
                k++;
                p[k]--;
                for (int j=k+1; j<n; j++)
                    p[j] = '9';
                break;
            }
        }
        int k;
        for (k=0; p[k]=='0'; k++)
            ;
        printf("Case #%d: %s\n", o, p+k);
    }
}
