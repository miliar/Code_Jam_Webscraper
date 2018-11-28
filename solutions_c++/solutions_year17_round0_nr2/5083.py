/*

Problem B. Tidy Numbers

Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest, her pencils are sorted from shortest to longest and her computers from oldest to newest. One day, when practicing her counting skills, she noticed that some integers, when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order. Some examples of this are 8, 123, 555, and 224488. She decided to call these numbers tidy. Numbers that do not have this property, like 20, 321, 495 and 999990, are not tidy.

She just finished counting all positive integers in ascending order from 1 to N. What was the last tidy number she counted?

Input

The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with a single integer N, the last number counted by Tatiana.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the last tidy number counted by Tatiana.

Limits

1 <= T <= 100.
Small dataset

1 <= N <= 1000.
Large dataset

1 <= N <= 10^18.

Sample

Input 

4
132
1000
7
111111111111111110

Output 

Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999

*/

#include <iostream>

using namespace std;

bool existsZero(string num) {
    for (char n : num) {
        if (n == '0') {
            return true;
        }
    }
    return false;
}

string getNines(string num) {
    string toReturn;
    for (int i=1; i<num.size(); ++i) {
        toReturn += '9';
    }
    return toReturn;
}

string getLargestTidyNumberWithNoZeroes(string num) {
    // Fix self + -1 and start over
    for (int i = num.size() - 1; i > 0; --i) {
        // Out of order
        if (num[i-1] > num[i]) {
            int j;
            for (int k = i-1; ; --k) {
                if (num[k] > '0') {
                    num[k] = num[k] - 1;
                    j = k + 1;
                    break;
                }
                cout << "stuck" << endl;
            }
            for (; j<num.size(); ++j) {
                num[j] = '9';
            }
            i = num.size();
        }
    }
    return num;
}

string getLargestTidyNumber(string num) {
    string largest = getLargestTidyNumberWithNoZeroes(num);
    for (char n : largest) {
        if (n == '0') {
            return getNines(largest);
        }
        return largest;
    }
}

int main() {
    string num;
    int T;
    cin >> T;
    for (int i=1; i<=T; ++i) {
        cin >> num;
        cout << "Case #" << i << ": " << getLargestTidyNumber(num) << endl;
    }
}

