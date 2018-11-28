#include<stdio.h>
#include<algorithm>
#include<vector>
#define maxx(x,y) ((x) > (y) ? (x) : (y))
#define minn(x,y) ((x) < (y) ? (x) : (y))
int now;
int n=0;
long long int dap=0;
using namespace std;
#include<string.h>
struct data
{
    long long int r,h,area;
}a[10000];
bool cmp(const data &w, const data &v)
{
    return w.area>v.area;
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
        int k,count=0;
        fscanf(in,"%d %d",&n,&k);
        for(i=1;i<=n;i++)
        {
            fscanf(in,"%lld %lld",&a[i].r,&a[i].h);
            a[i].area = a[i].r*a[i].h*2;
        }
        sort(a+1,a+n+1,cmp);
        long long int mm=0;
        for(i=1;i<=n;i++)
        {
            dap=(a[i].r*a[i].r)+a[i].area;;
            count=1;
            for(j=1;j<=k;j++)
            {
                if(count==k){break;}
                if(j==i){continue;}
                dap+=a[j].area;
                count++;
            }
            mm=maxx(mm,dap);
        }
        fprintf(out,"Case #%d: ",ll);
double pi = 3.14159265358979323846264338327950288419716939937510;
        pi = (double)(pi * (double)mm);
        fprintf(out,"%.13lf",pi);
        fprintf(out,"\n");
    }
}
