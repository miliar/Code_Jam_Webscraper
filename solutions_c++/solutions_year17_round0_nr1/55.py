//
// Created by XelaPi.
//
#include <iostream>

using namespace std;

int main() {

    int num;

    cin >> num;

    for (int i = 0; i < num; i++) {
        cout << "Case #" << (i + 1) << ": ";

        string p;

        cin >> p;

        int s;

        cin >> s;

        int num = 0;

        for (int j = 0; j <= p.length() - s; ++j) {
            if (p[j] == '-') {
                for (int k = 0; k < s; ++k) {
                    if (p[j + k] == '-') {
                        p[j + k] = '+';
                    } else {
                        p[j + k] = '-';
                    }
                }

                num++;
            }
        }

        bool valid = true;

        for (int j = p.length() - s; j < p.length(); ++j) {
            if (p[j] == '-') {
                valid = false;
                break;
            }
        }

        if (valid) {
            cout << num;
        } else {
            cout << "IMPOSSIBLE";
        }

        cout << endl;
    }

    return 0;
}