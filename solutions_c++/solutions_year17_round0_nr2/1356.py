#include <cstdio>
#include <cstring>
int t,n;
char s[23];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas) {
        scanf("%s",s);
        n=strlen(s);
        for (int i=n-1;i>=1;--i)
            if (s[i-1]>s[i]) {
                --s[i-1];
                for (int j=i;j<n;++j)
                    s[j]='9';
            }
        int id=0;
        while (s[id]=='0')
            ++id;
        printf("Case #%d: %s\n",cas,s+id);
    }
    return 0;
}
