#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
    int t,r,c,m=1;
    scanf("%d",&t);
    while(m<=t)
    {
        scanf("%d%d",&r,&c);
        char a[r+1][c+2],k1=-1;
        for(int i=0;i<r;i++)
        {
            scanf("%s",a[i]);
        }
        int count=0;
        for(int i=0;i<r;i++)
        {
            int p=0;
            for(int j=0;j<c;j++)
            {
                if(a[i][j]!='?')
                {
                   for(int k=j;k>0;k--)
                   if(a[i][k-1]=='?')
                   a[i][k-1]=a[i][k];
                   for(int k=j;k<c-1;k++)
                   if(a[i][k+1]=='?')
                   a[i][k+1]=a[i][k];
                   k1=i;
                   if(count>0)
                   {
                       while(count--)
                       strcpy(a[i-count-1],a[i]);
                   }
                }
                else
                p++;
            }
            if(p==c)
            {
            count++;
            }
        }
        //int p=0;
        count=0;
       for(int i=r-1;i>=0;i--)
        {
            int p=0;
            for(int j=c-1;j>=0;j--)
            {
            if(a[i][j]=='?')
            p++;
            else
            {
                if(count>0)
                while(count--)
                strcpy(a[i+count+1],a[i]);
            }
            }
            if(p==c)
            count++;
        }
        printf("Case #%d:\n",m++);
        for(int i=0;i<r;i++)
        printf("%s\n",a[i]);
        }
    return 0;
}
