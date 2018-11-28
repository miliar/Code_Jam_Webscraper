#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
    int T;  cin>>T;
    
    for (int t = 1; t <= T; ++t) {
        int Ac, Aj; cin>>Ac>>Aj;
        
        if (Ac <= 1 && Aj <= 1) {
            cout<<"Case #"<<t<<": 2\n";
            for (int i = 0; i < Ac+Aj; ++i) {
                int f, t;   cin>>f>>t;
            }
        } else {
            int f1, t1, f2, t2; cin>>f1>>t1>>f2>>t2;
            if (f1 > f2) {
                swap(f1, f2);
                swap(t1, t2);
            }
            
            int d1 = abs(t2 - f1);
            int d2 = abs(t1 - f2 + 1440);
            
            if (min(d1, d2) > 720)
                cout<<"Case #"<<t<<": 4\n";
            else 
                cout<<"Case #"<<t<<": 2\n";
        }
    }
    
    return 0;
}
