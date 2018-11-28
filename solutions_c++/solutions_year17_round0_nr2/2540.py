#include <iostream>
#include <string>

using namespace std;

// returns 0 if num is tidy
int get_untidy_pos(const string &num) {
    for (int i = 1; i < (int)num.size(); ++i) {
        if (num[i] < num[i - 1]) {
            return i;
        }
    }
    return 0;
}

int main() {
    int number_of_cases;
    cin >> number_of_cases;
    for (int test_case = 0; test_case < number_of_cases; ++test_case) {
        string num;
        cin >> num;
        int index = get_untidy_pos(num);
        if (index != 0) {
            --index;
            while (index && num[index - 1] == num[index]) {
                --index;
            }
            if (num[index] == 0) {
                --index;
            }
            num[index]--;
            for (index++; index < (int)num.size(); ++index) {
                num[index] = '9';
            }
            int start = 0;
            while (num[start] == '0' && start < -1 + (int)num.size()) {
                ++start;
            }
            num = num.substr(start);
        }
        cout << "Case #" << test_case + 1 << ": ";
        cout << num;
        cout << endl;
    }
    return 0;
}
