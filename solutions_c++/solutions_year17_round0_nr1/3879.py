#include <iostream>



#include<cstring>





char s[10005];
int k,n;
#define fr(i,x,y) for(int i=x;i<=y;i++)

void doit()
{
    scanf("%s%d",s,&k);
    n=strlen(s);
    int ans=0;
    fr(i,0,n-1)if (s[i]=='-')
    {
        if (i+k<=n)
        fr(j,i,i+k-1)
            if (s[j]=='-') s[j]='+';else s[j]='-';

        else{
                printf("IMPOSSIBLE\n"); return;
            }
        //printf("%s\n",s);
        ans++;
    }
    printf("%d\n",ans);
}






int main() {
    int cas;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    scanf("%d",&cas);
    int id=0;
    while (cas--)
    {
        printf("Case #%d: ",++id);
        doit();
    }
    return 0;
}