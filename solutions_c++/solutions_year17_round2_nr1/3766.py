#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int main() {
    int t, k;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        double distance;
        int horseNum;
        double maxWaitTime = 0;
        cin >> distance >> horseNum;
        for(int j = 0; j< horseNum; j++) {
            int startDis, speed;
            double currentTime;
            cin >> startDis >> speed;
            currentTime = (double) (distance - startDis)/ speed;
            if (currentTime > maxWaitTime) {
                maxWaitTime = currentTime;
            }

        }

        double ans = distance /maxWaitTime ;
        // answer
        cout << "Case #" << i << ": ";
        cout << fixed << setprecision (6) << ans << endl;

    }
    return 0;
}
