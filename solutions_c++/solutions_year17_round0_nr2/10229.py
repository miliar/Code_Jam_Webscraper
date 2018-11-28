#include <iostream>
using namespace std;

int main(){
    
    int numCases;
    unsigned long long int N;
    cin >> numCases;
    
    for (int i = 0; i < numCases; i++){
        cout << "Case #" << i+1 << ": ";
        cin >> N;
        while(1){
            unsigned long long K = N;
            unsigned short d = 10;
            
            while (K > 0){
                if (d >= K % 10) {
                    d = K % 10;
                    K /= 10;
                }
                else break;
            }
            
            if (K > 0) N -= 1;
            else{
                cout << N;
                break;
            }
        }
        
        cout << endl;
        cin.clear();
    }

    return 0;
}