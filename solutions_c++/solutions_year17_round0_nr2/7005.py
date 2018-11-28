#include <bits/stdc++.h>

using namespace std;
int T;
ifstream f("in.in");
ofstream g("in.out");
int ok=1;


void tidy(int digits,long long lim, long long number = 0)
{
    if(ok)
        {int i = (number % 10) ;
    number *= 10;
    for (int j=9;j>=i;j--)
    {
        if (digits == 1)
            {if(number+j<=lim)
             {g<<number + j;ok=0;return;}
            }
        else
            tidy(digits - 1, lim,number + j);
    }}
}


int nrcifre(long long x)
{
    int nr=0;
    while(x) x/=10,nr++;
    return nr;
}
int main()
{
    f>>T;
    for(int i=1;i<=T;i++)
    {
        long long x;
        f>>x;
        int q=nrcifre(x);
        ok=1;
       g<<"Case #"<<i<<": ";tidy(q,x,0);g<<'\n';
    }

}
