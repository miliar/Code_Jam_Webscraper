#include<iostream>

using namespace std;

int main(){
    double T,D,N,cases = 1, K, S,tmay = 0,V;
    cin >> T;
    for(int t = 0; t < T; t++){
        tmay = 0;
        cin >> D >> N;
        for(int n = 0; n < N; n++){
            cin >> K >> S;
            if(tmay < (D - K)/S)
                tmay = (D - K)/S;
        }
        V = D/tmay;
        // cout << "Case #" << cases << ": " << V <<endl;
        printf("Case #%.f: %.6f \n", cases, V);
        cases++;
    }
    return 0;
}