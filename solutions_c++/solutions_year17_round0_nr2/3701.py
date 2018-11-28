#include <iostream>
#include <string>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        string num;
        cin >> num;
        for (int i = num.size() - 1; i > 0; i--) {
            if ((num[i] - '0') < (num[i - 1] - '0')) {
                for (int j = i; j < (int)num.size(); j++) {
                    num[j] = '9';
                }
                for (int j = i - 1; j >= 0; j--) {
                    if (num[j] != '0') {
                        num[j] = num[j] - 1;
                        break;
                    } else {
                        num[j] = '9';
                    }
                }
            }
        }
        int firstNonZero;
        for (firstNonZero = 0; firstNonZero < (int) num.size(); firstNonZero++) {
            if (num[firstNonZero] != '0') {
                break;
            }
        }
        cout << "Case #" << t + 1 << ": " << num.substr(firstNonZero) << endl;
    }

	return 0;
}

