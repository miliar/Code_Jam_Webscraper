#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    long long n, k, t;
    unsigned long long *seka, *seka1;
    seka = new unsigned long long[61];
    seka1 = new unsigned long long[61];
    seka[0] = seka1[0] = 1;
    for (int i = 1; i < 61; i++) {
        seka[i] = seka[i - 1] * 2;
        seka1[i] = seka1[i - 1] + seka[i];
        //cout << seka[i] << " " << seka1[i] << endl;
    }
    cin >> t;
    for (int p = 1; p <= t; p++) {
        cin >> n >> k;
        long long a, b = 0;
        for (int i = 0; i < 61; i++) {
            if (k <= seka1[i]) {
                a = seka[i];
                if (i != 0) {
                    b = seka1[i - 1];
                }
                break;
            }
        }
        long long k1 = k - b;
        b = n - b;
        long long c = b / a, d = b % a;
        if (k1 <= d) {
            c++;
        }
        long long min = c / 2, max = min - !(c % 2);
        cout << "Case #" << p << ": " << min << " " << (max >= 0 ? max : 0) << endl;
    }
    delete[] seka;
    delete[] seka1;
    //while (1);
    return 0;
}
