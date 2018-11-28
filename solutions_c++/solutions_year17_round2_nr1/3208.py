#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;
#define MAX 100010

int main() {
//    #ifndef ONLINE_JUDGE
//    freopen("/Users/d/Documents/A-large.in", "rt", stdin);
//    #endif
    int K;
    cin >> K;
    for(int k=1;k<=K;k++) {
        int d, n;
        vector<long double> data;
        cin >> d >> n;
        int ki, mi;
        for(int i=0;i<n;i++) {
            cin >> ki >> mi;
            long double temp = (d - ki)*1.0 / mi;
            data.push_back(temp);
        }
        long double m=data[0];
        for(int i=1;i<n;i++) {
            m = max(data[i], m);
        }
        long double r = d / m;
        cout << fixed << setprecision(6);
        cout << "Case #" << k << ": " << r << endl;
    }
    return 0;
}
