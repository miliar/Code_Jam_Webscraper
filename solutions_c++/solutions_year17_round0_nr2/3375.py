#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main() {
    int T;
    int A[20];
    unsigned long long D=1, N, R=0;
    int G=0;;
    
    cin >> T;  // read t. cin knows that t is an int, so it reads it as such.
    
    
    
    for (int t = 1; t <= T; ++t) {
        cin >> N;  // read n and then m.

        
        for (int i=0; i<=18; i++) {
            if (N/D == 0) break;
            D *= 10;
            G++;
        }
        D/=10;
        
        for (int i=0;i<G;i++) {
            A[i] = N/D;
            N -= (N/D)*D;
            D /= 10;
        }

        for (int i=1; i<G; i++) {
            if (A[G-i] < 0) {
                A[G-i] = 9;
                A[G-i-1]--;
            }
            if (A[G-i] < A[G-i-1] || A[G-i] == 0) {
                A[G-i] = 9;
                if (G-i+1 < G)
                    A[G-i+1] = 9;
                A[G-i-1]--;
            }
        }
        
        D = 1;
        for (int i=1; i<=G; i++) {
            R += A[G-i] * D;
            D*=10;
        }
        cout <<"Case #" << t <<": " << R << endl;
        
        D = 1;
        R = 0;
        G = 0;
        
        for (int i=0; i<=18; i++) A[i] = 0;
    }
}
