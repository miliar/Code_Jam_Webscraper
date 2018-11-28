#include "stdafx.h"
#include "Qual_B.h"

bool IsTidy(long long n) {
    int last = 9;
    while (n) {
        if (n % 10 > last)
            return false;
        last = n % 10;
        n /= 10;
    }
    return true;
}

void Qual_B::Solve() {
    long long n, ans, factor;
    cin >> n;
    ans = 0;
    factor = 1;
    while (n) {
        if (IsTidy(n)) {
            ans = n * factor + ans;
            break;
        }
        ans += 9 * factor;
        factor *= 10;
        n /= 10;
        n--;
    }
    cout << ans << endl;
}

Qual_B::Qual_B()
{
}


Qual_B::~Qual_B()
{
}

