#include<bits/stdc++.h>
using namespace std;
#define N 1005
int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t,c,i,j,k,l,fg,ans,a[N];
    char s[N];
    scanf("%d",&t);
    for(c=1;c<=t;c++){
        scanf("%s%d",s,&k);
        l=strlen(s);
        for(i=0;i<l;i++) a[i]=s[i]=='+';
        for(ans=i=0;i<=l-k;i++)
            if(!a[i])for(ans++,j=0;j<k;j++) a[i+j]^=1;
        for(fg=0;i<l;i++)if(!a[i]) { fg=1;break; }
        printf("Case #%d: ",c);
        if(fg) puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
}
