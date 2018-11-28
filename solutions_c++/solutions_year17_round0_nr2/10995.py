#include <iostream>
#include <vector>

using namespace std;

bool is_tidy(long num) {
    vector<int> digits;
    while (num != 0) {
        int rem = num % 10;
        num /= 10;
        digits.insert(digits.begin(), rem);
    }

    for (int i = 0; i < digits.size()-1; i++) {
        if (digits[i] > digits[i+1])
            return false;
    }

    return true;
}

int main() {
    int num_cases;
    cin >> num_cases;

    long input[num_cases];
    long tidy_input[num_cases];
    for (int i = 0; i < num_cases; i++) {
        cin >> input[i];
    }

    for (int i = 0; i < num_cases; i++) {
        bool found_tidy = false;
        while (!found_tidy) {
            if (is_tidy(input[i])) {
                tidy_input[i] = input[i];
                found_tidy = true;
            }
            input[i]--;
        }
    }

    for (int i = 0; i < num_cases; i++) {
        cout << "Case #" << i+1 << ": " << tidy_input[i] << endl;
    }
}
