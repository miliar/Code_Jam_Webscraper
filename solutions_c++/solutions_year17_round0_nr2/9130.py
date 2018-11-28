#include <iostream>
#include <cstring>
using namespace std;

int main() {
    int a[19];
    long long int b;
    int n;
    cin >> n;
    for (int oi = 0; oi < n; oi++) {
        memset(a, sizeof(a), 0);
        cin >> b;
        long long int res = b/10;
        int pos = 1;
        int curDigit = b % 10, newDigit = 0; // First digit
        int foundPos = -1;
        while (res > 0) {
            int newDigit = res % 10;
            if (newDigit > curDigit) {
                foundPos = pos;
                curDigit = newDigit - 1;
            }
            else {
                curDigit = newDigit;
            }
            pos++;
            res /= 10;
        }
        res = b;
        int count = 0;
        while (res > 0) {
            int digit = res % 10;
            a[count++] = digit;
            res /= 10;
        }
        cout << "Case #" << oi + 1 << ": ";
        for (int i = count - 1; i >= 0; i--) {
            if (i < foundPos)
                cout << "9";
            else if (i == foundPos && i == count - 1 && a[i] == 1)
                cout << "";
            else if (i == foundPos)
                cout << a[i] - 1;
            else
                cout << a[i];
        }
        cout << endl;
    }
    return 0;
}
