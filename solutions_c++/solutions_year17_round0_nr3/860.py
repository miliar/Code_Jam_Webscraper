/**

**/
#include <bits/stdc++.h>
using namespace std;

#define N 200005
#define maxN 1000000007
#define PI 3.14159265358979
#define bb __builtin_popcount
#define ll long long
long long n, test, m;
void solve() {
    cin >> test;
    for (int te = 1; te <= test; te++) {
        cin >> n >> m;
        //double k = log2(m);
        //long long p = ceil(k) + 1;
        //for (int i = 1; i <= p - 1; i++)  n = (n + 1) / 2;
        while (m > 1) {
            if (m % 2 == 1) n = (n - 1) / 2;
            else n = n / 2;
            m = m / 2;
        }
        long long mi = (n - 1) / 2, ma = (n - 1) / 2 + ((n - 1) % 2);
        cout << "Case #" << te << ": " << ma << " " << mi << endl;
        //cout << n << endl;
    }
}
int main() {
    freopen("large.in", "r", stdin);
    //freopen("main.in", "w", stdout);
    freopen("main.txt", "w", stdout);
    solve();
    //fclose(stdin);
    //fclose(stdout);
}
///CTKB1997
