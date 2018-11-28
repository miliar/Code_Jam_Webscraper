#include<iostream>

using namespace std;

bool areSorted(int n)
{
    // Note that digits are traversed from last to first
    int next_digit = n % 10;
    n = n / 10;
    while (n)
    {
        int digit = n % 10;
        if (digit > next_digit)
            return false;
        next_digit = digit;
        n = n / 10;
    }

    return true;
}

int main() {
    int T,N,flag=0,temp;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": ";
        cin >> N;
        for (int j = N; j >= 1; j--) {
            if (areSorted(j)) {
                cout << j << endl;
                flag = 1;
                break;
            }
        }
    }
}