#include<cstdio>
#include<stdlib.h>

bool mm()
{
    int n;
    int a[6];
    scanf("%d",&n);
    for(int i=0;i<6;i++)
    {
        scanf("%d",&a[i]);
    }
    char ans[n+1];
    int cnt = 0;
    for(int i=0;i<n;i++)
    {
        while(a[cnt]==0)cnt+=2;
        if(cnt == 0)ans[i] = 'R';
        else if(cnt == 2)ans[i] = 'Y';
        else if(cnt == 4)ans[i] = 'B';
        a[cnt]--;
    }
    ans[n] = '\0';
    for(int i=1;i<n;i++)
    {
        bool chk = false;
        if(i == n-1)
        {
            if(ans[i-1] == ans[i] || ans[0] == ans[i])chk = true;
        }
        else
        {
            if(ans[i-1] == ans[i] || ans[i+1] == ans[i])chk = true;
        }
        if(chk)
        {
            bool exchk = true;
            for(int j=0;j<n;j++)
            {
                bool ccc = false;
                if(j>0) ccc = ans[j-1] !=ans[i] && ans[j]!=ans[i];
                else ccc = ans[n-1] !=ans[i] && ans[j]!=ans[i];
                if(ccc)
                {
                    exchk = false;
                    int ii,jj;
                    if(j == 0)
                    {
                        ii = i;
                        jj = 0;
                    }
                    else if(i>j)
                    {
                        ii = i;
                        jj = j;
                    }
                    else
                    {
                        ii = j;
                        jj = i;

                    }
                    for(int k=ii;k>jj;k--)
                    {
                        char tmp = ans[k];
                        ans[k] = ans[k-1];
                        ans[k-1] = tmp;
                    }

                    break;
                }
            }
            if(exchk)
            {
                //printf("%s\n",ans);
                return false;
            }
        }
    }
    printf("%s\n",ans);
    return true;
}
main()
{
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        printf("Case #%d: ",i+1);
        if(!mm())printf("IMPOSSIBLE\n");
    }
}
