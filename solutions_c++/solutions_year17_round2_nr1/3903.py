#include <iostream>
#include <iomanip>
using namespace std;
typedef long long int lli;
const int MAXN=1003;
int main()
{
    freopen("/Users/nsbhasin/Desktop/Kickstart2017/CruiseControl/A-large.in","r",stdin);
    freopen("/Users/nsbhasin/Desktop/Kickstart2017/CruiseControl/output1.txt","w",stdout);
    lli t,test=1;
    lli N,D;
    double ans;
    lli K[MAXN],S[MAXN];
    double T,max_time=-1;
    cin>>t;
    while(t--)
    {
        max_time=-1;
        cin>>D>>N;
        for(int i=0;i<N;i++)
        {
            cin>>K[i]>>S[i];
            T=D-K[i];
            T=T/S[i];
            if(T>max_time)
                max_time=T;
        }
        ans=D/max_time;
        cout<<"Case #"<<test++<<": "<<fixed<<setprecision(6)<<ans<<endl;
    }
    return 0;
}
