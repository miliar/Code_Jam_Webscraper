#include <bits/stdc++.h>

using namespace std;
int cases = 1;

int main(void) {
    freopen("/home/vanessi/CLionProjects/CodeJam2017QB/B-large.in", "r", stdin);
    freopen("/home/vanessi/CLionProjects/CodeJam2017QB/B-large.out", "w", stdout);
    int testcases;
    scanf("%d", &testcases);
    while (testcases--) {
        string number;
        cin >> (number);
        bool bug = false;
        for (int i = int(number.size()) - 1; i > 0; --i) {
            if (number[i] < number[i - 1]) {
                for (int j = i; j < number.size(); ++j) {
                    number[j] = '9';
                }
                number[i - 1]--;
            }
        }
        if (number[0] == '0') {
            number = number.substr(1);
        }
        cout << "Case #" << cases++ << ": " << number << "\n";
    }
}