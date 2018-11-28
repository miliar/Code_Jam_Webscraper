#include<cstdio>
#include<cstring>
char str[1010];
int main()
{
    int q,k;
    scanf("%d",&q);
    for(int i = 1; i<=q; i++)
    {
        scanf(" %s %d",str,&k);
        printf("Case #%d: ",i);
        int len = strlen(str);
        if(k>len)
        {
            bool ch = true;
            for(int j=0; j<len; j++)
                if(str[j]=='-')
                {
                    ch=false;
                    break;
                }
            if(!ch)printf("IMPOSSIBLE\n");
            else printf("0\n");
        }
        else
        {
            int cnt=0;
            for(int j=0; j<=len-k; j++)
            {
                if(str[j]=='-')
                {
                    for(int l=0; l<k; l++)
                    {
                        if(str[j+l]=='+')str[j+l]='-';
                        else if(str[j+l]=='-')str[j+l]='+';
                    }
                    cnt++;
                }
            }
            bool ch = false;
            for(int j=0; j<len; j++)
                if(str[j]=='-')ch=true;
            if(ch)printf("IMPOSSIBLE\n");
            else printf("%d\n",cnt);
        }

    }
    return 0;
}
