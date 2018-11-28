#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main () {
    freopen("/Users/bowbowbow/Downloads/A-large.in", "r", stdin);
    freopen("/Users/bowbowbow/Downloads/A-large.out", "w", stdout);
    int T;
    cin >> T;
    for(int t=1;t<=T;t++) {
        double D;
        int N;
        cin >> D >> N;
        
        double ans = 0.0;
        for(int i=1;i<=N;i++) {
            double K, S;
            cin >> K >> S;
            if(ans < (D-K)/S) {
                ans = (D-K)/S;
            }
        }
        cout << fixed;
        cout.precision(7);
        cout << "Case #"<< t << ": " << D/ans << endl;
    }
    return 0;
}
