#include <iostream>
#include <algorithm>

#define N 1000000

using namespace std;

int main() {

    int t;
    cin >> t;

    long n, k;
    int slots[N];
    int counter[N];
    for (int l = 0; l < t; l++) {
        cin >> n >> k;
        for (int i = 0; i < n; i++) counter[i] = 0;
        counter[n-1] = 1;
        long m = n-1, ma, mi;
        for (int i = 0; i < k; i++) {
            for (int j = m; j >= 0; j--) 
                if (counter[j] > 0) {
                    m = j;                    
                    break;
                }             
            mi = m/2;
            ma = m - mi;            
            counter[mi-1]++;
            counter[ma-1]++;
            counter[m]--;
        }

        cout << "Case #" << (l+1) << ": " << ma << " " << mi << endl;
    }

    return 0;
}

