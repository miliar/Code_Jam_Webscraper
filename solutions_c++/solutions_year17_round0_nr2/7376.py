#include <bits/stdc++.h>

using namespace std;

int main()
{
#ifdef DEBUG
    freopen("B-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
#endif // DEBUG
    std::ios::sync_with_stdio(false);
    int n;
    cin >> n;
    for(int i = 0; i < n; i++) {
        long long a;
        cin >> a;
        long long b = a;
        int digitCount = 0;
        while(b != 0) {
            b /= 10;
            digitCount++;
        }
        b = a;
        vector<int> digits(digitCount);
        for(int j = digitCount - 1; j >= 0 ; j--) {
            digits[j] = b%10;
            b /= 10;
        }
        cout << "Case #" << i+1 << ": ";
        if(digitCount == 1) {
            cout << a << endl;
            continue;
        }
        for(int j = digitCount - 2; j >= 0; j--) {
            if(digits[j] > digits[j+1]) {
                if(digits[j] != 0) {
                    digits[j]--;
                    for(int k = j+1; k < digitCount; k++) {
                        digits[k] = 9;
                    }
                }
            }
        }
        for(int j = 0; j < digitCount; j++) {
            if(!(digits[j] == 0 && j == 0))
                cout << digits[j];
        }
        cout << endl;
    }
    return 0;
}
