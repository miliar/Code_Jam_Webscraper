#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>



int max (int a, int b)
{
if (a>b)
    {
    return a;
    }
return b;
}


int min (int a, int b)
{
if (a<b)
    {
    return a;
    }
return b;
}






int main ()
{
int i,j,t,r,p,l1,q, ac, aj;
int acm[2][2];
int ajm[2][2];
long long n,k,s, diff, mod, ans;
double l;
FILE *in = fopen("input.txt","r");    
FILE *out= fopen("output.txt","w");
fscanf(in, "%d", &t);
for (i=0;i<t;i++)
    {
    fscanf(in,"%d%d", &ac, &aj);
    for (j=0;j<ac;j++)
        {
        fscanf(in, "%d%d", &acm[j][0], &acm[j][1]);
        
        }
    for (j=0;j<aj;j++)
        {
        fscanf(in, "%d%d", &ajm[j][0], &ajm[j][1]);
        
        }

    if ((ac<=1)&&(aj<=1))
        {
        fprintf(out, "Case #%d: 2\n", i+1);
        continue;
        }
    if (ac==2)
        {
        if ((max(acm[1][1],acm[0][1])-min(acm[1][0],acm[0][0])<=12*60)|| ( min(acm[1][1],acm[0][1])+24*60-max(acm[1][0],acm[0][0])<=12*60 ))
            {
            fprintf(out, "Case #%d: 2\n", i+1);
            
            }
        else 
            {
            fprintf(out, "Case #%d: 4\n", i+1);
            
            }
        
        }
    if (aj==2)
        {
        if ((max(ajm[1][1],ajm[0][1])-min(ajm[1][0],ajm[0][0])<=12*60)|| ( min(ajm[1][1],ajm[0][1])+24*60-max(ajm[1][0],ajm[0][0])<=12*60 ))
            {
            fprintf(out, "Case #%d: 2\n", i+1);
            
            }
        else 
            {
            fprintf(out, "Case #%d: 4\n", i+1);
            
            }
        
        }


    
    
    
    }


    
    
}
