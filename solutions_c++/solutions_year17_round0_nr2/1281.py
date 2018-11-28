#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#define rep(i, n) for (int i = 0; i < (n); i++)
#define rrep(i, n) for (int i = (n)-1; i >= 0; i--)
using namespace std;
using lli = long long int;
bool isd(lli n)
{
    lli pre = 9;
    while (n > 0) {
        lli a = n % 10;
        if (pre < a)
            return false;
        pre = a;
        n /= 10;
    }
    return true;
}
void solve(lli n, int l)
{

    lli ans = 0;
    int cnt = 0;
    if (isd(n)) {
        ans = n;
        cout << "Case #" << l << ": " << ans << endl;
        return;
    }
    while (n) {
        lli a = pow(10, cnt + 1);
        lli b = a - 1;
        lli c = pow(10, cnt);
        while (n % a != b) {
            n -= c;
            if (isd(n)) {
                ans = n;
                cout << "Case #" << l << ": " << ans << endl;
                return;
            }
        }
        if (isd(n)) {
            ans = n;
            cout << "Case #" << l << ": " << ans << endl;
            return;
        }
        cnt++;
    }
}
int main()
{
    lli t;
    cin >> t;
    lli n;
    rep(i, t)
    {
        cin >> n;
        solve(n, i + 1);
    }
}
