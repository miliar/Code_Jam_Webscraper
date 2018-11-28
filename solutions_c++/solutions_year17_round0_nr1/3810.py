#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int T,k;
char s[1005];

void solve (void)
{
    int len = strlen(s), cnt = 0;

    for(int i=0;i<len-k+1;i++){
        if(s[i]=='-'){
            cnt++;
            for(int j=i;j<i+k;j++)
                s[j]=(s[j]=='+'?'-':'+');
        }
    }

    for(int i=len-k+1;i<len;i++){
        if(s[i]=='-'){
            puts("IMPOSSIBLE");
            return ;
        }
    }

    printf("%d\n",cnt);

    return ;
}
int main (void)
{
    int i;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);

    for(i=0;i<T;i++){
        scanf("%s %d",&s,&k);
        printf("Case #%d: ",i+1);
        solve();
    }

    return 0;
}
