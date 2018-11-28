/**

**/
#include <bits/stdc++.h>
using namespace std;

#define N 200005
#define maxN 1000000007
#define PI 3.14159265358979
#define bb __builtin_popcount
#define ll long long
long long n, test, a[100], m;
void solve() {
    cin >> test;
    for (int te = 1; te <= test; te++) {
        cin >> m;
        n = 0;
        while (m > 0) {
            a[n] = m % 10;
            n++;
            m /= 10;
        }
        for (int i = n - 2; i >= 0; i--)
            if (a[i] < a[i + 1]) {
                if (a[i + 1] != 0) {
                    a[i + 1]--;
                    for (int j = i; j >= 0; j--) a[j] = 9;
                    int j = i;
                    while (j + 2 < n) {
                        if (a[j + 1] < a[j + 2]) {
                            a[j + 2]--;
                            a[j + 1] = 9;
                            j++;
                        } else break;
                    }
                }
                break;
            }
        long long kq = 0;
        for (int i = n - 1; i >= 0; i--) kq = kq * 10 + a[i];
        cout << "Case #" << te << ": " << kq << endl;
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
