


#include <iostream>

using namespace std;

int input(int *num)
{
    int i = 0;
    string s;
    cin >> s;

    for (i = 0; i <= (int)s.length(); i++) {
        num[i] = s[i] - '0';
    }
    return i - 1;
}

void printAll(int *num, int n)
{
    bool valuable = false;

    for (int i = 0; i < n; i++) {

        if (num[i] != 0) {
            valuable = true;
        }

        if (valuable) {
            cout << num[i];
        }
    }
    cout << endl;
}

void tidy(int *num, int n)
{
    for (int i = 0; i < n - 1; i++) {
        if (num[i] > num[i + 1]) {
            num[i] -= 1;

            for (int j = i + 1; j < n; j++) {
                num[j] = 9;
            }
        }
    }

    for (int i = n - 1; i > 0; i--) {
        if (num[i - 1] > num[i]) {
            num[i] = 9;
            num[i - 1] -= 1;
        }
    }
}


int main()
{
    int num[20];

    int n = 0;
    int t = 0;

    cin >> t;

    for (int i = 0; i < t; i++) {
        n = input(num);
        // printAll(num, n);
        tidy(num, n);
        cout << "Case #" << i + 1 << ": ";
        printAll(num, n);
    }

    return 0;
}