#include <cstdio>
#include <string.h>

int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1; t<=T; t++)
    {
        char s[1000];
        scanf("%s",s);
        int n = strlen(s);
        int k;
        scanf("%d",&k);

        int count = 0;
        for(int i=0; i<=n-k; i++)
        {
            if(s[i] == '+') continue;
            else
            {
                count++;
                for(int j=i; j<i+k; j++)
                {
                    //printf("%d %c",j,s[j]);
                    if(s[j] == '+') s[j]='-';
                    else s[j]='+';
                }
                //printf("\n");
            }    
        }

        int flag = 0;
        for(int i=0; i<n; i++)
        {
            //printf("%c",s[i]);
            if(s[i] == '-') 
            {
                flag = 1;
                break;
            }
        }
        //printf("\n");

        printf("Case #%d: ",t);
        if(flag == 1) printf("IMPOSSIBLE\n");
        else printf("%d\n",count);

    }
}