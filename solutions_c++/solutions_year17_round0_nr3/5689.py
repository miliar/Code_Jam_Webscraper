
#include <iostream>
#include <string.h>

using namespace std;


int main(void) {
    int T;
    unsigned long long N;
    unsigned long long K;
    unsigned long long max;
    unsigned long long min;
    
    cin >> T;
    
    for (int t = 0; t < T; t++) {
        cin >> N;
        cin >> K;
        
        if (N == 1) {
            max = 0;
            min = 0;
            cout << "Case #" << t+1 << ": " << max << " " << min << endl;
            continue;
        } else if (K == 1) {
            if (N%2 == 1) {
                min = N / 2;
                max = N / 2;
            } else {
                min = N / 2 - 1;
                max = N / 2;
            }
            cout << "Case #" << t+1 << ": " << max << " " << min << endl;
            continue;
        }
        
        while (K > 1) {
            N -= 1;
            K -= 1;
            
            if (K == 1) {
                N = (N+1) / 2;
                break;
            }
            
            N = (N+(K%2)*(N%2)) / 2;
            K = (K+1) / 2;
        }
        
        if (N%2 == 1) {
            min = N / 2;
            max = N / 2;
        } else {
            min = N / 2 - 1;
            max = N / 2;
        }
        
        cout << "Case #" << t+1 << ": " << max << " " << min << endl;
    }
    
    return 0;
}
