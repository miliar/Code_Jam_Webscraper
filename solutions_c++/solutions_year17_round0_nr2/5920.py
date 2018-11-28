#include<cstdio>
using namespace std;
int main()
{
    freopen("large.in","r",stdin);
    freopen("large.out","w",stdout);
    int T;
    char s[50],ans[50];
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%s",s);
        int j=0;
        for(int i=0,flag=0;s[i]!=0;i++)
        {
            if(flag)
            {   ans[j++]='9';    continue;   }
            if(s[i+1]==0||s[i+1]>=s[i])
                ans[j++]=s[i];
            else
            {
                ans[j++]=s[i];
                for(int k=j-1;k>=0;k--)
                {
                    if(k-1>=0&&ans[k-1]<ans[k])
                    {   ans[k]=ans[k]-1;    break;  }
                    if(k-1>=0&&ans[k-1]==ans[k])
                        ans[k]='9';
                    else
                        if(ans[k]=='1')
                        {
                            for(int l=0;l<j-1;l++)
                                ans[l]=ans[l+1];
                            j--;
                        }
                        else
                            ans[k]=ans[k]-1;
                }
                flag=1;
            }
        }
        ans[j++]=0;
        printf("Case #%d: %s\n",t,ans);
    }
    return 0;
}
