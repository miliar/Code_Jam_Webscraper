#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

char str[20];
void solve (void)
{
    int i,len = strlen(str);

    for(i = len-1; i>0; i--){
        if(str[i-1] > str[i]){
            str[i-1]--;
            for(int j=i; j<len; j++)
                str[j]='9';
        }
    }

    i=0;
    while(str[i]=='0') i++;

    for(;i<len;i++)
        printf("%c",str[i]);
    printf("\n");

    return ;
}
int main (void)
{
    int i,T;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&T);

    for(i=0;i<T;i++){
        scanf("%s",str);
        printf("Case #%d: ",i+1);
        solve();
    }


    return 0;
}
