#include <bits/stdc++.h>

using namespace std;

bool check(string& s) {
    for (int i = 0; i + 1 < s.size(); i++) {
        if (s[i] > s[i + 1]) return false;
    }
    return true;
}

string solve() {
    string input;
    cin >> input;

    if (check(input)) return input;
    
    int i = 0, s = 0;
    while (input[i] <= input[i + 1]) {
        if (input[i] != input[i + 1]) {
            s = i + 1;
        }
        i++;
    }

    input[s] = char(input[s] - 1);
    for (int i = s + 1; i < input.size(); i++)
        input[i] = '9';

    if (input[0] == '0') input = input.substr(1, input.size() - 1);

    return input;
}

int main() {
    int n;
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        printf("Case #%d: ", i + 1);
        cout << solve() << endl;
    }

    return 0;
}