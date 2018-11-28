#include <iostream>
#include <cstring>
using namespace std;

typedef long long ll;

long long pow10[18];
long long pow11[18];

void go() {
    long long n;
    cin >> n;
    long long cur = 0;
    for (int i = 17; i >= 0; i--) {
        for (int j = 9; j >= 1; j--) {
            if (cur + pow11[i] * j <= n) {
                cur += pow10[i] * j;
                break;
            }
        }
    }
    cout << cur;
}
int main() {
    int testn;
    cin >> testn;
    pow11[0] = 1;
    pow10[0] = 1;
    for (int i = 1; i < 18; i++) {
        pow10[i] = pow10[i-1] * 10;
        pow11[i] = pow10[i] + pow11[i-1];
    }
    for (int testi = 0; testi < testn; testi++) {
        cout << "Case #" << testi+1 << ": ";
        go();
        cout << '\n';
    }
}
