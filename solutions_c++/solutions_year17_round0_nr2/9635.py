#include <iostream>
#include <string>

using namespace std;

inline bool checkTidy(int num) {
    string s = to_string(num);
    for (int i = 0; i < s.length() - 1; i++) {
        int first = s[i] - '0';
        int next = s[i + 1] - '0';
        if (first > next) {
            return false;   
        }
    }

    return true;
}

inline int getTidy(int num) {
    int result = num;

    while (result > 10) {
        if (checkTidy(result)) {
            return result;       
        } else {
            result -= 1;
        }
    }

    return result;
}

int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        int num; cin >> num;
        cout << "Case #" << i << ": " << getTidy(num) << endl;
    }

    return 0;
}
