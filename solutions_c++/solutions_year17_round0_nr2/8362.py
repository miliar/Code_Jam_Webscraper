#include <stdio.h>
#include <string.h>

char S[100];

void println(char * S){
    int n = strlen(S);
    int j;
    for(j = 0; j < n; j++){
        if( S[j]!='0') break;
    }
    for(int k = j; k < n; k++)
        printf("%c", S[k]);
    printf("\n");
}

bool istidy(char * S){

    int n = strlen(S);
    for(int j = 0; j < n-1; j++){
        if( S[j] > S[j+1] ) return false;
    }
    return true;
}


int main(){
    int T;

    scanf(" %d ", &T);

    for(int i = 0; i < T; i++){

        gets(S);

        int n = strlen(S);

        while( !istidy(S) ){

            int j;
            for(j = 0; j < n-1; j++){
                if( S[j] > S[j+1] ){
                    //printf("altera digito %d\n", j);
                    int x = S[j]-'0';
                    x--;
                    //printf("x %d\n", x);
                    S[j] = '0'+x;

                    break;
                }
            }

            if(j<n-1){
                for(int k = j+1; k < n; k++){
                    S[k] = '9';
                }
            }

            //printf("resultado parcial %s\n", S);

        }

        //printf("resultado final %s\n", S);

        printf("Case #%d: ", i+1);
        println(S);
    }


}
