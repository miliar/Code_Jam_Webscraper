#include <bits/stdc++.h>
using namespace std;
int t,i,l,j,k,a[25];
long long n;
FILE *in,*out;
int main()
{
    in=fopen("B-large.in","r");
    out=fopen("output.out","w");
    for(fscanf(in,"%d",&t);i<t;i++)
    {
        fscanf(in,"%lld",&n);
        for(l=0;n;l++)
        {
            a[l]=n%10;
            n/=10;
        }
        a[l]=0;
        for(j=k=l;j>0;j--)
        {
            if(a[j]!=a[j+1])
                k=j;
            if(a[j]>a[j-1])
            {
                j=k;
                a[j]--;
                for(j--;j>=0;j--)
                    a[j]=9;
            }
        }
        fprintf(out,"Case #%d: ",i+1);
        for(j=l;a[j]==0;j--);
        for(;j>=0;j--)
            fprintf(out,"%d",a[j]);
        fprintf(out,"\n");
    }
}
