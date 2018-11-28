#include <iostream>
#include <map>
#include <fstream>
#define ull  long long
#define P10A18 (ull) 1000000000000000000
using namespace std;
//unsigned ull Complejidad=0;
pair<ull,ull> Caso(ull n, ull k)
{
    k--;
    int nmax,nmin;
    nmax=(n)/2;
    nmin=(n-1)/2;
//    cout<<n<<" para "<<k<<"==="<<nmax<<" , "<<nmin<<"  "<<(P10A18)<<endl;

    if(k>=1)
    {
        if(k%2==0)
            return Caso(nmin,k/2);
        else
        {
            ull kmax=k/2+1, kmin=k/2;
            return min(Caso(nmin,kmin),Caso(nmax,kmax));
        }
    }
    if(k==0)
        return {nmax,nmin};
    return {P10A18,P10A18};
}
int main()
{
    int T;
    ifstream FE("entrada.in");
    FE>>T;
    ofstream FS("salida.out");
    int N,K;
    for(int i=0;i<T;i++)
    {
        FE>>N>>K;
        pair<int,int> P =Caso(N,K);
        FS<<"Case #"<<i+1<<": "<<P.first<<" "<<P.second<<endl;
    }
    FE.close();
    FS.close();
}
