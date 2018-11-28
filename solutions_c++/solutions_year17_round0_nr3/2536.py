#include <iostream>
#include <queue>
#include <fstream>
#include <map>
using namespace std;

int main()
{
    ifstream cin2("C-large.in");
    ofstream cout2("salida2.out");
    long long n;
    cin2>>n;
    long long x,p,aux,aux2,a,b;
    for(int u=1;u<=n;u++){
        cin2>>x>>p;
        map<long long,long long> mapa;
        priority_queue <long long>q;
        q.push(x);
        mapa[x]=1;
        long long con=0;
        for(;;){
            aux=q.top();
            con+=mapa[aux];
            q.pop();
            aux2=aux/2;
            if(mapa[aux2]==0)q.push(aux2);
            mapa[aux2]+=mapa[aux];
            a=aux2;
            if(aux%2==0)aux2--;
            if(mapa[aux2]==0)
                q.push(aux2);
            mapa[aux2]+=mapa[aux];
            b=aux2;
            if(con>=p)break;
        }
        cout2<<"Case #"<<u<<": "<<max(a,b)<<" "<<min(a,b)<<"\n";
    }
    return 0;
}
