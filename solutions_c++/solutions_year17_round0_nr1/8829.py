#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main() {
    ifstream fin("/Users/uelnily/Downloads/A-large.in");
    ofstream fout("/Users/uelnily/Downloads/A-large.out");
    
    int T, K, C;
    string S;
    
    fin >> T;
    C = T;
    while(T--) {
        int ans = 0, np = 0;
        fin >> S >> K;
        
        for(int i = 0; i <= (S.length() - K); i++) {
            if(S[i] == '-') {
                S[i] = '+';
                for(int j = 1; j < K; j++) {
                    if(S[i+j] == '+')
                        S[i+j] = '-';
                    else if (S[i+j] == '-')
                        S[i+j] = '+';
                }
                ans++;
            }
        }
        for(long int i = (S.length() - K); i < S.length(); i++) {
            if(S[i] == '-') {
                np = 1;
            }
        }
        
        if(np) {
            fout << "Case #" << C-T << ": IMPOSSIBLE" << endl;
            continue;
        }
        
        fout << "Case #" << C-T << ": " << ans << endl;
    }
    
    return 0;
}
