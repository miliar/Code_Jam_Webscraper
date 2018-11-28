#include <bits/stdc++.h>
using namespace std;
int n;
double d, K[1005], S[1005], maxx;
void solve(int Case) {
    cin >> d >> n;
    maxx = 0;
    for (int i = 0; i < n; i++) {
        cin >> K[i] >> S[i];
        maxx = max(maxx, (d-K[i])/S[i]);
    }

    cout << "Case #" << (Case+1) <<": ";
    printf("%lf\n", d/maxx);
}

int main () {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int i=0;i<T;i++) solve(i);
}
