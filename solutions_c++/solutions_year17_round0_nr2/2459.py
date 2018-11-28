#include <bits/stdc++.h>

using namespace std;

int n;
string s;
int a[19];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        printf("Case #%d: ", tt);
        cin >> s;
        n = s.length();
        for (int i = 1; i <= n; i++) a[i] = int(s[i - 1]) - 48;
        //for (int i = 1; i <= n; i++) cout << a[i];
        //cout << endl;
        s = "";
        int pivot = n + 1;
        int remain = 0;
        for (int i = n; i; i--) {
            a[i] -= remain;
            if (a[i] < a[i - 1]) {
                remain = 1;
                pivot = i;
            } else remain = 0;
        }
        for (int i = pivot; i <= n; i++) a[i] = 9;
        for (pivot = 1; pivot <= n; pivot++)
            if (a[pivot] != 0) break;
        for (int i = pivot; i <= n; i++) s += char(a[i] + 48);
        cout << s << endl;
    }
}
