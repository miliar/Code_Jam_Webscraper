#include<stdio.h>
#include<string.h>
int test,n,m;
char s[1005];
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,p,ans;
    scanf("%d",&test);
    for(p=1;p<=test;p++){
        scanf("%s %d",s,&m);
        printf("Case #%d: ",p);
        n=strlen(s);
        ans=0;
        for(i=0;i<=n-m;i++){
            if(s[i]=='+')   continue;
            ans++;
            for(j=0;j<m;j++)    s[i+j]=(s[i+j]-'+')?'+':'-';
        }
        for(j=0;j<m;j++){
            if(s[n-j-1]-'+')    break;
        }
        if(j==m)    printf("%d\n",ans);
        else    printf("IMPOSSIBLE\n");
    }
    return 0;
}
