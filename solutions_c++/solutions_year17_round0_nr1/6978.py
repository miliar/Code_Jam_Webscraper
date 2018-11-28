#include <stdio.h>

#define NUM(x) (x - '0')

char buffer[1001];
int pan;
int TC;
int answer;

int main(){
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);

    int T; scanf("%d", &T); while(T--){
        // init
        answer = 0;

        // input
        scanf("%s %d", buffer, &pan);

        // process
        for(int start = 0; buffer[start + pan - 1] != NULL; start++){
            if(buffer[start] == '-'){
                answer++;
                for(int i = 0; i < pan; i++)
                    buffer[start + i] = buffer[start + i] == '-' ? '+' : '-';
            }
        }

        for(int start = 0; buffer[start] != NULL; start++)
            if(buffer[start] == '-') answer = -1;

        // output
        if(answer == -1)
            printf("Case #%d: %s\n", ++TC, "IMPOSSIBLE");
        else
            printf("Case #%d: %d\n", ++TC, answer);
    }
    return 0;
}
