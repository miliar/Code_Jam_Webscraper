#include <iostream>
#include <string> 
#include <cstring>

using namespace std;

int main () {
    int T;
    cin >> T;
    for (int Tc=1; Tc<=T; Tc++) {
        
        string S;
        int K;
        int count = 0;
        bool result = true;
        
        cin >> S >> K;
        
        int i=0;
        for (i=0; i<S.length()-K+1; i++) { 
            // l=6, k=3, then i=0,1,2,3 [4,5]
            
            if (S[i] == '+') continue;
            
            // else S[i] == '-';
            count++;
            for (int j=0; j<K; j++) {
                int x = i+j;
                if (S[x] == '+') S[x] = '-';
                else if (S[x] == '-') S[x] = '+';
            }
            
        }
        
        for (; i<S.length(); i++) {
            if (S[i] == '-') {
                result = false;
                break;
            }
        }
        
        if (result) cout << "Case #" << Tc << ": " << count << "\n";
        else cout << "Case #" << Tc << ": IMPOSSIBLE\n";
        
    }
}