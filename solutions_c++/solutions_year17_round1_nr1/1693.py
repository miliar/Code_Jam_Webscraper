#include<bits/stdc++.h>
using namespace std;
char s[50][50];
int main()
{
     freopen("i.in","r",stdin);
    freopen("o.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int x=1;x<=t;x++)
    {
        int R,C;
        scanf("%d %d",&R,&C);
        int i,j;
        for(i=0;i<R;i++)
        {
           scanf("%s",s[i]);
        }
        int idx=100;
        int jdx=100;
        for(i=0;i<R;i++)
        {
            for(j=0;j<C;j++)
            {
               if(s[i][j]!='?')
               {
                   jdx=j;
                   break;
               }
            }
            if(jdx==j)
                {   idx=i;
                    break;
                }
        }
        int g;
        for(i=idx;i>=0;i--)
        {
            int f=0;
            for(j=0;j<C;j++)
            {   g=0;
                if(s[i][j]!='?')
                {
                    f=1;
                    g=1;
                }
                if(g){
                for(int k=j-1;k>=0;k--)
                 {
                    if(s[i][k]=='?')
                        s[i][k]=s[i][j];
                    else
                        break;
                  }
                for(int k=j+1;k<C;k++)
                {
                    if(s[i][k]=='?')
                        s[i][k]=s[i][j];
                    else
                        break;
                 }
               }

            }
            if(!f && i+1<R)
            {
                for(j=0;j<C;j++)
                    s[i][j]=s[i+1][j];
            }
        }
         for(i=idx+1;i<R;i++)
         {
            int f=0;
            for(j=0;j<C;j++)
            {   g=0;
                if(s[i][j]!='?')
                {
                    f=1;
                    g=1;
                }
                if(g){
                for(int k=j-1;k>=0;k--)
                 {
                    if(s[i][k]=='?')
                        s[i][k]=s[i][j];
                    else
                        break;
                  }
                for(int k=j+1;k<C;k++)
                {
                    if(s[i][k]=='?')
                        s[i][k]=s[i][j];
                    else
                        break;
                 }
               }

            }
            if(!f && i-1>=0)
            {
                for(j=0;j<C;j++)
                    s[i][j]=s[i-1][j];
            }



    }
    printf("Case #%d:\n",x);
     for(i=0;i<R;i++)
      {
             printf("%s\n",s[i]);
      }
  }
  return 0;
}
