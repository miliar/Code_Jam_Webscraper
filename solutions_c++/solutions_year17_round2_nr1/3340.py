#include <iostream>
#include <iomanip>
#include <stdio.h>

using namespace std;

int main() {

	int T; cin >> T;
    double D,N,K,S;
    
	for(int t = 0; t < T; t++) {
        cin >> D >> N;
        
        double v = -1.0;
        
        for(int n = 0; n < N; n++){
            cin >> K >> S;
            
            if(v<0)  {
                v = D*S/(D-K);
            } else {
                double tmp = D*S/(D-K);
                if (tmp < v) v = tmp;
            }       
        }
        
        
        cout << "Case #" << t+1 << ": ";
        printf("%f\n", v);
        
	}

	return 0;
}