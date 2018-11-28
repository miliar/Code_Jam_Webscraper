#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <cstdlib>
using namespace std;

fstream f("C-large.in", ios_base::in);
fstream g("output.txt", iostream::out);
int t;

unsigned long long n, k;

int main()
{
    f>>t;
    for(int i=1; i<t+1; ++i)
    {
        f>>n; f>>k;
        if(k==1)
        {
            if(n%2==0) g<<"Case #"<<i<<": "<<n/2<<" "<<n/2-1<<endl;
            else g<<"Case #"<<i<<": "<<n/2<<" "<<n/2<<endl;
        }
        else
        {
            --k;
            unsigned long long s=0, res;
            while(s<k) s=2*s+2;
            s+=2; s/=2;
            if((n-k)%s==0) res=(n-k)/s; else res=(n-k)/s+1;
            if(res%2==0) g<<"Case #"<<i<<": "<<res/2<<" "<<res/2-1<<endl;
            else g<<"Case #"<<i<<": "<<res/2<<" "<<res/2<<endl;
        }
    }

    return 0;
}
