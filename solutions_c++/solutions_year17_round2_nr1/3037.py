#include<bits/stdc++.h>
#define lli long long int
using namespace std;
int main()
{
    lli T;
    cin>>T;
    lli i=1;
    while(i<=T)
    {
        lli D,N;
        cin>>D>>N;
        lli k,s;
        lli j=0;double max=-1.0,t=0.0;
        while(j<N)
        {
            cin>>k>>s;
            t=double(D-k)/s;
            //  cout<<t<<endl;
            if((t)>max)
            {
                max=t;

            }
            j++;
        }
        cout<<"Case #"<<i<<": "<<fixed<<setprecision(6)<<double(D/max)<<endl;
        i++;
    }
}
