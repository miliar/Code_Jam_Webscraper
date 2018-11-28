#include <iostream>
#include <string>
#include <vector>

using namespace std;

void doit() {
    long long N, n2;
    cin >> N;
    vector<long long> num;

    n2 = N;
    while (n2) {
        num.push_back(n2 % 10);
        n2 /= 10;
    }

    if (N == 0) {
        cout << 0 << endl;
        return;
    }

    int firstl = 0;
    int largest = 0;
    for (int i = num.size() - 1; i >= 0; --i) {
        if (num[i] > largest) {
            largest = num[i];
            firstl = i;
        }
        else if (num[i] != largest) {
            num[firstl] -= 1;
            for (int j = firstl - 1; j >= 0; --j) {
                num[j] = 9;
            }
            break;
        }
    }

/*
    int smallest = num[0];
    for (int i = 0; i < num.size(); ++i) {
//        cout << i << ' ' << num[i] << ' ' << smallest << endl;
        if (num[i] > smallest) {
            for (int j = 0; j < i; j++) {
                num[j] = 9;
            }
            num[i] -= 1;
            smallest = num[i];
        }
    }
*/
    bool have_non_zero = false;
    for (int i = num.size() - 1; i >= 0; --i) {
        if (have_non_zero || num[i] != 0) {
            cout << num[i];
            have_non_zero = true;
        }
    }
    cout << endl;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        doit();
    }
    return 0;
}
