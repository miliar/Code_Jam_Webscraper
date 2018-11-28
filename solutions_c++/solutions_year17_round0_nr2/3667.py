#include <iostream>
#include <deque>
#include <string>

using namespace std;

// Highest is 0, lowest is size -1
void lastTidyNumber(deque<int> &num) {
    int size = num.size();
    if (size <= 1) 
        return;
    for (int i = size - 1; i > 0; i--) {
        if (num[i - 1] > num[i]) {
            num[i - 1] -= 1;
            for (int j = i; j < size; j++) {
                num[j] = 9;
            }
        }
    }
    if (num[0] == 0)
        num.pop_front();
}


int main() {
    int tests;
    string N;
    cin >> tests;
    for (int i = 0 ; i < tests; i++) {
        cin >> N;
        deque<int> num;
        for (char c : N) {
            num.push_back(c - '0');
        }
        lastTidyNumber(num);

        cout << "Case #" << (i + 1) << ": ";
        for (int n : num) {
            cout << n;
        }
        cout << endl;
    }
}