#include <cstdio>
#include <cstring>
#include <cstdlib>

#define MEMSET(x) memset(x, 0, sizeof(x))

int main(void){
    int T;
    char N[20];
    char i, j, len;

    scanf("%d", &T);
    for(int t=1; t<=T; t++){
        // initial
        MEMSET(N);

        // input
        scanf("%s", N);

        //  solve
        len = strlen(N);
        i = len-1;
        while( i>0 ){
            if( N[i] < N[i-1] ){
                N[i-1]--;
                N[i] = '9';

                for(j=i+1; j<len; j++)
                    N[j] = '9';-

                i--;
                while( N[i]<0 ){
                    N[i] = '9';
                    N[i-1]--;
                    i--;
                }
            }else{
                i--;
            }
        }

        //  output
        for(i=0; i<len && N[i]=='0'; i++);
        printf("Case #%d: %s\n", t, (N+i));

    }

    return 0;
}
