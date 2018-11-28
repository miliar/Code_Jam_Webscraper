#include <iostream>
#include <iomanip>
#include <map>

using namespace std;

int main() {
    long long ins, cur;
    double dest, slowest;
    
    slowest = 100000000000;

    cin >> ins;
    
    for (int i=0; i< ins; i++) {
        cin >> dest >> cur;

        slowest = 0;
        
        for (int j=0; j<cur; j++) {
            double start, speed;
            
            cin >> start >> speed;
            
            double time = (dest-start)/speed;
            
            //cout << dest  << ' ' << start << ' ' << speed;
            
            if (time>slowest) slowest = time;
        }
        
        cout << fixed << setprecision(6);
        cout << "Case #" << i+1 << ": " << dest/slowest << "\n"; 
    }
    
}

