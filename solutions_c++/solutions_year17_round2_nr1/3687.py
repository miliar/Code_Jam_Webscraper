#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    cin.tie(NULL);
    ios_base::sync_with_stdio(NULL);
    int casos,distancia,caballos,comienza;
    long double minimo,aux,res,velocidad;
    cin>>casos;
    cout << fixed;
    for(int i=1;i<=casos;i++)
    {
        cin>>distancia>>caballos;
        minimo=0;
        while(caballos--)
        {
            cin>>comienza>>velocidad;
            aux=(distancia-comienza)/velocidad;
            if(aux>minimo) minimo=aux;
        }
        res=distancia/minimo;
        if(minimo!=0)cout<<"Case #"<<i<<": "<<setprecision(6)<<res<<'\n';
        else cout<<"Case #"<<i<<": "<<setprecision(6)<< distancia<<'\n';
    }

    return 0;
}
