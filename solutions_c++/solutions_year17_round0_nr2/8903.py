#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream cin("input.in");
    ofstream cout("output.txt");
    int t;
    cin >>t;
    for (int iii=1; iii<=t; iii++)
    {

    long long n;
    cin >>n;
    long long ans=0;
    for (long long i=n; i>=1; i--)
    {
        if (i<10)
        {
            ans=i;
            break;
        }
        long long nn=i;
        int zz=nn%10;
        nn/=10;
        bool ok=true;
        while (nn>0)
        {
            int z=nn%10;
            if (z>zz)
            {
                ok=false;
                break;
            }
            zz=z;
            nn/=10;
        }
        if (ok)
        {
            ans=i;
            break;
        }
    }
    cout <<"Case #"<<iii<<": "<<ans<<"\n";

    }
    return 0;
}
