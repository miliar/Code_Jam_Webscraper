#include <stdio.h>
#include <stdlib.h>


int main ()
{
int i,j,t,s,k,r,p;
int a[1000];
char c;
FILE *in = fopen("input.txt","r");    
FILE *out= fopen("output.txt","w");
fscanf(in, "%d", &t);
for (i=0;i<t;i++)
    {
    s=0;
    r=0;
    while (1==1)
        {
        fscanf(in,"%c",&c);
        if (c=='+') 
            {
            a[s]=1;
            s++;
            }
        if (c=='-') 
            {
            a[s]=0;
            s++;
            }
        if (c==' ')
            {
            fscanf(in,"%d",&k);
            break;
            }
        }
    for (j=0;j<s;j++)
        {
        if (a[j]==1) {continue;}
        if (j+k>s) {r=-1;break;}
        r++;
        for (p=0;p<k;p++)
            {
            a[j+p]=1-a[j+p];
            }       
        
        }
    fprintf(out,"Case #%d: ",i+1);
    if (r==-1)
        {
        fprintf(out, "IMPOSSIBLE\n");
        continue;
        }
    fprintf(out,"%d\n",r);
    
    
    }  
    
    
}
