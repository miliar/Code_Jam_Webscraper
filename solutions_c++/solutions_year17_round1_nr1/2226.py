#include<stdio.h>
#include<algorithm>
#include<vector>
#define maxx(x,y) ((x) > (y) ? (x) : (y))
#define minn(x,y) ((x) < (y) ? (x) : (y))

int now;
int n=0;
int dap=0;
using namespace std;
#include<string.h>
char map[100][100]; 
char init[100];
char init_u[100];
int init_l,lll=0;
int check[10000];
int main()
{
    FILE *in = fopen("input.txt","r");
    FILE *out = fopen("output.txt","w");
    int T,ll=0,i,j;
    fscanf(in,"%d",&T);
    while(T--)
    {
        ll++;
        dap=0;
        int m;
        fscanf(in,"%d %d",&n,&m);
        init_l=0;
        for(i=0;i<1000;i++){check[i]=0;}
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                fscanf(in," %c",&map[i][j]);
                }
        }
       int k,l=0;
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                char before=0;
                int mmm[1000],xx,yy;
                if(check[map[i][j]]==1){continue;}
                for(k=i;k<=n;k++)
                {
                    for(l=j;l<=m;l++)
                    {
                        if(map[k][l]!='?')
                        {
                            if(before!=0||check[map[k][l]]==1){mmm[k] = l-1;break;}
                            before=map[k][l];xx=k,yy=l;
                        }
                    }
                    if(l==m+1){mmm[k]=l-1;}
                }
                int max2=0,max2i,ming=9999,mink,bm=0;
                for(k=i;k<=n;k++)
                {
                    ming=minn(ming,mmm[k]);
                    if((max2<(ming-j+1)*(k-i+1)&&xx<=k&&yy<=ming))
                    {
                        if(bm==0||bm==ming){
                        max2=(ming-j+1)*(k-i+1);
                        mink=ming;
                        max2i=k;
                        bm=mink;
                        }
                    }
                }
                for(k=i;k<=max2i;k++)
                {
                    for(l=j;l<=mink;l++)
                    {
                        map[k][l] = before;
                    }
                }
                check[before]=1;
            }
        }
        
        fprintf(out,"Case #%d:\n",ll);
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                fprintf(out,"%c",map[i][j]);
            }
            fprintf(out,"\n");
        }
    }
}
