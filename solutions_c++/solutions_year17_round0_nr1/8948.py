// Example program
#include <iostream>
#include <string>

using namespace std;

int main()
{
  // input params
  int T, K;
  string S;
  
  // extend params
  int minus_signs;
  int time_oversized;
  bool impossible;
  
  cin >> T;
  for (int i = 0; i<T; i++){
       cin >> S;
       cin >> K;
       
       int n = S.size();
       minus_signs = 0;
       time_oversized = 0;
       impossible = false;
    }
       for(int j = 0; j<=n-K; j++){
            if(S[j] == '-'){
                minus_signs ++;
                time_oversized ++;
                for (int k=0; k<K; k++){
                    if(S[k+j]=='-'){
                        S[k+j] = '+';
                    }else{
                        S[k+j] = '-';
                    }
                }
            }
            if(j == n-K){
                for (int k=0; k<K; k++){
                    if(S[k+j]=='-'){
                        minus_signs ++;
                        impossible = true;
                    }
                }
            }
        }
        if (minus_signs == 0){
            cout << "Case #" << i+1 << ": 0" << endl;
        }
        else if (impossible){
            cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
        }
        else {
            cout << "Case #" << i+1 << ": " << time_oversized << endl;
       }
  }
}