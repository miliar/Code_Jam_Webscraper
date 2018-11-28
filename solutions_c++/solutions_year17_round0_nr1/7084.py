#include<bits/stdc++.h>
using namespace std;
int main(){

    freopen("A-large.in", "r", stdin);
    freopen("output.in", "w", stdout);

    int t, k , cou , kase = 1;
    char cake[100000];

    scanf("%d",&t);
    while(t-->0){
            cou = 0;
        scanf("%s",&cake);
        scanf("%d",&k);
        for(int i = 0 ;i <= strlen(cake)-k;i++){
            if(cake[i]=='-'){
                    int f = k+i;
                    if(f>strlen(cake)){
                        f = strlen(cake);
                    }
                    int g = i;
                    for(g; g < f;g++){
                        if(cake[g]=='-'){
                            cake[g]='+';
                        }
                        else{
                            cake[g]='-';
                        }
                    }
                    cou++;
            }
        }
        int i=0;
        for(i = 0 ;i < strlen(cake);i++){
            if(cake[i]=='-'){
                printf("Case #%d: IMPOSSIBLE\n",kase++);
                break;
            }
        }
        if(i==strlen(cake)){
            printf("Case #%d: %d\n",kase++,cou);
        }
    }

return 0;
}
