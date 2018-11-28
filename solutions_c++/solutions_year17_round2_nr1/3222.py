#include <iostream>
#include <algorithm>

using namespace std;


int main() {
    int t;
    cin >> t;
    
    for (int i=1; i<=t; ++i) {
        long d;
        int n;
        double max_t = 0.0;
        cin >> d >> n;
        
        for (int i=0; i<n; i++) {
            long pos;
            int speed;
            double time;
            
            cin >> pos >> speed;
            
            time = (d - pos) / (double) speed;
            
            max_t = max(max_t, time);
        }
        
        cout.precision(6);
        cout << "Case #" << i << ": " << fixed << d / max_t << endl;
    }
    return 0;
}
