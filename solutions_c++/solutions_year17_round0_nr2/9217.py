#include <iostream>
#include <cmath>
using namespace std;

long calc(long N)
{
    long y = N;
    int e = log10(N);
        while(e>0)
        {
            long p = pow(10,e);
            if((y/p)%10 > ((y*10)/p)%10)
             {
                 y = (y/p - 1)*p + (p - 1);
                  e+=2;
             }
            --e;
        }
    return y;
}

int main()
{
   int t;
   long N,y;
   cin>>t;
   for(int i=1;i<=t;++i)
   {
        cin>>N;
        y = calc(N);
        cout<<"Case #"<<i<<": "<<y<<endl;
   }
   return 0;
}
