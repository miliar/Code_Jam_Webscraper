#include <iostream>

using namespace std;

int main()
{
    int t = 0;
    cin >> t;
    for (int i=1; i<=t; i++) {
        unsigned long long data;
        cin >> data;
        for (unsigned long long j = data; j>0; j--) {
            bool sukses = false;
            bool cek = true;
            unsigned long long temp = j;
            int tempCek = -1;
            while (temp / 10 > 0) {
                if (tempCek == -1) tempCek = temp % 10;
                else {
                    if (tempCek >= temp % 10) {
                        tempCek = temp % 10;
                    } else {
                        cek = false;
                        break;
                    }
                }
                temp /= 10;
            }
            if (cek) {
                if (tempCek == -1) {
                    sukses = true;
                } else {
                    if (tempCek >= temp) {
                        sukses = true;
                    }
                }
            }

            if (sukses) {
                cout << "Case #" << i << ": " << j << endl;
                break;
            }
        }
    }
    return 0;
}
