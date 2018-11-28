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
struct data
{
    double pos,v;
}a[10000]; 
struct data2
{
    double t,pos;
    int x,y;
}b[1000001]; 
bool cmp(const data2 &w, const data2 &v)
{
    if(w.t==v.t)
    {
        return w.pos<v.pos;
    }
    return w.t < v.t;
}
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
        int d;
        fscanf(in,"%d %d",&d,&n);
        for(i=1;i<=n;i++)
        {
            int x,y;
            fscanf(in,"%d %d",&x,&y);
            a[i].pos=double(x);
            a[i].v=double(y);
        }
        int l=0;
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            {
                if(i!=j&&a[i].pos>a[j].pos&&a[i].v<a[j].v)
                {
                    double aa=a[i].pos,bb=a[i].v,cc=a[j].pos,dd=a[j].v;
                    if(dd==bb){continue;}
                    double t1,pos1;
                    t1 = (aa-cc)/(dd-bb);
                    pos1 = aa+bb*t1;
                    if(pos1<=d){
                    b[++l].pos = pos1;
                    b[l].t = t1;
                    b[l].x = i;
                    b[l].y = j;
                    }
                }
            }
        }
        sort(b+1,b+l+1,cmp);
        double tttt=-1;
        for(i=1;i<=l;i++)
        {
            if(check[b[i].x]==0&&check[b[i].y]==0)
            {
                check[b[i].y] = 1;
            }
        }

        for(i=1;i<=n;i++)
        {
            if(check[i]==0)
            {
                tttt = maxx(tttt,(d-a[i].pos)/a[i].v);
            }
            check[i]=0;
        }
        
        fprintf(out,"Case #%d: ",ll);
        fprintf(out,"%.10lf",double(d)/tttt);
        fprintf(out,"\n");
    }
}  
