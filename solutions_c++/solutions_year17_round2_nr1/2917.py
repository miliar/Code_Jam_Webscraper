#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <cstring>
#include <cstdio>
#include <iomanip>
#include <vector>
#include <queue>
#include <cmath>
#include <unordered_map>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main() {
    int t,d,n,k;
    string s;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i1 = 1; i1 <= t; ++i1) {
        cin >> d >> n;
        cout << "Case #" << i1 << ": ";
        double lastarr = 0;
        for(int i2 = 0; i2 < n; ++i2){
            int start, speed;
            cin >> start >> speed;
            lastarr = max(lastarr, ((double)d-start)/speed);
        }
        double ret = (double)d/lastarr;
        printf("%6f\n", ret);
        // cout<<setiosflags(ios::fixed)<<setprecision(6)<<(float)d/lastarr<<endl;
        
    }
    return 0;
}