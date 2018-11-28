#include <bits/stdc++.h>
#define LL long long int
using namespace std;

const int INF = 0x7FFFFFFF;

void
Filework(){
    freopen("alarge.in", "r", stdin);
    freopen("alarge.out", "w", stdout);
}

char s[10005];
int k;

int
main(){

    Filework();

    int T;
    int t;
    int i, j;
    int flag;
    int num;

    scanf("%d", &T);
    for(t = 1; t <= T; t ++){
        scanf("%s", s);
        scanf("%d", &k);
        flag = 1;
        num = 0;
        for(i = 0; i < strlen(s) && (flag == 1); i ++){
            if(s[i] == '-'){
                if(i + k - 1 > strlen(s) - 1){
                    flag = 0;
                    break;
                }
                for(j = 0; j < k; j ++){
                    if(s[j + i] == '-'){
                        s[j + i] = '+';
                    }
                    else
                        s[j + i] = '-';
                }
                num ++;
            }
        }

        printf("Case #%d: ", t);

        if(!flag){
            printf("IMPOSSIBLE\n");
        }
        else{
            printf("%d\n", num);
        }
    }


return 0;
}
