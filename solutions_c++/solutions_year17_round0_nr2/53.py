//
// Created by XelaPi.
//
#include <iostream>

using namespace std;

bool isTidy(unsigned long long n) {

    int lastDigit = 10;

    while (n > 0) {
        int digit = n % 10;

        if (digit > lastDigit) {
            return false;
        }

        lastDigit = digit;

        n /= 10;
    }

    return true;
}

int main() {

    int num;

    cin >> num;

    for (int i = 0; i < num; i++) {
        cout << "Case #" << (i + 1) << ": ";

        unsigned long long N;

        cin >> N;

        string length = to_string(N);
        string allOnes = "";

        for (int k = 0; k < length.length(); ++k) {
            allOnes.append("1");
        }

        unsigned long long start = strtoull(allOnes.c_str(), nullptr, 10);

        if (N < start) {
            for (int j = 0; j < length.length() - 1; ++j) {
                cout << "9";
            }

            cout << endl;
            continue;
        }

        unsigned long long last = N;
        unsigned long long place = 1;

        while (!isTidy(last)) {
            unsigned long long numberToRemove = (last % (place * 10)) / place;
            numberToRemove *= place;

            last -= numberToRemove;
            last += 9 * place;

            place *= 10;

            while (last > N) {
                last -= place;
            }
        }

        cout << last << endl;
    }

    return 0;
}