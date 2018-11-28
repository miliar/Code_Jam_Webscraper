#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int T, arr[19], res[19];
long long N;

int main() {
    cin >> T;
    for (int ca = 1; ca <= T; ca++) {
        cin >> N;
        long long m = N;
        int i = 0;
        while (m != 0) {
            int rem = m%10;
            arr[i] = rem;
            m = (m-rem)/10;
            i++;
        }

        int top = 9;
        memset(res, 0, sizeof(res));

        for (int j = 0; j < i; j++) {
            if (arr[j] <= top) {
                res[j] = arr[j];
                top = arr[j];
            }
            else if (arr[j] != 0) {
                res[j] = arr[j] - 1;
                top = arr[j] - 1;
                for (int k = j-1; k >=0; k--) {
                    res[k] = 9;
                }
            }

            
        }
        // for (int f = 0; f < i; f++) {
        //     cout<<res[f];
        // }

        int h = i-1;
        if (h > 0 && res[h] == 0) h--;

        cout << "Case #" << ca << ": ";
        for(; h >= 0; h--) {
            cout << res[h];
        }
        cout << endl;


    }

}