#include <iostream>

using namespace std;

void change(string& s, int start, int k) {
    for (int i = start; i < start + k; i++) {
        if (s[i] == '+') {
            s[i] = '-';
        }
        else {
            s[i] = '+';
        }
    }
}

void printResult(int nr, int result) {
    cout << "Case #" << nr << ": " << result << "\n";
}

void printResult(int nr, string result) {
    cout << "Case #" << nr << ": " << result << "\n";
}

int main() {
    ios_base::sync_with_stdio(0);

    int t, k;
    string s;
    cin >> t;

    int result = 0;

    bool isPossible;

    for (int i = 1; i <= t; i++) {
        cin >> s >> k;
        result = 0;
        isPossible = true;

        for (int j = 0; j <= s.size() - k; j++) {
            if (s[j] == '-') {
                change(s, j, k);
                result++;
            }
        }

        for (int j = 0; j < s.size(); j++) {
            if (s[j] == '-') {
                printResult(i, "IMPOSSIBLE");
                isPossible = false;
                break;
            }
        }

        if (isPossible) {
            printResult(i, result);
        }

    }

    return 0;
}