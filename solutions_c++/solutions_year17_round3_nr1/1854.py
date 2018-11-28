#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>

#define pi 3.1415926535

using namespace std;

int main() {        

    int t, p = 1;
    int n, k;
    double r[1000], h[1000];
    for (cin >> t; t--;) {
        cin >> n >> k;
        for (int i = 0; i < n; i++) {
            cin >> r[i] >> h[i];
        }

        long double area = 0;        
        bool f = true;
        int br = 0;
        while (k--) {
            long double maa = 0;
            int mi;
            for (int i = 0; i < n; i++) {                
                if (r[i] == -1) continue;
                long double tempa = 0;
                if (f) {
                    tempa = pi * r[i] * r[i];                    
                }
                if (!f and r[i] > br) {
                    tempa = pi * r[i] * r[i] - (pi * br * br);
                }
                tempa += 2 * pi * r[i] * h[i];                
                if (tempa > maa) {
                    mi = i;
                    maa = tempa;                    
                }
            }            
            if (f) f = 0;                
            if (r[mi] > br) br = r[mi];
            area += maa;
            r[mi] = -1;
            h[mi] = -1;            
        }

        cout << "Case #" << p++ << ": ";
        printf("%0.7Lf",area);
        cout <<  endl;
    }

    return 0;
}