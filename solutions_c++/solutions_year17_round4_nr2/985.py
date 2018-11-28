#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<int, int> pii;

void sub() {
    int n, c, m;
    cin >> n >> c >> m;
    vector<int> as(n + 1);
    vector<int> bs(n + 1);
    int aa = 0, bb = 0;
    for (int i = 0; i < m; i++) {
        int pos, num;
        cin >> pos >> num;
        pos--;
        if (num == 1)
            as[pos]++;
        else
            bs[pos]++;
        if (num == 1)
            aa++;
        else
            bb++;
    }

    if (aa < bb)
        as[n] += bb - aa;
    else
        bs[n] += aa - bb;
    aa = max(aa, bb);
    bb = max(aa, bb);

    int x = aa, y = 0;
    for (int i = 0; i < n; i++) {
        // non-i
        int ii = as[i];
        int noni = aa - bs[i];
        if (i == 0)
            x += max(0, ii - noni);
        else
            y += max(0, ii - noni);
    }

    cout << x << " " << y << endl;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        sub();
    }
}
