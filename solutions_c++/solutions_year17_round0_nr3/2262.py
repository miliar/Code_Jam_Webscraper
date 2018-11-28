#include <iostream>
#include <fstream>
using namespace std;
long long p[65],S[65],n,k,a,b,t;
int i,it;
int bs(long long val)
{
    int ls=0,ld=60,m=30;
    while(ls<=ld)
    {
        if(S[m]<val && S[m+1]>=val)return m+1;
        if(S[m+1]<val)
        {
            ls=m+1;
            m=(ls+ld)/2;
        }
        else
        {
            ld=m-1;
            m=(ls+ld)/2;
        }
    }
    return 0;
}
int main()
{
    S[0]=1;p[0]=1;
    for(i=1;i<62;++i)
    {
        p[i]=2*p[i-1];
        S[i]=S[i-1]+p[i];
    }
    ifstream f("text.in");
    ofstream g("text.out");
    f>>t;
    for(it=1;it<=t;++it)
    {
        f>>n>>k;
        i=bs(k)+1;
        a=(n-k)/p[i];
        b=(n-k)/p[i-1]-a;
        g<<"Case #"<<it<<": "<<max(a,b)<<" "<<min(a,b)<<'\n';
    }
    return 0;
}
