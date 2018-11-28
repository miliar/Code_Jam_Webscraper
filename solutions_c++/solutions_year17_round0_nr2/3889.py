#include <iostream>
#include <cstdio>

using namespace std;

int num[30];

int main()
{
    freopen("txt.in", "r", stdin);
    freopen("txt.out", "w", stdout);

    int t;

    cin >> t;
    int64_t x;
    for(int i = 1; i <= t; ++i) {
        cin >> x;

        int k = 0;
        while(x) {
            num[++k] = x % 10;
            x /= 10;
        }

        bool dat = false;
        for(int z = 1; z < k; ++z) {
            if(dat && num[z] > 0) {
                num[z]--;
                dat = false;
            }

            if(num[z] < num[z + 1]) {
                int ii = z;
                while(num[ii] != 9 && ii >= 1) {
                    num[ii] = 9;
                    ii--;
                }

                num[z + 1]--;
            }
        }

        x = 0;
        while(num[k] == 0) k--;
        for(int j = k; j >= 1; --j) {
            x = x * 10 + num[j];
        }

        cout << "CASE #" << i << ": " << x << "\n";
    }

    return 0;
}
