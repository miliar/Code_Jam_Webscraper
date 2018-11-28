#include <iostream>

using namespace std;

long long int tidyNum(unsigned long long num) {
    long long int result = 0;
    string numStr = to_string(num);
    bool hasEqual = false;
    int j = 0;
    for (int i = 0; i != numStr.size(); ++i) {
        if (i > 0 && numStr[i - 1] < numStr[i]) continue;
        else if (i > 0 && numStr[i - 1] == numStr[i]) {
            if (numStr[i - 1] != numStr[j]) j = i - 1;
            hasEqual = true;
        } else if (i > 0 && numStr[i - 1] > numStr[i]) {
            if (hasEqual) {
                if (numStr[j] == numStr[i - 1]) {
                    numStr[j]--;
                    for (int k = j + 1; k != numStr.size(); ++k) numStr[k] = '9';
                    break;
                } else {
                    numStr[i-1]--;
                    for (int k = i; k != numStr.size(); ++k) numStr[k] = '9';
                    break;
                }
            } else {
                numStr[i - 1]--;
                for (int j = i; j != numStr.size(); ++j) numStr[j] = '9';
                break;
            }
        } else continue;
    }

    return stoull(numStr);
}

int main() {
    int T, id = 1;
    unsigned long long num;
    cin >> T;
    while (T--) {
        cout << "Case #" << id << ": ";
        cin >> num;
        id++;
        cout << tidyNum(num) << endl;
    }

    return 0;
}