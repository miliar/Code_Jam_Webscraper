#include <stdio.h>

int T, ans;
int tidyNum[20];

void tidy(int i, int s){
    if(i == s-1) return;
    if(tidyNum[i] > tidyNum[i+1]){
        tidyNum[i]--;
        for(int j = i+1; j < s; ++j){
            tidyNum[j] = 9;
        }
        return;
    }
    tidy(i+1, s);
}
int main(){
//     freopen("/Users/depa/Downloads/B-large.in", "r", stdin);
    scanf("%d", &T);
    for(int t = 1; t <= T; ++t){
        
        char input[20];
        scanf("%s", input);
        int s = 0;
        for(int i = 0; input[i] != '\0'; ++i){
            tidyNum[i] = input[i] - '0';
            s++;
        }
        
        for(int i = s - 2; i >= 0; --i){
            tidy(i, s);
        }
        
        printf("Case #%d: ", t);
        
        for(int i = 0; i < s; ++i){
            
            if(i == 0){
                if(tidyNum[i] > 0)
                    printf("%d", tidyNum[i]);
            }
            else
                printf("%d", tidyNum[i]);
        }
        
        printf("\n");
    }
    
    return 0;
}
