#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    long long int test=1;
    while(t--)
    {
        long long  int d,k;
       long  double a,s;
        cin>>d>>k;
        long double t;
        long  double max_t=0;
        long double sp;

        for(int i=0;i<k;i++)
        {
            cin>>a>>s;
            t=(d-a)/s;
            if(t>max_t)
                max_t=t;

        }
        sp=d/max_t;
       cout<<"Case #"<<test<<": "<<fixed<<setprecision(6)<<sp<<endl;
        test++;

    }
}
