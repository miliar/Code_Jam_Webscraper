#include<cstdio>
#include<cstring>
char str[1010],ans[1010];
bool ch=true;
void sol()
{

        scanf(" %s",str);
        int len = strlen(str);
        ch=true;
        for(int i=0; i<len; i++)
        {
            if(!ch)
            {
                ans[i] = '9';
                continue;
            }
            if(ans[i-1]>str[i])
            {
                ans[i]='9';
                ans[i-1]-=1;
                ch = false;
                for(int j=i-1;j>=0;j--)
                {
                    if(ans[j+1]<ans[j])
                    {
                        ans[j+1] = '9';
                        ans[j] -= 1;
                    }
                }
            }
            else ans[i] = str[i];
        }
        ch=true;
        for(int j=0; j<len; j++)
        {
            if(ans[j]=='0'&&ch)continue;
            ch=false;
            printf("%c",ans[j]);
        }
        printf("\n");
}
int main()
{
    int q;
    scanf("%d",&q);
    for(int i = 1; i<=q; i++)
    {
        printf("Case #%d: ",i);
        sol();
    }
    return 0;
}
