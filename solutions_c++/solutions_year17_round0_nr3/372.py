#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <vector>
#include <list>
#include <string.h>
#include <map>
#include <set>

using namespace std;

typedef long long int LL;

int main()
{
    FILE* in, *out;
    string filename = "C-small-2-attempt0";
    string infilename = filename, outfilename = filename;
    infilename+=".in";
    outfilename+=".out";
    if((in=fopen(infilename.c_str(), "rt"))==NULL)
    {
        cout<<"Input file not found."<<endl;
        getchar();
        return 1;
    }
    if((out=fopen(outfilename.c_str(), "wt"))==NULL)
    {
        cout<<"Cannot create output file."<<endl;
        getchar();
        return 2;
    }

    int T;
    fscanf(in, "%d", &T);

    for(int t=0; t!=T; ++t)
    {
        LL n, k;
        fscanf(in, "%lld %lld", &n, &k);

        LL divs = 0, k0=k, n0=n;
        while(k0>1)
        {
            k0 = k0/2;
            ++divs;
        }
        for(int i=0; i<divs; ++i)
        {
            n0=(n0-1)/2;
        }
        LL base=n0;
        for(int i=0; i<divs; ++i)
        {
            n0=(n0*2)+1;
        }
        LL diff = n-n0;
        LL a=base;

        LL Kdivs = 0;
        k0=k;
        while(k0>1)
        {
            k0 = k0/2;
            ++Kdivs;
        }
        LL first = k & (1 <<(Kdivs));
        if(k - first < diff)
        {
            ++a;
        }

        fprintf(out, "Case #%d: %lld %lld\n", t+1, a/2, (a-1)/2);
    }

    fclose(in);
    fclose(out);
    return 0;
}

