#include <iostream>
#include <string>
#include <stdio.h>
#include <string.h>

using namespace std;

int main() {
    int cases;
    cin >> cases;
    for (int i = 1; i <= cases; i++) {
        string number;
        cin >> number;
        char num_array[number.length()];
        bool decrement[number.length()];
        memset(decrement, 0, sizeof(decrement));
        strncpy(num_array, number.c_str(), sizeof(num_array));
        for (long long j = sizeof(num_array) - 1; j > 0; j--) {
            if (num_array[j] < num_array[j-1]) {
                num_array[j] = '9';
                decrement[j-1] = true;
                num_array[j-1] = num_array[j-1] - 1;
            }
        }
        long long start = sizeof(num_array);
        bool start_string = false;
        for (long long j = 0; j < sizeof(num_array); j++)
        {
            if(decrement[j] == true) {
                start = j;
                break;
            }
        }
        cout << "Case #" << i << ": ";
        for (long long j = 0; j < sizeof(num_array); j++) {
            if (start_string == false) {
                if (num_array[j] > '0') {
                    start_string = true;
                }
            }
            if (j <= start && start_string) {
                cout << num_array[j];
            }
            else if(j > start && start_string)
                cout << '9';
        }
        cout << endl;
    }
}