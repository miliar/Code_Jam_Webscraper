#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    
    void problemA() {
        int case_number = 0;
        cin >> case_number;
        for (int i = 0; i < case_number;i++) {
            string temp;
            cin >> temp;
            int val = 0;
            cin >> val;
            int flip_number = 0;
            for (int j = 0; j <= temp.size() - val; j++) {
                if (temp[j] == '-') {
                    temp[j] = '+';
                    int k = 1;
                    while (k < val) {
                        if (temp[j + k] == '+') {
                            temp[j + k] = '-';
                        }
                        else {
                            temp[j + k] = '+';
                        }
                        k++;
                    }
                    flip_number++;
                }
            }
            bool is_possible = true;
            for (int j = temp.size() - val + 1; j < temp.size();j++) {
                if (temp[j] == '-') {
                    cout << "Case #"<<i+1<<": IMPOSSIBLE" << endl;
                    is_possible = false;
                    break;
                }
            }
            if (is_possible) {
                cout << "Case #"<<i+1<<": "<<flip_number << endl;
            }
            
            
        }
    }
    
public:
    void problemB() {
        int case_number = 0;
        cin >> case_number;
        for (int i = 0; i < case_number;i++) {
            long long number;
            cin >> number;
            string s_number = to_string(number);
            for (int i = 0; i < s_number.size();i++) {
                for (int j = i + 1; j < s_number.size();j++) {
                    if (s_number[i] > s_number[j]) {
                        s_number[i] --;
                        for (int k = j; k < s_number.size();k++) {
                            s_number[k] = '9';
                        }
                    }
                }
            }
            cout << s_number << endl;
            
        }

    }
};

int main() {
    Solution a;
    a.problemA();
    return 0;
}
