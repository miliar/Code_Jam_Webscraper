#include<cstdio>
#include<cstring>
char str[1010];
int tod[1010];
int main()
{
    int q;
    scanf("%d",&q);
    for(int i = 1; i<=q; i++)
    {
        scanf(" %s",str);
        printf("Case #%d: ",i);
        int len = strlen(str);
        for(int j=0; j<len; j++)
        {
            while(1)
            {
                bool ch=true,ch2=false;
                for(int k=j+1; k<len; k++)
                {
                    if(ch2)
                    {
                        if(str[j]>str[k])
                        {
                            ch=false;
                            break;
                        }
                    }
                    else if(str[j]<str[k])
                    {
                        break;
                    }
                    else if(str[j]==str[k])ch2=true;
                    else if(str[j]>str[k])
                    {
                        ch=false;
                        break;
                    }
                }
                if(ch)break;
                if(str[j]=='1'&&j==0)
                {
                    str[j]='0';
                    for(int k=j+1; k<len; k++)str[k]='9';
                    goto BREAK;
                }
                str[j]-='0';
                str[j]--;
                str[j]+='0';
                for(int k=j+1;k<len;k++)str[k]='9';
            }

        }
        BREAK:
        bool ch=true;
        for(int j=0; j<len; j++)
        {
            if(str[j]=='0'&&ch)continue;
            ch=false;
            printf("%c",str[j]);
        }
        printf("\n");
    }
    return 0;
}
