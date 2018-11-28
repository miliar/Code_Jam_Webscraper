#include<stdio.h>
#include<conio.h>
#include<string.h>
void flip(char [],int ,int );
int main()

{

freopen("A-large.in","r",stdin);
freopen("Pancake_output.out","w",stdout);
    char a[1000];
    int t,k,j=0,count=0,n=1,i,f=0;

    scanf("%d",&t);

      for(i=1;i<=t;i++)
    {
        scanf("%s",a);
        scanf("%d",&k);
        n=strlen(a);
        while(j<n)
        {
            if(a[j]=='-')
            {

                if(j<=n-k)
                {
                flip(a,j,k);
                count++;
                }

            }
           j++;

        }


        for(j=0;j<n;j++)
        {
            if(a[j]=='-')
            {
                f=1;
                break;
            }
        }
        if(f==1)
        {
          printf("Case #%d: IMPOSSIBLE\n",i);
        }
        else
        {
           printf("Case #%d: %d\n",i,count);
        }

        f=0;
        j=0;
        count=0;


    }
    return 0;



}
void flip(char a[],int i,int k)
{
    int j;


        for(j=i;j<i+k;j++)
        {
            if(a[j]=='-')
            {
                a[j]='+';
            }
            else
            {
                a[j]='-';

            }

        }

}
