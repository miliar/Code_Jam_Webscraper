#include <iostream>
#include <vector>
#include <string>

using namespace std;

string solve(string& number) {

    if (number.size() > 1) {

        int32_t index = 0;
        char n = number[0];
        bool tidy = true;
        bool backtrack = false;

        for (int32_t i = 0; i < number.size() - 1 && tidy; i++) {

            // not a tidy number ?
            if (number[i] > number[i + 1]) {
                tidy = false;
                if (!backtrack) {
                    index = i;
                }
            }
            else if (number[i] < number[i + 1]) {
                index = i;
                n = number[i];
                backtrack = false;
            }
            else {
                backtrack = true;
            }

        }

        if (tidy) {
            return number;
        }

        number[index]--;

        for (int32_t i = index + 1; i < number.size(); i++) {
            number[i] = '9';
        }
    }

    // strip leading zeros
    number.erase(0, min(number.find_first_not_of('0'), number.size()-1));

    return number;
}

int main() {

    int32_t t;

    cin >> t;

    for (int32_t test = 1; test <= t; ++test) {

        string number;
        string result;

        cin >> number;
        result = solve(number);

        cout << "Case #" << test << ": " << result << "\n";
    }

    return 0;
}