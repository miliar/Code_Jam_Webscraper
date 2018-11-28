
#include <iostream>

using namespace std;
bool  revisar(int n);


int main(){
    int tc;
    cin>>tc;
    for(int n=1;n<=tc;++n){
        int num;
        cin>>num;
        bool entrar=false;
        for(int j=num;j>1;--j){
            if(revisar(j))
            {
                entrar=true;
                cout<<"Case #"<<n<<": "<<j<<endl;

                break;
            }

        }
        if(!entrar)
            cout<<"Case #"<<n<<": "<<num<<endl;

    }

}


bool  revisar(int n){
    int anterior=9,aux=n;
    while(aux!=0){
        n=aux%10;
        if(n>anterior)
            return false;
        aux=aux/10;
        anterior=n;

    }
    return true;

}
