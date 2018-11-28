#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        bool stall[1000002] = {};
        int n, p;
        cin >> n >> p;
        stall[0] = 1, stall[n+1] = 1;
        for (int j = 0; j < p; ++j) {
            int maxD = 0, minD = 0, lD = 0, rD = 0, place;
            for (int k = 1; k <= n; ++k) { 
                if (stall[k]) continue;
                int pos = k - 1;
                while (!stall[pos]) --pos;
                lD = k - pos-1;
                pos = k + 1;
                while (!stall[pos]) ++pos;
                rD = pos - k-1;
                if (min(lD, rD) > minD || (min(lD,rD) == minD && max(lD,rD) > maxD))  {
                    minD = min(lD, rD);
                    maxD = max(lD, rD);
                    place = k;
                }
            }
            stall[place] = 1;
            if (j == p - 1) {
                //cout << place << endl;
                cout << "Case #" << i << ": " << maxD << " " << minD << endl;
            }
        }
        
    } 
    return 0;
}
