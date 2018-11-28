#include <bits/stdc++.h>

using namespace std;
int cases = 1;

int main(void) {
    freopen("/home/vanessi/CLionProjects/CodeJam2017QA/A-large.in", "r", stdin);
    freopen("/home/vanessi/CLionProjects/CodeJam2017QA/A-large.out", "w", stdout);
    int testcases;
    scanf("%d", &testcases);
    while (testcases--) {
        string input;
        int k;
        cin >> (input) >> k;
        int number = 0;
        bool never = false;
        for (int i = 0; i < input.size(); ++i) {
            if(input[i] == '-'){
                if (input.size() - i >= k) {
                    for (int j = i; j < i + k; ++j) {
                        if (input[j] == '-')input[j] = '+';
                        else input[j] = '-';
                    }
                    number++;
                } else if (input[i] == '-') {
                    never = true;
                    break;
                }
            }
        }
        if (never)cout << "Case #" << cases++ << ": " << "IMPOSSIBLE" << "\n";
        else cout << "Case #" << cases++ << ": " << number << "\n";
    }
}