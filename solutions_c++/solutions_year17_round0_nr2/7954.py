#include <iostream>
#include <stdlib.h>
#include <fstream>

using namespace std;

int main() {
    long long int cases, n, n2, cnt, cnt2, ind;
    char num[20];
    ifstream cin;
    ofstream cout;
    cin.open("large.in");
    cout.open("large.out");
    cin >> cases;
    for (int j = 1; j <= cases; j++) {
        cin >> n;
        cnt = 0;
        if (n < 10) {
            cout << "Case #" << j << ": " << n << endl;
            continue;
        }
        n2 = n;
        while (n2 != 0) {
            n2 /= 10;
            cnt++;
        }
        cnt2 = cnt - 1;
        while (cnt2 >= 0) {
            n2 = n % 10;
            num[cnt2] = (n2 + '0');
            n /= 10;
            cnt2--;
        }
        ind = cnt;
        for (int i = cnt - 1; i > 0; i--) {
            if (num[i - 1] > num[i]) {
                ind = i;
                num[i - 1]--;
            }
        }
        for (int i = ind; i < cnt; i++) {
            num[i] = '9';
        }
        cout << "Case #" << j << ": ";
        if (num[0] != '0') {
            cout << num[0];
        }
        for (int i = 1; i < cnt; i++) {
            cout << num[i];
        }
        cout << endl;
    }
    cin.close();
    cout.close();
    return 0;
}
