#include <stdio.h>

void flip(char *s, int k){
    for(int i=0; i<k; ++i){
        if(s[i]=='-'){
            s[i] = '+';
        }else{
            s[i] = '-';
        }
    }
}

int solve(char *s, int k){
    int n = 0;
    while(s[n]){
        ++n;
    }
    int cnt = 0;
    for(int i=0; i+k <= n; ++i){
        if(s[i]=='-'){
            flip(s+i, k);
            ++cnt;
        }
    }
    for(;i<n;++i){
        if(s[i]=='-'){
            return -1;
        }
    }
    return cnt;
}

int main(){
    int T;
    scanf("%d", &T);
    for(int t=1;t<=T;++t){
        int k;
        char buffer[1002];
        scanf("%s %d", buffer, &k);
        
        int sol = solve(buffer, k);
        if(sol==-1){
            printf("Case #%d: IMPOSSIBLE\n", t);
        }else{
            printf("Case #%d: %d\n", t, sol);
        }
    }
    return 0;
}


