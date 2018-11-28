#include <bits/stdc++.h>
using namespace std;

int t;
string number;

int main (int argc, char** argv) {
    cin >> t;
    for (int cur = 1; cur <= t; cur++) {
        cin >> number;
        for (int i = number.size()-1; i > 0; i--) {
            if (number[i-1] <= number[i]) continue;
            number[i-1]--;
            for (int j = i; j < number.size(); j++) {
                number[j] = '9';
            }
        }
        while(number[0] == '0') {
            number.erase(0, 1);
        }
        cout << "Case #" << cur << ": " << number << endl;
    }
    return 0;
}