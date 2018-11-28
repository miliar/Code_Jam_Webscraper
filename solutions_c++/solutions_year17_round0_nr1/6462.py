#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int t,k;
char s[1010];

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("data.out","w",stdout);
    scanf("%d",&t);
    for(int q=1;q<=t;++q)
    {
        scanf("%s%d",s,&k);
        int i,ans=0;
        for(i=0;s[i+k-1]!='\0';++i)
        {
           // printf("i=%d\n",i);
            if(s[i]=='-')
            {
                for(int j=0;j<k;++j) if(s[j+i]=='-') s[j+i]='+';else s[j+i]='-';
                ans++;
            }
        }
        bool flag=0;
        for(int j=i;s[j]!='\0';++j) if(s[j]=='-') { flag=1;break; }
        printf("Case #%d: ",q);
        if(flag) puts("IMPOSSIBLE");else printf("%d\n",ans);
    }
    return 0;
}
