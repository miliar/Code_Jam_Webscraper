#include <iostream>
#include <iomanip>  

using namespace std; 
 
int main(int argc, char *argv[]) { 
	
    int tests;
    cin >> tests;
    for (int t = 1; t <= tests; t++) {
        int dist, horses;
        cin >> dist >> horses;
        
        double max = 0;
        for(int i = 0; i<horses; i++) {
            int k, s;
            cin >> k >> s;
            int diff = dist - k;
            double hours = diff / (double) s;
            max = max < hours? hours : max;
        }
        
        double speed = dist / max;
        
        cout << "Case #" << t << ": "<< setiosflags(ios::fixed) << setprecision(6) << speed << endl;
    }
    
    
	return 0; 
} 
