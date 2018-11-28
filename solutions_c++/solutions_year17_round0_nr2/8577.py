#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>

using namespace std;

/*bool tidy(long long n)
{
    int i;
    long long n1 = n, temp;
    vector <long long> x;
    while (n1) { temp = n1 % 10; n1 /= 10; x.push_back(temp); }
    for (i = 1; i < x.size(); i++) {
        if (x[i] > x[i - 1]) { return false; break; }
    }
    return true;
}*/

long long lasttidy(long long n)
{
    bool tidy;
    int i, last_tidy;
    long long n1 = n, res, temp;
    vector <long long> x;
    while (n1) { temp = n1 % 10; n1 /= 10; x.push_back(temp); }

    tidy = true;
    for (i = 1; i < x.size(); i++) {
        if (x[i] > x[i - 1]) { tidy = false; break; }
    }
    if (tidy) return n;
    while (!tidy) {
        last_tidy = -1;
        for (i = x.size() - 1; i > 0; i--) {
            if ((x[i] > x[i - 1]) && (last_tidy == -1)) last_tidy = i;
        }
        x[last_tidy]--; for (i = 0; i < last_tidy; i++) x[i] = 9;
        tidy = true;
        for (i = 1; i < x.size(); i++) {
            if (x[i] > x[i - 1]) { tidy = false; break; }
        }
        if (tidy) {
            res = 0;
            for (i = x.size() - 1; i >= 0; i--) { res *= 10; res += x[i]; }
            return res;
        }
    }
}

int main()
{
    int x, i, len, t;
    long long n, y;
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    cin >> t;
    for (x = 1; x <= t; x++)
    {
        cin >> n;

        //y = n; while (!tidy(y)) y--;
        y = lasttidy(n);

        //display results
        cout << "Case #" << x << ": " << y << endl;
    }
    return 0;
}
