#include <iostream>
using namespace std;

int main () {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string num;
        cin >> num;
        long long len = num.length();
        for (long long j = len - 1; j > 0; j--) {
            if (num[j] < num[j - 1]) {
                num[j - 1] = char(int(num[j - 1]) - 1);
                for (long long k = j; k < len; k++) {
                    num[k] = '9';
                }
            }
        }
        while (num[0] == '0') {
            num.erase(num.begin());
        }
        cout << "Case #" << i + 1 << ": " << num << endl;
    }
}
