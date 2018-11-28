#include<iostream>
using namespace std;
int main()
{
    cin.tie(NULL);
    ios_base::sync_with_stdio(NULL);
    int casos,tam,tam2,K,vueltas;
    bool posible;
    cin>>casos;
    string pan;
    for(int a=1;a<=casos;a++)
    {
        cin>>pan>>K;
        vueltas=0;
        posible=true;
        tam=pan.size();
        tam2=pan.size()-K+1;
        for(int i=0;i<tam2;i++)
        {
            if(pan[i]=='-')
            {
                for(int j=0;j<K;j++)
                {
                    pan[i+j]= (pan[i+j]=='-')? '+': '-';
                }
                vueltas++;
            }
        }
        for(int i=tam2;i<tam;i++)
        {
            if(pan[i]=='-')
            {
                posible=false;
                break;
            }
        }
        if(posible) cout<<"Case #"<<a<<": "<<vueltas<<'\n';
        else cout<<"Case #"<<a<<": IMPOSSIBLE"<<'\n';
    }
}
