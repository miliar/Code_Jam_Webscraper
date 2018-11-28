#include <iostream>

using namespace std;

int main (){
    int teste;
    cin >> teste;

    string numero;

    for(int t=1;t<=teste;t++){
        cin >> numero;

        int tam = numero.size();

        int i = 0;

        while (i<tam-1){

            if(numero[i] <= numero[i+1])
                i++;
            else{

                numero[i]--;

                for(int j=i+1;j<tam;j++)
                    numero[j] = '9';

                i = 0;
            }
        }


        bool leadingZeros = true;

        cout << "Case #" << t << ": ";
        for(int i=0;i<tam;i++){
            if(!leadingZeros || (leadingZeros && numero[i] != '0')){
                cout << numero[i];
                leadingZeros = false;
            }else{
                if(numero[i] != '0')
                    leadingZeros = false;
            }
        }

        cout << "\n";
    }




    return 0;
}
