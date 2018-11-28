#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

string getValid(string input) {
    string result = "";
    int start = 0;
    while (start < input.length() && input[start] == '0') {
        start++;
    }

    for (int i = start; i < input.length(); i++) {
        result += input[i];
    }

    return result;
}


int main() {
	// your code goes here
	int tc;
	cin >> tc;
	for (int i = 0; i < tc; i++) {
        long long num, tmp, mul;
        int curPos, ninePos;
        cin >> num;
        tmp = num;
        curPos = 1;
        ninePos = -1;
        while (tmp > 0) {
            if (tmp % 10 < (tmp % 100) / 10) {
                int decrease = 10;
                tmp -= decrease;
                ninePos = curPos;
            }
            tmp /= 10;
            curPos++;
        }

        if (ninePos == -1) {
            cout << "Case #" << i + 1 << ": " << num << endl;
        } else {
            string result = "";
            while (num > 0) {
                if (ninePos > 0) {
                    result += "9";
                    ninePos--;
                } else {
                    if (ninePos == 0) {
                        result += num % 10 + 48 - 1;
                        ninePos--;
                    } else {
                        result += num % 10 + 48;
                    }
                }
                num /= 10;
            }

            reverse(result.begin(), result.end());
            cout << "Case #" << i + 1 << ": " << getValid(result) << endl;
        }
	}
}
