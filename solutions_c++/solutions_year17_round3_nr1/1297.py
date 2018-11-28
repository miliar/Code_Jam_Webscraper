#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int ti=0; ti<t; ti++) {
        long n, k, r[1010], h[1010];
        cin >> n >> k;
        for (int i=0; i<n; i++) {
            cin >> r[i] >> h[i];
        }
        long temp;
        for (int i=0; i<n; i++) {
            for (int j=0; j<i; j++) {
                long temp1 = r[i]*h[i];
                long temp2 = r[j]*h[j];
                if (temp1 > temp2) {
                    temp = r[i]; r[i]=r[j]; r[j]=temp;
                    temp = h[i]; h[i]=h[j]; h[j]=temp;
                }
            }
        }
        // for (int i=0; i<n; i++) {
        //     cout << r[i] << " ";
        // }
        // cout << endl;
        long ans = 0;
        for (int i=0; i<n; i++) {
            int flag = 1;
            long temp_ans = 2*r[i]*h[i];
            for (int j=0; j<n; j++) {
                if (i != j && r[j] <= r[i] && flag < k) {
                    flag++;
                    temp_ans += 2*r[j]*h[j];
                    // cout << "r[i] = " << r[i] << ", choose " << r[j] << endl;
                }
            }
            if (flag == k) {
                temp_ans += r[i]*r[i];
                // cout << "temp_ans " << temp_ans << endl;
                if (temp_ans > ans) {
                    ans = temp_ans;
                }
            }
        }
        // cout << ans << endl;
        // setprecision(6);
        double out = ans*M_PI;
        cout << "Case #" << ti+1 << ": " << setiosflags(ios::fixed)<<
            setprecision(9) << out << endl;
    }
}
