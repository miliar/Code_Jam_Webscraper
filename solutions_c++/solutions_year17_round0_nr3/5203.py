#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int main ()
{
int i,j,t,r,p,l1;
long long n,k,s, diff, mod, ans;
double l;
FILE *in = fopen("input.txt","r");    
FILE *out= fopen("output.txt","w");
fscanf(in, "%d", &t);
for (i=0;i<t;i++)
    {
    fscanf(in,"%lld%lld", &n, &k);
    l1=floor(log(k)/log(2));
    s=pow(2,l1);
    diff=(n-s)/s;
    mod=n%s;
//    fprintf(out,"%lld %lld %d %lld %lld %lld\n",n,k,l1,s,diff,mod);
    if (k<=s+mod)
        {
        ans=diff+1;
        }
        else
        {
        ans=diff;
        }
    if (ans%2==1)
        {
        fprintf(out,"Case #%d: %lld %lld\n", i+1, ans/2, ans/2);
        }
        else
        {
        fprintf(out,"Case #%d: %lld %lld\n", i+1, ans/2, ans/2-1);
        }
    }  



    
    
}
