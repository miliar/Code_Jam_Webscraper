#include <iostream>
#include <cstdio>
#include <cstring> // memset
#include <algorithm> // sort
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <=T; i++) {
        int k, d;
        cin >> k >> d;
        double t = 0;
        for (int j = 0; j < d; j++) {
            double a, b;
            cin >> a >> b;
            double c;
            c = (k - a) / b;
            if (c > t)
                t = c;
        }
        printf("Case #%d: %f\n", i, k/t);
    }
    return 0;
}
