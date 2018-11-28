#include<stdio.h>
#include<string.h>


char s[100],m;

int main(){
    int n,k,i,j,x,y;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&n);

    for(i=1;i<=n;i++){
        scanf("%s",s);
        m=strlen(s);

        j=1;
        while(s[j]){
            if(s[j]<s[j-1]){
                s[j-1]--;
                for(x=j;x<m;x++) s[x]='9';
                j=1;
            }else j++;
        }
        printf("Case #%d: ",i);
        for(j=0;j<m;j++){
            if(s[j]>'0') break;
        }
        for(;j<m;j++){
            printf("%c",s[j]);
        }
        printf("\n");
    }

    return 0;
}
