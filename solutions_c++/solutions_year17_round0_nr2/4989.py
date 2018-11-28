# include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("Bout.txt", "w", stdout);
    int cases, caseno = 0, firstNonZero;
    char N[20];
    scanf ("%d", &cases);
    while(cases--){
        scanf("%s", N);
        firstNonZero = 0;
        int len = strlen(N);
        for (int i=len-1; i>0; i--){
            if (N[i] >= N[i-1]) continue;
            while(N[i-1]=='0') i--;
            N[i-1]--;
            for (int j=i; j<len; j++) N[j] = '9';
        }
        for (int i=0; i<len; i++){
            if (N[i]!='0'){
                firstNonZero = i;
                break;
            }
        }
        printf("Case #%d: %s\n", ++caseno, N+firstNonZero);
    }
    return 0;
}
