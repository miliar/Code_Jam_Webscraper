#include <bits/stdc++.h>
int T,k;
char a[1003];
int main()
{
    char x='+'^'-';
    scanf("%d",&T);
    for(int t=1;t<=T;++t)
    {
        int ans=0,i,j;
        scanf(" %s %d",a+1,&k);
        for(i=1;a[i+k-1];++i)
            if(a[i]=='-')
            {
                ++ans;
                for(j=i;j<=i+k-1;++j)
                    a[j]^=x;
            }
        printf("Case #%d: ",t);

        for(int j=i;a[j];++j)
            if(a[j]=='-')
            {
                ans=-1;
                break;
            }
        if(ans<0)
            puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
    return 0;
}
