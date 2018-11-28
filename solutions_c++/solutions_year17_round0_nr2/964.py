#include <cstdlib>
#include <cstring>

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

void fix(std::string& input) {
    bool flag = false;
    for (int i = 0; i < input.size() - 1; i ++) {
        if (input[i] > input[i + 1]) {
            flag = true;
            input[i] -= 1;
            for (int j = i + 1; j < input.size(); j++) {
                input[j] = '9';
            }
        }
    }
    if (flag) fix(input);
}

void work() {
    std::string input;
    cin >> input;
    if (input.size() == 1) {
        cout << input << endl;
        return;
    }
    fix(input);
    if (input[0] == '0') {
        cout << input.substr(1) << endl;
    }
    else {
        cout << input << endl;
    }
}

int main() {
    int tot; cin >> tot;
    for (int cas = 1; cas <= tot; cas ++) {
        cout << "Case #" << cas << ":";
        cout << " ";
        work();
    }
    return 0;
}
