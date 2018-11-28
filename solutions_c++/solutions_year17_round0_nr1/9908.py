#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    char a[1005];
    int kase=0;
    while(t--)
    {
        bool flag=true;
        int k;
        int cnt=0;
        scanf("%s",a);
        scanf("%d",&k);
        int len=strlen(a);
        for(int i=0;i<len;i++)
            if(a[i]!='+')
            {
                flag=false;
                break;
            }
        if(!flag)
        {
            for(int i=0;i<=len-k;i++)
            {
                if(a[i]=='-')
                {
                    for(int j=0;j<k;j++)
                        if(a[i+j]=='-')
                            a[i+j]='+';
                        else
                            a[i+j]='-';
                    ++cnt;
                }
            }
            bool f=true;
            for(int i=0;i<len;i++)
                if(a[i]!='+')
                {
                    f=false;
                    break;
                }
            if(f)
                printf("Case #%d: %d\n",++kase,cnt);
            else
                printf("Case #%d: IMPOSSIBLE\n",++kase);
        }
        else
            printf("Case #%d: 0\n",++kase);
    }
    return 0;
}
