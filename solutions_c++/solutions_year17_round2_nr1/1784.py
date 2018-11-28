#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int main ()
{
int n, i,j,t,r,p,l1, d;
long long k,s, diff, mod, ans;
double l,ti;
int hp[1000];
int hs[1000];
FILE *in = fopen("input.txt","r");    
FILE *out= fopen("output.txt","w");
fscanf(in, "%d", &t);

for (i=0;i<t; i++)
    {
    fscanf(in, "%d%d", &d, &n);
    l=0;
    for (j=0;j<n;j++)
        {
        fscanf(in,"%d%d", &hp[j], &hs[j] );
        ti=(1.0*(d-hp[j]))/hs[j];
        if (l<ti)
            {
            l=ti;
            }
        
                
        }
    ti=d/l;
    fprintf(out, "Case #%d: %lf\n", i+1, ti);


    }

    
    
}
