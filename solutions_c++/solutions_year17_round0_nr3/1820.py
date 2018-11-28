#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int t,tdb;
    long long N,K;
    cin>>tdb;
    for (t=0; t!=tdb; t++)
    {
        cin>>N>>K;
        while (K>1)
        {
            if (N%2==0)
            {
                if (K%2==0)
                {
                    K/=2;
                    N=N/2;
                }
                else
                {
                    K/=2;
                    N=(N-1)/2;
                }
            }
            else
            {
                N/=2;
                K/=2;
            }
        }
        cout<<"Case #"<<t+1<<": "<<N/2<<" "<<(N-1)/2<<endl;
    }
    return 0;
}
