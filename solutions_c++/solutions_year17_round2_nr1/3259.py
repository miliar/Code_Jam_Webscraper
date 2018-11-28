#include <stdio.h>

int main()
{
    int t,n,k,s,d;
    double mx=-1;
    FILE *out, *in;
    in=fopen("A-large.in", "r");
    out=fopen("output.txt", "wt");
    fscanf(in, "%d", &t);
    for(int i=1; i<=t; ++i)
    {
        fscanf(in,"%d %d",&d,&n);
        mx=-1;
        for(int j=1; j<=n; ++j)
        {
            fscanf(in,"%d %d", &k, &s);
            if(mx<double((d-k))/s)
                mx=double((d-k))/s;
        }
        fprintf(out,"Case #%d: %f\n", i, double(d)/mx);
    }
}
