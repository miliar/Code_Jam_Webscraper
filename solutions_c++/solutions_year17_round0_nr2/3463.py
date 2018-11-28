#include <bits/stdc++.h>

using namespace std;

int main() {
//    freopen("B-large.in", "r", stdin);
//    freopen("B-large.out", "w", stdout);
    int t;
    string input;
    scanf("%d", &t);
    for (int tc = 1; tc <= t; tc++) {
        cin >> input;
        int inputSize = (int) input.size();
        int maxIndex = 0, maxValue = input[0] - '0';
        bool flag = false;
        for (int i = 1; i < inputSize; i++) {
            int charValue = input[i] - '0';
            if (charValue > maxValue) {
                maxValue = charValue;
                maxIndex = i;
            } else if(charValue < maxValue) {
                flag = true;
                break;
            }
        }
        if (flag) {
            if (maxIndex == 0 && input[0] - '0' == 1) {
                input = input.substr(1);
                maxIndex--;
                inputSize--;
            } else {
                input[maxIndex] = (char) (input[maxIndex] - 1);
            }
            for (int i = maxIndex + 1; i < inputSize; i++) {
                input[i] = '9';
            }
        }
        cout << "Case #" << tc << ": " << input << endl;
    }
    return 0;
}
