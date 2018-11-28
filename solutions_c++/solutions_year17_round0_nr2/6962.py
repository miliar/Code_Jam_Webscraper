#include <stdio.h>

#define NUM(x) (x - '0')

char buffer[100][20];
int TC;

inline int getLength(char *str){
    int length = 0;
    while(str[length] != NULL) length++;
    return length;
}

int main(){
    freopen("B-large.txt", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T; scanf("%d", &T); while(T--){
        // input
        scanf("%s", buffer[T]);

        // process
        int length = getLength(buffer[T]);
        int maxIndex = -1;
        int amend = 0;

        for(int i = 0; i < length - 1; i++){
            if (NUM(buffer[T][i]) > NUM(buffer[T][i + 1])){
                maxIndex = i;
                break;
            }
        }

        if(maxIndex >= 0){
            buffer[T][maxIndex]--;
            for(int i = maxIndex + 1; i < length; i++) buffer[T][i] = '9';
            while(maxIndex > 0){
                if(NUM(buffer[T][maxIndex - 1]) > NUM(buffer[T][maxIndex])){
                    buffer[T][maxIndex - 1]--;
                    buffer[T][maxIndex] = '9';
                    maxIndex--;
                }
                else
                    break;
            }
            amend = maxIndex == 0 && buffer[T][0] == '0'? 1 : 0;
        }

        // output
        printf("Case #%d: %s\n", ++TC, &(buffer[T][0 + amend]));
        fflush(stdout);
    }
    return 0;
}
