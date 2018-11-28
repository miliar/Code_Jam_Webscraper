#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
typedef long long ll;

ll N;
int x[20];

void solve()
{
    int digit = 0;
    for (int i = 0; i < 19; i++) {
        x[i] = N % 10;
        N /= 10;
        if (x[i]) digit = i;
    }

    for (int i = 0; i < digit; i++) {
        if (x[i + 1] > x[i]) {
            x[i + 1]--;
            for (int j = 0; j <= i; j++) {
                x[j] = 9;
            }
        }
    }

    if (x[digit]) cout << x[digit];
    for (int i = digit - 1; i >= 0; i--) {
        cout << x[i];
    }
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N;
        cout << "Case #" << i + 1 << ": ";
        solve();
        cout << endl;
    }
}
