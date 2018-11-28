#include <cstdio>
#include <cstring>

bool cake[2000];
char S[2000];

int T, K;
int len, solved;
int sum;

void reverse(int p){
    sum++;
    for(int i=p; i<p+K; i++)
        cake[i] = (!cake[i]);
}

int main(){
    while(~scanf("%d", &T)){
        for(int t=1; t<=T; t++){
            scanf("%s %d", S, &K);
            len = strlen(S);
            for(int i=0; i<len; i++){
                if(S[i]=='-')
                    cake[i] = false;
                else if(S[i]=='+')
                    cake[i] = true;
            }
            sum = 0;
            for(int i=0; i<=len-K; i++){
                if(!cake[i])
                    reverse(i);
            }
            solved=1;
            for(int i=len-1; i>=0; i--){
                if(!cake[i]){
                    solved = 0;
                    break;
                }
            }
            if(solved)
                printf("Case #%d: %d\n", t, sum);
            else
                printf("Case #%d: IMPOSSIBLE\n", t);
        }
    } 
}
