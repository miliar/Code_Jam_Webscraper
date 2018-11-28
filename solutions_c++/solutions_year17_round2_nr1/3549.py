#include <iostream>
#include <cstdio>
using namespace std;

int main(){
    int tc, hs;
    long long dist;
    double t;
    cin >> tc;
    for (int i=0;i<tc;i++) {
        cin >> dist >> hs;
        t = -1;
        for (int j=0;j<hs;j++) {
            long long dist0;
            int speed;
            cin >> dist0 >> speed;
            double temp = (dist - dist0) / (double) speed;
            if (t == -1) {
                t = temp;
            } else if (temp > t) {
                t = temp;
            }
        }
        // printf("Header: %lld %d\n", dist, hs);
        // printf("Total distance: %lld, total time: %.3f\n", dist, t);
        double result = dist / t;
        printf("Case #%d: %.6f\n", i+1, result);
    }
}
