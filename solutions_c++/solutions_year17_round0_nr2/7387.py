#include <algorithm>
#include <fstream>
#include <vector>
#include <iostream>

using namespace std;

bool check(vector <int> &digits) {
    for (int i = 1; i < digits.size(); ++i) {
        if (digits[i] < digits[i - 1]) {
            return false;
        }
    }
    return true;
}

inline void print(int test, vector <int> &digits) {
    cout << "Case #" << test << ": ";
    for (int i = 0; i < digits.size(); ++i) {
        cout << digits[i] ;
    }
    cout << endl;
}

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        long long number;
        vector <int> digits;
        cin >> number;
        while (number > 0) {
            digits.push_back(number % 10);
            number /= 10;
        }
        reverse(digits.begin(), digits.end());
        if (check(digits)) {
            print(test, digits);
            continue;
        }
        int pos = 0;
        for (int i = 1; i < digits.size(); ++i) {
            if (digits[i - 1] > digits[i]) {
                pos = i - 1;
                break;
            }
        }
        vector <int> answer;
        while (pos > 0 && digits[pos] == digits[pos - 1]) {
            pos--;
        }
        if (pos == 0) {
            if (digits[0] == 1) {
                for (int i = 0; i < digits.size() - 1; ++i) {
                    answer.push_back(9);
                }
                print(test, answer);
            } else {
                answer.push_back(digits[0] - 1);
                for (int i = 0; i < digits.size() - 1; ++i) {
                    answer.push_back(9);
                }
                print(test, answer);
            }
        } else {
            digits[pos]--;
            for (int i = pos + 1; i < digits.size(); ++i) {
                digits[i] = 9;
            }
            print(test, digits);
        }
    }
    return 0;
}