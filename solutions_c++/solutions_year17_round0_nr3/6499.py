#include <stdio.h>
#include <limits.h>
#include <set>
using namespace std;
bool b[1000002];
set<int> ans;
int min(int a,int b)
{
    if(a<b)return a;
    else return b;
}
int max(int a,int b)
{
    if(a>b)return a;
    else return b;
}
int main()
{
    freopen("output.txt","w",stdout);
    freopen("C-small-1-attempt0.in","r",stdin);
    int T,N,K,col,cor,temp,r,l,index,h;
    scanf("%d",&T);
    for(int t=1;t<=T;++t)
    {
        scanf("%d %d",&N,&K);
        b[0]=true;
        b[N+1]=true;
        for(int i=1;i<=N;++i)
        {
            b[i]=false;
        }
        for(int i=1;i<=K;++i)
        {
            h=-1;
            for(int j=1;j<=N;j++)
            {
                if(b[j])continue;
                col=0; cor=0;
                for(int k=j-1;k>=1;--k)
                {
                    if(!b[k])++col;
                    else break;
                }
                for(int k=j+1;k<=N;++k)
                {
                    if(!b[k])++cor;
                    else break;
                }
                temp=min(col,cor);
                if(temp>h)
                {
                    index =j;
                    l=col;
                    r=cor;
                    h=temp;
                }
                else if(temp==h)
                {
                    if(max(l,r)<max(col,cor))
                    {
                        index=j;
                        l=col;
                        r=cor;
                    }
                }

            }
            b[index]=true;
        }
        col=0; cor=0;
        for(int k=index-1;k>=1;--k)
        {
            if(!b[k])++col;
            else break;
        }
        for(int k=index+1;k<=N;++k)
        {
            if(!b[k])++cor;
            else break;
        }
        printf("Case #%d: %d %d\n",t,max(col,cor),min(col,cor));
    }
}
