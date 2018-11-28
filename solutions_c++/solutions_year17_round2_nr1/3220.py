#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    ifstream cin("input.txt");
    ofstream cout("output.txt");
    
    int test;
    cin >> test;

    int num = 0;

    while (test--) {

        ++num;

        int d, n;
        cin >> d >> n;
        long double ans = -1;

        for (int i = 0; i < n; ++i) {
            long double k, s;
            cin >> k >> s;  
            if (ans == -1)
                ans = s * d / (d - k);
            else
                ans = min(ans, s * d / (d - k));
        }
      
        cout << "Case #" << num << ": " << fixed << setprecision(10) << ans << '\n';

    }


    return 0;
}