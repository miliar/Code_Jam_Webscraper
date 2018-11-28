#include <iostream>
#include<string>

using namespace std;

//int buscar(string pal,int k);
void voltear(string &pal,int k,int ind);
void voltear2(string &pal,int k,int ind);

int main()
{
    int casos;
    cin>>casos;
    for(int l=0; l<casos; l++)
    {
        string fila,aux;
        cin>>fila;
        aux=fila;
        int k,iz=0,der,pan=0;
        cin>>k;
        bool lado=true,entro=false;

        der=k-1;

        int i,contador=0;
        for(int o=0; o<fila.size(); o++)
        {
            if(fila[o]=='-')
            {
                entro=true;
                break;
            }
        }
        if(!entro)
        {
            cout<<"Case #"<<l+1<<": "<<0<<endl;
            continue;
        }
        entro=false;
        /* if(fila.size()<2*k){
             for(int z=k;z<fila.size()-k;z++){
                 if(fila[z]=='-')
                     entro=true;
             }
             if(entro){
                 cout<<"Case #"<<l+1<<": "<<"IMPOSSIBLE"<<endl;
                 continue;
             }
         }*/
        for(int j=0; j<10*fila.size(); j++)
        {
            entro=false;
            if(lado)
            {
                for(int i=0; i<fila.size(); ++i)
                {
                    if(fila[i]=='-'&&i<=fila.size()-k)
                    {
                        entro=true;
                        contador++;
                        voltear(fila,k,i);
                        lado=false;
                        break;
                    }

                }
            }
            else
            {
                for(int i=fila.size(); i>=0; --i)
                {
                    if(fila[i]=='-'&&i>=k)
                    {
                        entro=true;
                        contador++;
                        voltear2(fila,k,i);
                        lado=true;
                        break;
                    }
                }
            }

            if(!entro)
                break;

        }
        entro=false;
        for(int o=0; o<fila.size(); o++)
        {
            if(fila[o]=='-')
            {
                entro=true;
                break;
            }
        }
        if(!entro)
        {
            cout<<"Case #"<<l+1<<": "<<contador<<endl;

        }
        else
            cout<<"Case #"<<l+1<<": "<<"IMPOSSIBLE"<<endl;



    }

}

void voltear(string &pal,int k,int ind)
{
    for(int i=ind; i<ind+k; ++i)
    {
        if(pal[i]=='-')
        {
            pal[i]='+';
        }
        else
        {
            pal[i]='-';
        }
    }
}

void voltear2(string &pal,int k,int ind)
{
    for(int i=ind; i>ind-k; --i)
    {
        if(pal[i]=='+')
            pal[i]='-';
        else
        {
            pal[i]='+';
        }
    }

}

/*
int buscar(string pal,int k){
    int mayor=0,res=k-1;
    int der=k-1,izqui=0;
    bool iz=false;
    for(int i=0;i<k;++i){
        if(pal[i]=='-'&&pal[izqui]=){
            mayor++;
            cout<<endl<<"llllllll";
        }
    }
    if(pal[0]=='-')
        iz=true;;
    int cont=mayor;
    for(int i=k;i<pal.size();++i){
        iz++;
        der++;
        if(iz)
            cont--;
        if(pal[i-k]=='-'){
            iz==true;
        }
        else{
            iz=false;
        }
        if(pal[der]=='-')
            cont++;
        if(cont>mayor){
            mayor=cont;
            res=i;
        }
    }
    return res-k+1;
}
*/
