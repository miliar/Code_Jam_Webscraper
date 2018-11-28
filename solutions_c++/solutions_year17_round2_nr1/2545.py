#include <iostream>
#include <bitset>
#include <string>

using namespace std;

typedef unsigned int uint;

int get_blank(string s, int start) {
    uint i = start;
    
    for (; i < s.size() && s[i] != '-'; i++);

    return i;
}


int main() {
    int t;
    cin >> t;

    for (int x = 0; x < t; ++x) {
        int d, n;
        cin >> d >> n;

        uint horses[n];
        double speed[n];

        for (int i = 0; i < n; i++) {
            cin >> horses[i] >> speed[i];
        }

        double max_speed = -1;
        
        for (int i =0; i<n; i++) {

            double time = (d - horses[i]) / speed[i];
            double ispeed = d / time;

            if (ispeed < max_speed || max_speed == -1) {
                max_speed = ispeed;
            }
        }

        cout << "Case #" << x + 1 << ": ";
        // for (int k = 0; k < r; k++) {
        //     cout << horses[k] << '\n';
        // }
        
        printf("%.6f\n", max_speed);
    }
}
