#include<cstdio>
#include<cstring>

int main()
{
    int t = 0;
    scanf("%d",&t);
    for(int cs=1;cs<=t;cs++)
    {
        char st[2000];
        bool rn[2000] = {false};
        int k;
        scanf("%s",st);
        scanf("%d",&k);
        int ht = 0,ed = strlen(st);
        for(int i=0;i<ed;i++)
        {
            if(st[i] == '+') rn[i] = 0;
            else rn[i] = 1;
        }
        int count = 0;
        for(int i=0;i<=ed-k;i++)
        {
            if(rn[i] == 1)
            {
                count++;
                for(int j=i;j<i+k;j++)
                {
                    rn[j] = !rn[j];
                }
            }
        }
        bool chk = true;
        for(int i=ed-k;i<ed;i++)
        {
            if(rn[i] != 0) chk = false;
        }
/*
        for(int i=0;i<ed;i++)
        {
            printf("%d", rn[i]);
        }
        printf(" %d\n",count);
*/
        printf("Case #%d: ", cs);
        if(chk)
            printf("%d\n",count);
        else
            printf("IMPOSSIBLE\n");
    }
    return 0;
}
