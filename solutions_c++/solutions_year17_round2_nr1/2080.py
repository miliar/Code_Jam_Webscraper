#include <iostream>
#include <map>
#include <limits>
#include <stack>
#include <algorithm>
#include <vector>
#include <fstream>
#include <cstdio>

#define rep(i,x,n) for(int i = x; i < n; ++i)
#define rrep(i,n,x) for(int i = n; i >= x; --i)
#define mod 1000000007

using namespace std;

void print_f(float x)
{
    int n = x;
    x = x - n;
    x = x*1000000;
    printf("%d.%06d",n,(int)x);
}

int main()
{
    int t, k = 0;
    ifstream in;
    in.open("A.in");
    FILE* out;
    out = fopen("Aout.out", "a");
    in >> t;
    while(t--)
    {
        int n,d;
        in >> d >> n;
        int *a = new int[n];
        int *b = new int[n];
        rep(i,0,n)
        {
            in >> a[i] >> b[i];
        }
        double time = 0.0;
        rep(i,0,n)
        {
            a[i] = d - a[i];
            double val = (double)a[i] / (double)b[i];
            if(val > time)
                time = val;
        }
        double speed = (double)d/time;
        fprintf(out, "Case #%d: %0.6f\n", ++k, speed);
    }
    return 0;
}
