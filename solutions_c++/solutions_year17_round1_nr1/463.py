#include <bits/stdc++.h>

using namespace std;

#define vec vector
#define ALL(x) (x).begin(), (x).end()

typedef pair< int, int > pii;
typedef long long ll;

int const inf = 1000 * 1000 * 1000;
ll const inf64 = 1ll * inf * inf;

void solve() {
    int r, c;
    cin >> r >> c;
    vec< string > a(r);
    for(int i = 0;i < r;i++) {
        cin >> a[i];
    }
    for(int i = 0;i < r;i++) {
        if(count(ALL(a[i]), '?') == c) {
            if(i > 0) {
                a[i] = a[i - 1];
            }
        }else {
            for(int last = 0, j = 0;j < c;j++) {
                if(a[i][j] != '?') {
                    for(int q = last;q <= j;q++) {
                        a[i][q] = a[i][j];
                    }
                    last = j + 1;
                }
            }
            for(int j = 1;j < c;j++) {
                if(a[i][j] == '?') {
                    a[i][j] = a[i][j - 1];
                }
            }
        }
    }
    for(int i = r - 2;i >= 0;i--) {
        if(count(ALL(a[i]), '?') == c) {
            a[i] = a[i + 1];
        }
    }
    cout << "\n";
    for(int i = 0;i < r;i++) {
        cout << a[i] << "\n";
    }
}

int main() {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int testNumber;

    scanf("%d", &testNumber);

    for(int test = 1;test <= testNumber;test++) {
        printf("Case #%d: ", test);
        solve();
    }

    return 0;
}
