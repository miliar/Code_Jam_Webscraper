#include <cstdio>
#include <iomanip>
#include <iostream>
#include <map>
using namespace std;
int T,N;
int K;
long double U;
map<long double,int> M;
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cout<<"Case #"<<t<<": ";
        cin>>N>>K>>U;M.clear();
        for(int i=1;i<=N;i++)
        {
            long double P;
            cin>>P;
            M[P]++;
        }
        M[1]++;
        while(U>0.0000001)
        {
            long double p=M.begin()->first,npr;
            int nr=M.begin()->second;
            M.erase(M.begin());
            if((M.begin()->first-p)*nr-U>0.0000001)
            {
                npr=p+U/nr;
                U=0;
            }
            else
            {
                npr=M.begin()->first;
                U-=(M.begin()->first-p)*nr;
            }
            M[npr]+=nr;
        }
        long double rez=1;
        for(auto it:M)
        {
            while(it.second)
            {
                rez*=it.first;
                it.second--;
            }
        }
        cout<<setprecision(10)<<fixed<<rez;
        cout<<"\n";
    }
    return 0;
}
