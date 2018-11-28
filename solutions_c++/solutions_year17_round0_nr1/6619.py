#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;


int t,k;
char s[1005];

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    scanf("%d",&t);
    int z=1;
    while(t--)
    {
        scanf("%s %d",s,&k);
        int len=strlen(s);
        int flag,ff;
        int ans=0;
        while(1)
        {
            flag=0,ff=0;
            for(int i=0;i<len;++i)
            {
                if(s[i]=='-')
                {
                    if(i>len-k)
                    {
                        flag=1;
                        break;
                    }
                    ans++;
                    for(int j=i;j<i+k;++j)
                    {
                        if(s[j]=='-') s[j]='+';
                        else s[j]='-';
                    }
                }
            }
            if(flag==1) break;
            ff=0;
            for(int i=0;i<len;++i)
                if(s[i]=='-') ff=1;
            if(ff==0) break;
        }
        printf("Case #%d: ",z++);
        if(flag)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
        if(ff==0) printf("%d\n",ans);
    }
}
