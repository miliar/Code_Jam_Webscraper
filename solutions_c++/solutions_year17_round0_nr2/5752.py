#include <cstdio>
#include <cstring>
using namespace std;
int isOk(char * number){
    int len = strlen(number) - 1;
    for(int i = 0; i < len; i++)
        if(number[i] > number[i + 1])
            return i;
    return -1;
}
int main()
{
    int t,ok,i;
    char number[20];
    freopen("ex2.in","r",stdin);
    freopen("ex2.out","w",stdout);
    scanf("%d",&t);
    for(int caseNumber = 1; caseNumber <= t; caseNumber++){
        scanf("%s",number);
        ok = isOk(number);
        if(ok == -1)
            printf("Case #%d: %s\n",caseNumber, number);
        else
            {
                number[ok] -= 1;
                while(ok>0 && number[ok - 1] > number[ok]){
                    ok--;
                    number[ok] -= 1;
                }
                printf("Case #%d: ", caseNumber);
                for(i = 0; i < ok; i++){
                    printf("%c",number[i]);
                }
                if(number[ok] != '0')
                    printf("%c", number[ok]);
                i++;
                while(i < strlen(number)){
                    printf("9");
                    i++;
                }
                printf("\n");
            }
    }
    return 0;
}
