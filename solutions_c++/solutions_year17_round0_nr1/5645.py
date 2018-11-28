#include <iostream>
#include <string>
using namespace std;

int t;
string s;
int k;
int answer[1000];

bool check_s() {
    string sequence(s.size(), '+');
    for (int i = 0; i < s.size() - k + 1; i++) {
        if (answer[i]) {
            for (int j = 0; j < k; j++) {
                if (sequence[i + j] == '+') {
                    sequence[i + j] = '-';
                }
                else {
                    sequence[i + j] = '+';
                }
            }
        }
    }
    return s == sequence;
}

bool dfs(int i) {
    if (i > s.size() - k) return check_s();
    answer[i] = 0;
    if (dfs(i + 1)) {
        return true;
    }
    else {
        answer[i] = 1;
        return dfs(i + 1);
    }
}

void main() {
    cin >> t;
    for (int i = 0; i < t; i++){
        cin >> s >> k;
        if (dfs(0)) {
            int counter = 0;
            for (int j = 0; j < s.size() - k +1; j++) {
                if (answer[j]) {
                    counter++;
                }
            }
            cout << "Case #" << (i + 1) << ": " << counter << endl;
        }
        else
        {
            cout << "Case #" << (i + 1) << ": IMPOSSIBLE" << endl;
        }
    }
}