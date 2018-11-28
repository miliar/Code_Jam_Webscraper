# include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("Aout.txt", "w", stdout);
    int cases, caseno=0, k, sum;
    char str[1009];
    scanf("%d", &cases);
    while(cases--){
        sum = 0;
        scanf("%s %d", str, &k);
        int len = strlen(str);
        for (int i=0; i<=len-k; i++){
            if (str[i]=='+') continue;
            sum++;
            for (int j=0; j<k; j++){
                if (str[i+j]=='+') str[i+j] = '-';
                else str[i+j] = '+';
            }
        }
        for (int i=len-k+1; str[i]; i++){
            if (str[i]=='-'){
                sum = -1;
                break;
            }
        }
        if (sum != -1) printf("Case #%d: %d\n", ++caseno, sum);
        else printf("Case #%d: IMPOSSIBLE\n", ++caseno);
    }
    return 0;
}
