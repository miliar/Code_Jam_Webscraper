#include<stdio.h>
#define max(x,y) ((x) > (y) ? (x) : (y))
#define min(x,y) ((x) < (y) ? (x) : (y))
char map[110][110];
char map2[110][110];
int maxx=0;
int n,m;
int ga[1000];
int ga2[1000];
int se[1000];
int se2[1000];
int d11[1000];
int d12[3000];
int d21[3000];
int d22[3000];
int check[110][110];
char dap[110][110];
struct data
{
    int xx,yy;
    char tt;
}queue[10000];
int main()
{
    int i,j,k;
    FILE *in = fopen("input.txt","r");
    FILE *out = fopen("output.txt","w");
    int T,ll=0;
    fscanf(in,"%d",&T);
    while(T--)
    {
        ll++;
        maxx=0;
        int x,y,p=0,orgp=0;
        char t;
        fscanf(in,"%d %d",&n,&m);
        for(i=0;i<m;i++)
        {
            fscanf(in," %c %d %d",&t,&x,&y);
            map[x][y] = t;
            check[x][y] = 1;
            if(t=='o'){orgp+=2;}
            else{orgp+=1;}
            if(t!='+')
            {
                ga[x]++;
                se[y]++;
            }
            if(t!='x')
            {
                d11[x+y-1]++;
                d21[x-y+n]++;
            }
        }
        int tail=m;
        for(i=1;i<=n;i++)
        {
            p=orgp;
            tail=m;
            for(j=1;j<=n;j++){for(k=1;k<=n;k++){map2[j][k] = map[j][k];}}
            for(j=1;j<=n;j++){ga2[j] = ga[j]; se2[j] = se[j];}
            for(j=1;j<=2*n-1;j++){d12[j] = d11[j]; d22[j]= d21[j];}
            for(j=1;j<=n;j++)
            {
                if(d12[i+j-1]==0&&d22[i-j+n]==0&&map2[i][j]==0)
                {
                    map2[i][j] = '+';
                    d12[i+j-1]++;
                    d22[i-j+n]++;
                    p++;
                }
            }
            for(j=1;j<=n;j++)
            {
                for(k=1;k<=n;k++)
                    {
                        if(se2[k]==0&&ga2[j]==0&&map2[j][k]==0)
                        {
                            map2[j][k]='x';
                            ga2[j]++;
                            se2[k]++;
                            p++;
                        }
                    } 
            }
            int start=n,size=0;
            for(j=1;j<=n;j++)
            {
                for(k=1;k<=n;k++)
                {
                    if(d12[j+k-1]==0&&d22[j-k+n]==0&&map2[j][k]==0)
                    {
                       map2[j][k]='+';
                       d12[j+k-1]++;
                       d22[j-k+n]++;
                       p++;
                    }
                }
            }
            for(j=1;j<=n;j++)
            {
                for(k=1;k<=n;k++)
                {
                    if(map2[j][k]=='x')
                    {
                        if(d12[j+k-1]==0&&d22[j-k+n]==0)
                        {
                            map2[j][k]='o';
                            d12[j+k-1]++;
                            d22[j-k+n]++;
                            p++;
                        }
                    }
                    if(map2[j][k]=='+')
                    {
                        if(ga2[j]==0&&se2[k]==0)
                        {
                            map2[j][k]='o';
                            ga2[j]++;
                            se2[j]++;
                            p++;
                        }
                    }
                }
            }
            if(maxx<p)
            {
                maxx=p;
                for(j=1;j<=n;j++)
                {
                    for(k=1;k<=n;k++)
                    {
                        dap[j][k] = map2[j][k];
                    }
                }
            }
        }
        fprintf(out,"Case #%d: ",ll);
        int diff=0;
        for(i=1;i<=n;i++){for(j=1;j<=n;j++){if(map[i][j]!=dap[i][j]){diff++;}}}
        for(i=1;i<=n;i++){ga[i]=0;se[i]=0;}
        for(i=1;i<=2*n-1;i++){d11[i]=0;d21[i]=0;}
        fprintf(out,"%d %d\n",maxx,diff);
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            {
                if(dap[i][j]!=map[i][j])
                {
                    fprintf(out,"%c %d %d\n",dap[i][j],i,j);

                }
                map[i][j]=0;
                dap[i][j]=0;
            }
        }
        //fprintf(out,"\n");
    }

}
