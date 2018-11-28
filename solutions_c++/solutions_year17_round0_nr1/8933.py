#include<stdio.h>
#include<string.h>
int main()
{
    int t,k,i=0,j,m=0,flag=0,f=1;
    char a[1001];
    scanf("%d",&t);
    while(t)
    {
        k=0;j=0;i=0;
        scanf("%s",a);
        scanf("%d",&k);
        m=0;flag=0;
        while(i<(strlen(a)))
        {
           if(a[i]=='-')
           {
               if((k+i-1)<strlen(a))
               {
                    m++;
               for(j=i;j<k+i;j++)
                    {
                        if(a[j]=='-')
                            a[j]='+';
                        else
                            a[j]='-';
                    }

                }
                else
                {
                    flag=1;
                    break;
                }
            }
                i++;
        }
        if(flag==1)
     printf("Case #%d: IMPOSSIBLE\n",f++);
        else
        printf("Case #%d: %d\n",f++,m);
        t--;
    }
}
