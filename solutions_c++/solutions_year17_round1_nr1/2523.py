#include<bits/stdc++.h>
using namespace std;
char a[30][30];
int b[30];
int main()
{
    //freopen("i.in","r",stdin);
	//freopen("o.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        int r,c;
        scanf("%d %d",&r,&c);
        for(int j=0;j<r;j++)
        {
            scanf("%s",a[j]);
        }
        for(int j=0;j<r;j++)
        {
            char p='0';
            for(int k=0;k<c;k++)
            {
                if(a[j][k]=='?')
                {
                    if(p!='0')
                    {a[j][k]=p;b[p-'A']=1;}
                }
                else
                {
                    p=a[j][k];
                }
            }
        }
        for(int j=0;j<r;j++)
        {
            char p='0';
            for(int k=c-1;k>=0;k--)
            {
                if(a[j][k]=='?')
                {
                    if(p!='0')
                    {a[j][k]=p;b[p-'A']=1;}
                }
                else
                {
                    p=a[j][k];
                }
            }
        }
        for(int j=0;j<c;j++)
        {
            char p='0';
            for(int k=0;k<r;k++)
            {
               // printf("%c %d %d\n",p,k,j);
                if(a[k][j]=='?')
                {
                    if(p!='0')
                    {a[k][j]=p;b[p-'A']=-1;}
                }
                else
                {
                    p=a[k][j];
                }
               // printf("%c\n",p);
            }
        }
         for(int j=0;j<c;j++)
        {
            char p='0';
            for(int k=r-1;k>=0;k--)
            {
                if(a[k][j]=='?')
                {
                    if(p!='0')
                    {a[k][j]=p;}
                }
                else
                {
                    p=a[k][j];
                }
            }
        }

        printf("Case #%d:\n",i);
        for(int j=0;j<r;j++)
        {
            printf("%s\n",a[j]);
        }
        for(int i=0;i<30;i++)
            b[i]=0;
    }
    return 0;
}
