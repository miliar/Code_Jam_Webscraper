#include <bits/stdc++.h>

using namespace std;

const int INF = 10000;

int n, m, k;

string number;


int main()
{
    int tests;
    freopen("B-large.in", "r", stdin);
    freopen("B-largeOUT.txt","w", stdout );
    scanf("%d", &tests);
    for (int i = 1; i <= tests; i++) {
        cin >> number;
        vector<int> tidyNumber;
        bool finished = false;
        while (!finished) {
            bool flag = false;
            for (int i = 0; i < number.length() - 1; i++) {
                if (flag) {
                    number[i] = '9';
                }
                else if (number[i] > number[i + 1]) {
                    int curDigit = number[i] - '0';
                    number[i] = '0' + curDigit - 1;
                    number[i + 1] = '9';
                    flag = true;
                }

            }
            if (flag) number[number.length() - 1] = '9';
            else finished = true;
        }
        cout << "Case #" << i << ": ";
        for (int i = 0; i < number.length(); i++) {
            if (!(i == 0 && number[i] == '0')) {
                printf("%c", number[i]);
            }
        }
        cout << endl;
    }
    return 0;
}
