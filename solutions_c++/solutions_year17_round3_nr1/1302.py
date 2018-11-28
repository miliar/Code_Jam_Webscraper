#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

long long max(long long a, long long b)
{
if (a>b)
    {
    return a;
    }
return b;
}


struct pancake
{
long long r;
long long h;
long long hc;
};

pancake pnc[1000];



void quickSort(int l, int r)
{
    long long x = pnc[l + (r - l) / 2].hc;
    pancake tmp;
    int i = l;
    int j = r;
    while(i <= j)
    {
        while(pnc[i].hc < x) i++;
        while(pnc[j].hc > x) j--;
        if(i <= j)
        {
            tmp=pnc[i];
            pnc[i]=pnc[j];
            pnc[j]=tmp;
            i++;
            j--;
        }
    }
    if (i<r)
                quickSort(i, r);
   
    if (l<j)   
        quickSort(l, j);    
}





int main ()
{
long long i,j,t,p,l1,q;
long long n,k,s, diff, mod, ans;

long long sum, maxs, maxr, maxri, cnd, dist, maxrn;


double l;
FILE *in = fopen("input.txt","r");    
FILE *out= fopen("output.txt","w");
fscanf(in, "%lld", &t);
for (i=0;i<t;i++)
    {
    fscanf(in,"%lld%lld",&n,&k);
    for (j=0;j<n;j++)
        {
        fscanf(in, "%lld%lld", &pnc[j].r, &pnc[j].h);
        pnc[j].hc=2*pnc[j].r*pnc[j].h;
        
        }
    quickSort(0, n-1);
    maxr=0;
    maxri=-1; 
    sum=0;
    for (j=n-1;j>=n-k+1;j--)
        {
        sum=sum+pnc[j].hc;
        if (j==n-1)
            {
            maxr=pnc[j].r;
            maxri=j;
            }
        if (pnc[j].r>maxr )
            {
            maxr=pnc[j].r;
            maxri=j;
            }    
        }
    for (j=0;j<n;j++)
        {
        //fprintf(out,"%lld\n", pnc[j].hc);
        
        }
    //fprintf(out, "%lld\n", sum);
    maxs=0;
    cnd=-1;
    for (j=0;j<n-k+1;j++)
        {
        dist=max(pnc[j].r*pnc[j].r-maxr*maxr, 0)+pnc[j].hc;
        if (dist>maxs)
            {
            maxs=dist;
            cnd=j;
            maxrn=max(maxr, pnc[j].r);
            }
        
        }
     
        
    sum=sum+pnc[cnd].hc;
    sum=sum+maxrn*maxrn;

    l=sum*M_PI;
    fprintf(out, "Case #%lld: %lf\n", i+1, l);
    }


    
    
}
