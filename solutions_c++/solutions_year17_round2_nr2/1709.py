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
int a[10000];
int b[10000];
int co[10000];
char con[7]={'0','R','O','Y','G','B','V'};
int path[100000];
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
        fscanf(in,"%d",&n);
        for(i=1;i<=6;i++)
        {
            a[i] =0;
            b[i] = 0;
            fscanf(in,"%d",&a[i]);
        }

        fprintf(out,"Case #%d: ",ll);
        int mm=-1,tot=0,os=0,st,ed;
        for(i=1;i<=6;i++){b[i] =a[i];}
        for(i=1;i<=6;i++){mm=maxx(mm,b[i]);tot+=b[i];}  
        if(tot-mm<mm){fprintf(out,"IMPOSSIBLE\n");continue;}
        mm=-1;
        for(i=1;i<=6;i++)
        {
            if(b[i]>0&&mm<=b[i]){mm = b[i];st=i;}
        }
        os = st;
        a[st]--;
        for(i=1;i<n;i++)
        {
            path[i] = st;
            mm=-1;
            for(j=1;j<=6;j++)
              {
                        if(st!=j&&a[j]>0&&mm<=a[j])
                        {
                            if((mm==a[j]&&j==os)||mm<a[j])
                            {

                            mm = a[j];
                            ed = j;
                            }
                        }
               
              }
                
                    if(mm==-1){break;}
            
            a[ed]--;
            st = ed;
        }
        path[i] = st;
        if(path[1]==path[n]){printf("%d asdfasdfasdf",ll);}

        if(i==n)
        {
            for(i=1;i<=n;i++)
            {
                if(check[path[i]]==0)
                {
                    check[path[i]]=1;
                    for(j=1;j<=a[co[path[i]]];j++)
                    {
                        fprintf(out,"%c%c",con[path[i]],con[co[path[i]]]);
                    }
                }
                fprintf(out,"%c",con[path[i]]);
            }
        }
        else
        {
            fprintf(out,"IMPOSSIBLE");
        }

        for(i=1;i<=6;i++){check[i]=0;}
        fprintf(out,"\n");
    }
}
