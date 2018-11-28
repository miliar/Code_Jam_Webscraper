#include<cstdio>
#include<cstring>
using namespace std;

char s[1005];
void reverse(int x)
{
    s[x]=(s[x]=='+'?'-':'+');
}

int main()
{
    int T;
    scanf("%d",&T);
    int k;
    for(int cas=1;cas<=T;++cas)
    {
        scanf("%s%d",s,&k);
        int len=strlen(s);
        int cnt=0;
        for(int i=0;i<len-k+1;++i)
        {
            if(s[i]=='-')
            {
                ++cnt;
                for(int j=i;j<i+k;++j)
                    reverse(j);
            }
        }
        bool flag=false;
        for(int i=len-k+1;i<len;++i)
            if(s[i]=='-')
            {
                printf("Case #%d: %s\n",cas,"IMPOSSIBLE");
                flag=true;
                break;
            }
        if(!flag)
            printf("Case #%d: %d\n",cas,cnt);
    }
    return 0;
}
