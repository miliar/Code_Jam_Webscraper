#include<stdio.h>
#define max(x,y) ((x) > (y) ? (x) : (y))
#define min(x,y) ((x) < (y) ? (x) : (y))
#include<string.h>
char a[10000];


int main()
{
    FILE *in = fopen("input.txt","r");
    FILE *out = fopen("output.txt","w");
    int T,ll=0,i;
    fscanf(in,"%d",&T);
    while(T--)
    {
        ll++;
        int n,k,tt;
        fscanf(in,"%d %d",&n,&k);
        tt=k;
        int l=0;
        while(tt)
        {
            a[l++] = tt%2;
            tt/=2;
        }
        int root=n,left,right;
        for(i=0;i<l;i++)
        {
            left=(root-1)/2;
            right=root/2;
            if(a[i])
            {
                root = left;
            }
            else
            {
                root = right;
            }
        }
        
        fprintf(out,"Case #%d: ",ll);
        fprintf(out,"%d %d",max(left,right),min(left,right));
        fprintf(out,"\n");
    }
}
