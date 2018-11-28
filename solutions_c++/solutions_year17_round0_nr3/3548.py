#include <iostream>
using namespace std;
typedef long long LL;
LL calc1(LL n,LL k)
{
    if(k==1) return n>>1;
    if(n&1) return calc1(n>>1,k>>1);
    if(k&1) return calc1((n>>1)-1,k>>1);
    return calc1(n>>1,k>>1);
}
LL calc2(LL n,LL k)
{
    if(k==1) return (n-1)>>1;
    if(n&1) return calc2(n>>1,k>>1);
    if(k&1) return calc2((n>>1)-1,k>>1);
    return calc2(n>>1,k>>1);
}
int main()
{
    int T;
    LL n,k;
    cin>>T;
    for(int t=1;t<=T;++t)
    {
        cin>>n>>k;
        cout<<"Case #"<<t<<": "<<calc1(n,k)<<' '<<calc2(n,k)<<endl;
    }
    return 0;
}
