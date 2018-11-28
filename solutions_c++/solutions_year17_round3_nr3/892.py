#include<stdio.h>
#include<algorithm>
#include<vector>
#include<math.h>
#define maxx(x,y) ((x) > (y) ? (x) : (y))
#define minn(x,y) ((x) < (y) ? (x) : (y))
#define abs(x) ((x) > (0) ? (x) : (-1*x))
#define ROUNDING(x, dig)    ( floor((x) * pow(float(10), dig) + 0.5f) / pow(float(10), dig) )
int now;
int n=0;
int dap=0;
using namespace std;
#include<string.h>
double a[10000]; 
int check[10000];
bool cc(double aa, double bb)
{
    double cccc = aa-bb;
    if(cccc<0){cccc=-cccc;}
   if(aa>bb){return true;}
   if(cccc<0.0000001){return true;}
   else{return false;}

}
int main()
{
    int larget=10000000;
    FILE *in = fopen("input.txt","r");
    FILE *out = fopen("output.txt","w");
    int T,ll=0,i,j;
    fscanf(in,"%d",&T);
    while(T--)
    {
        ll++;
        dap=0;
        int k;
        fscanf(in,"%d %d",&n,&k);
        double p;
        fscanf(in,"%lf",&p);
        for(i=1;i<=n;i++)
        {
            fscanf(in,"%lf",&a[i]);
            a[i] = ROUNDING(a[i],7);
        }
        sort(a+1,a+n+1);
        int target=2;
        now=1;
        a[n+1] = 1;
        while(1)
        {
            double na=0;
            if(cc(p,((double)(now)*(a[target]-a[now]))))            {
                p-=(a[target]-a[now])*(double)(now);
                for(i=1;i<=now;i++)
                {
                    a[i] = a[target];
                }
            }
            else
            {
                for(i=1;i<=now;i++)
                {
                    a[i]+=p/double(now);
                }
                break;
            }

            if(now==n){break;}
            now++;
            target++;
         }
         double dd=1;

          for(i=1;i<=n;i++)
          {
              dd*=a[i];
            

          }
        fprintf(out,"Case #%d: ",ll);
        fprintf(out,"%lf",dd);
        fprintf(out,"\n");
    }
}
