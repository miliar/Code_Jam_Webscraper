#include <iostream>
using namespace std;

bool check(int x) {
    int prosli = 9;

    while (x) {
        int zadnji = x % 10;
        x /= 10;
        if (zadnji > prosli)
            return false;
        prosli = zadnji;
    }
    return true;
}


int main() {
    int t; cin >> t;
    int cnt = 0;

    while (t--) {
        cnt++;

        int n; cin >> n;
        while(!check(n)) n--;

        printf("Case #%d: %d\n", cnt, n);
    }

    return 0;
}
