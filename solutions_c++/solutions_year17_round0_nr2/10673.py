#include <iostream>
using namespace std;

int l = 20;

long long ltn(long long n)
{
    int a[l];
    int i = l - 1;
    for (; n > 0; i--) {
        a[i] = n % 10;
        n /= 10;
    }

    while (true) {

        bool tidy = true;
        for (int j = i + 1; j < l - 1; j++) {
            if (a[j] > a[j + 1]) {
                tidy = false;
                break;
            }
        }

        if (tidy)
            break;

        for (int j = i + 1; j < l - 1; j++) {
            if (a[j] > a[j + 1]) {
                a[j]--;
                for (int k = j + 1; k < l; k++) {
                    a[k] = 9;
                }
            }
        }
    }

    long long r = 0;
    for (int j = i + 1; j < l; j++) {
        r += a[j];
        r *= 10;
    }
    return r / 10;
}

int main()
{
    int t;
    long long n;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> n;
        cout << "Case #" << i << ": " << ltn(n) << endl;
    }
}