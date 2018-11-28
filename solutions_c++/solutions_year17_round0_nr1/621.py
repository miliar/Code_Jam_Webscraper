#include <iostream>

using namespace std;

int main (){
    int teste;
    cin >> teste;

    string pancake;
    int k;

    for(int t=1;t<=teste;t++){
        cin >> pancake;
        cin >> k;

        int tam = pancake.size();
        int flip = 0;

        for(int i=0;i<=tam-k;i++){

            if(pancake[i] == '-'){

                flip++;

                for(int j=i;j<i+k;j++){
                    if(pancake[j] == '-')
                        pancake[j] = '+';
                    else
                        pancake[j] = '-';
                }

            }

        }

        //cout << pancake << endl;

        bool impossible = false;
        for(int i=0;i<tam;i++){
            if(pancake[i] == '-'){
                impossible = true;
                break;
            }
        }

        cout << "Case #" << t << ": ";
        if(impossible)
            cout << "IMPOSSIBLE\n";
        else
            cout << flip << "\n";

    }

    return 0;
}
