#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <fstream>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main() {
    int T;
    long long N, M;
    ofstream f;
    
    cin >> T;  // read t. cin knows that t is an int, so it reads it as such.
    
    for (int t = 1; t <= T; ++t) {
        cin >> N >> M;  // read n and then m.
        long long max = 0;
        long long min = 0;
        
        while (M > 0) {
            if (M%2 == 0) {
                long long L = (N+1)/2-1;
                long long R = N-(N+1)/2;
                N = R;
                if (L < 0) L = 0;
                if (R < 0) R = 0;
                
                if (L > R) {
                    max = L;
                    min = R;
                }
                else {
                    max = R;
                    min = L;
                }
                M = M/2;
            }
            else {
                long long L = (N+1)/2-1;
                long long R = N-(N+1)/2;
                N = L;
                if (L < 0) L = 0;
                if (R < 0) R = 0;
                
                if (L > R) {
                    max = L;
                    min = R;
                }
                else {
                    max = R;
                    min = L;
                }
                M = M/2;
            }
        }

        cout <<"Case #" << t <<": " << max << " " << min << endl;
        

    }
    
    return 0;
}
