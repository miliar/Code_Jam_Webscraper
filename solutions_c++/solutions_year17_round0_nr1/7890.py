#include<stdio.h>
#include<string.h>
int main(){
    int t,i;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        char s[1000];
        int k,ans,l,j;
        scanf("%s",s);
        scanf("%d",&k);
        ans=0;j=k;
        for(l=0;l<strlen(s);l++){
            if(s[l]=='-'){
                //printf("tui");
                ans++;
                for(j=0;j<k;j++){
                    if((l+j)>=strlen(s))
                    goto yoho;
                else if(s[l+j]=='-')
                s[l+j]='+';
                else
                s[l+j]='-';
                //puts(s);
            }
        }
    }
    yoho:
    if(j<k)
    ans=-1;
    else{
    for(l=0;l<strlen(s);l++){
        if(s[l]=='-')
        {
            ans=-1;
            break;
        }
    }}
    if(ans==-1)
    printf("Case #%d: IMPOSSIBLE\n",i);
    else
    printf("Case #%d: %d\n",i,ans);
}}
