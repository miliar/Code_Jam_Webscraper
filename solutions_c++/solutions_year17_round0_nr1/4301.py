#include <iostream>
#include <string>
#include <vector>

using namespace std;

int test_flipper(string& s, int flipper) {
    int result = 0;
    for (int i = 0; i < s.size() - flipper + 1; ++i) {
        if (s[i] == '-') {
            for (int j = i; j < i + flipper; ++j) {
                s[j] = s[j] == '-' ? '+' : '-';
            }
            ++result;
        }
    }
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == '-')
            return -1;
    }
    return result;
}


int main(int argc, char* argv[]) {
    int test_num = 0;
    cin >> test_num;
    for (int i = 0; i < test_num; ++i) {
        string str;
        int flipper = 0;
        cin >> str >> flipper;
        cout << "Case #" << i + 1 << ": ";
        auto res = test_flipper(str, flipper);
        if (res == -1)
            cout << "IMPOSSIBLE";
        else
            cout << res;
        cout << endl;
    }
    return 0;
}
