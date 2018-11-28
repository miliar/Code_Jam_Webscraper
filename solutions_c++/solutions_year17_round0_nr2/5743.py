#include <iostream>

using namespace std;
int main(){
    int testCases;
    cin >> testCases;
    for (int test = 0; test < testCases; ++test) {
        string number;
        cin >> number;
        bool changed = true;
        while (changed) {
            changed = false;
            for (int i = 0; i < number.size() - 1; ++i) {
                if (number[i] > number[i + 1]) {
                    changed = true;
                    number[i] = (char) (number[i] - 1);
                    for (int j = i + 1; j < number.size(); ++j) {
                        number[j] = '9';
                    }
                }
            }
            while (number[0]=='0')
                number.erase(number.begin());
        }
        cout << "Case #" << test+1 << ": " << number << endl;
    }
    return 0;
}