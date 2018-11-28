#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <iomanip>

using namespace std;

#define remove_duplicate(a) sort(a.begin(), a.end()); a.resize(distance(a.begin(), unique(a.begin(), a.end())));

typedef long long longint;


longint tt;
longint n;

void extract (longint n, vector<longint> &digit) {
    while (n) {
        digit.push_back(n % 10);
        n /= 10;
    }
}

void makeMinDigit (vector<longint> &digit, vector<longint> &minDigit) {
    minDigit.resize(digit.size());
    minDigit[0] = digit[0];
    for (longint i = 1; i < digit.size(); i++)
        minDigit[i] = min(minDigit[i - 1], digit[i]);

}

void write (vector<longint> &digit) { for (longint i = 0; i < digit.size(); i++) cerr << digit[i] << " "; cerr << endl;}

bool nonDecrease (longint x) {
    vector<int> digit;
    while(x) digit.push_back(x % 10), x /= 10;
    for (int i = 0; i < (int)digit.size() - 1; i++) {
        if (digit[i] < digit[i + 1]) return false;
    }
    return true;
}

longint get (longint x, longint n) {
    //cout << "do get " << x << " " << n << endl;
    while (x * 10 + 9 <= n) x = x * 10 + 9;
    if (not nonDecrease(x)) return -1;
    return x;
}

int main(){
    #define file "in"
    freopen(file".inp", "r", stdin); freopen(file".out", "w", stdout);
    scanf("%lld", &tt);
    for (longint qq = 1; qq <= tt; qq++) {
        scanf("%lld", &n);
        vector<longint> digit, minDigit;
        extract(n, digit);
        makeMinDigit(digit, minDigit);
        //write(digit);
        longint res = get(0, n), curr = 0;

        for (longint i = digit.size() - 1; i >= 0; i--) {
            res = max(res, get(curr * 10 + digit[i] - 1, n));
            curr = curr * 10 + digit[i];
        }
        res = max(res, get(curr, n));
        printf("Case #%lld: %lld\n", qq, res);
    }

    return 0;
}
