#include<cstdio>
#include<cstring>
using namespace std;
const int maxn=1e3+200;
char s[maxn];
int main()
{
    //freopen("F:\\Users\\zheng\\Desktop\\A-large.in","r",stdin);
    //freopen("F:\\Users\\zheng\\Desktop\\A.txt","w",stdout);
    int T,ca=1;scanf("%d",&T);
    while(T--)
    {
        int k,ans=0;
        scanf("%s%d",s,&k);
        int len=strlen(s);
        for(int i=0;i<len;i++)
            if(s[i]=='-'&&i+k-1<len)
            {
                for(int j=0;j<k;j++)
                    s[i+j]=(s[i+j]=='-'?'+':'-');
                ans++;
            }
        int f=0;
        for(int i=0;i<len;i++)
            if(s[i]=='-')
            {
                f=1;break;
            }
        if(f)printf("Case #%d: IMPOSSIBLE\n",ca++);
        else printf("Case #%d: %d\n",ca++,ans);
    }
    return 0;
}
