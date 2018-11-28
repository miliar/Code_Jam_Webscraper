#include <cstdio>
#include <cstring>

#define REP(i,a,b) for (int i = (a); i < (b); ++i)
#define TAM 10000

int main () {

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int TC;
    int k = 0;

    scanf("%d",&TC);

    while (TC--) {

        char panqueques[TAM];
        int tamK;
        scanf("%s %d",panqueques,&tamK);
      //  printf("%s %d\n",panqueques,tamK);

        int len = strlen(panqueques);

        int mov = 0;
   //     printf("%s\n",panqueques);

        REP(i,0,len-tamK+1) {
            if (panqueques[i] == '-') {
                mov++;
                REP(j,i,tamK+i) {
                    if (j > len)                        break;

                    if (panqueques[j] == '-'){
                        panqueques[j] = '+';
                    }else{
                        panqueques[j] = '-';
                    }
                }
            }else {
                continue;
            }
        }

        int flag = 0;

        REP(i,0,len) {
            if (panqueques[i] == '-'){
                flag = 1;
                break;
            }
        }

    //    printf("%s\n",panqueques);

        if (flag)
            printf("Case #%d: IMPOSSIBLE\n",++k);
        else
            printf("Case #%d: %d\n",++k,mov);


    }



return 0;
}
