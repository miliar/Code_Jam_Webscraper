#include<iostream>
#include<string>

using namespace std;

int main(){
    long long T, contam,cont,cases = 1, S2,aux;
    string S;
    cin >> T;

    while (T != 0){
        cont = 0;
        contam = 0;
        cin >> S2;
        S = to_string(S2);
        contam = S.size();
        if(contam != 1){
            for (int k = 0; k < contam; k++){
                for(int x = 0 ; x < contam; x++){
                    if(x != contam - 1){
                        if (S[x] > S [x + 1]){
                            S[x] = S[x] - 1;
                            while(x < contam){
                                // cout << "cadena ants: " << S <<endl;
                                S[x + 1] = 57;
                                // cout << "cont for: " << cont << endl;
                                x++;
                                // cout << "cadena desp: " << S <<endl<<endl;
                            }
                            // x = 0;
                        }
                    }
                }
            }
        }
        if( S[0] == '0')
            S.erase(0,1);
        cout << "Case #" << cases <<": " << S <<endl;
        cases++;
        T--;
    }
    return 0;
}