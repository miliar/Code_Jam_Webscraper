#include <stdio.h>
#include <stdlib.h>
#include <string.h>
FILE *out;
char X[1001];
int main()
{
    out=fopen("output.txt","w");
    int i,j,n,k,t;
    int x;
    int p;
    scanf("%d",&n);
    for(t=0;t<n;t++)
    {
        p=0;
        scanf("%s",X);
        scanf("%d",&k);
        x=strlen(X);
        int minus=0;
        for(i=0;i<x;i++)
        {
            if(X[i]=='-')
            {
                minus++;
            }
        }
        for(i=0;i<=x-k;i++)
        {
            while(X[i]=='+'&&i<=x-k)
            {
                i++;
            }
            if(i<=x-k)
            {
                p++;
                for(j=i;j<i+k;j++)
                {
                    if(X[j]=='-')
                    {
                        minus--;
                        X[j]='+';
                    }
                    else
                    {
                        minus++;
                        X[j]='-';
                    }
                }
            }
        }
        if(minus==0)
        {
            printf("Case #%d: %d\n",t+1,p);
            fprintf(out,"Case #%d: %d\n",t+1,p);
        }
        else
        {
            printf("Case #%d: IMPOSSIBLE\n",t+1);
            fprintf(out,"Case #%d: IMPOSSIBLE\n",t+1);
        }
    }

}
