#include<iostream>
using namespace std;
int main()
{
    cin.tie(NULL);
    ios_base::sync_with_stdio(NULL);

    int casos,tam,comienza;
    string entrada;
    bool correcto;
    cin>>casos;
    for(int a=1;a<=casos;a++)
    {
        cin>>entrada;
        comienza=0;
        correcto=true;
        tam=entrada.size()-1;
        for(int i=0;i<tam;i++)
        {
            if (entrada[i+1]<entrada[i])
            {
                correcto=false;
                break;
            }else if(entrada[i+1]>entrada[i]) comienza=i+1;
            //cout<<entrada<<endl;
        }
        if(!correcto)
        {
            entrada[comienza]--;
            for(int i=comienza;i<tam;i++)
            {
                entrada[i+1]='9';
            }
        }
        if(entrada[0]=='0') entrada.erase(entrada.begin());
        cout<<"Case #"<<a<<": "<<entrada<<'\n';
    }

    return 0;
}
