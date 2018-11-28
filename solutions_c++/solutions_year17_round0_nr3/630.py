#include <iostream>

using namespace std;

typedef struct{
    long long int minimo,maximo;
}tipo_retorno;


tipo_retorno busca(long long int n,long long int k){
    long long int l,r,nextN,nextK;

    r = l = n/2;
    if(n%2==0)r--;

    tipo_retorno x;
    x.minimo = min(r,l);
    x.maximo = max(r,l);

    if(k==1)return x;

    if(k%2==0)
        nextN = l;
    else
        nextN = r;

    nextK = k/2;

    return busca(nextN,nextK);
}


int main (){
    int teste;
    cin >> teste;


    for(int t=1;t<=teste;t++){
        long long int n,k;

        cin >> n >> k;

        tipo_retorno resp = busca(n,k);

        cout << "Case #" << t << ": " << resp.maximo << " " << resp.minimo;

        cout << "\n";
    }




    return 0;
}
