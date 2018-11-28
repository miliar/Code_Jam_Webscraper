#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

string findTidy(string start) {
    if (start.length() == 1)
        return start;
    char last = start[0];
    for (int i = 1; i < (int)start.length(); ++i) {
        char current = start[i];
        if (current < last) {
            for (unsigned int j = i; j < start.length(); ++j) {
                start[j] = '9';
            }
            for (int j = (i - 1); j >= 0; --j) {
                start[j] = start[j] - 1;
                if (start[j - 1] > start[j])
                    start[j] = '9';
                else 
                    break;
            }
            for (unsigned int j = 0; j < start.size(); ++j) {
                if (start[j] == '0') continue;
                return start.substr(j);
            }
        }
        last = current;
    }
    return start;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        string temp;
        cin >> temp;
        cout << "Case #" << t << ": " << findTidy(temp) << endl;
    }

}
