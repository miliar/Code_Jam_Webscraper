#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

typedef pair<int, char> pic;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        pic a[] = {pic(r, 'R'), pic(y, 'Y'), pic(b, 'B')};
        sort(a, a + 3);
        int x0 = a[0].first;
        int x1 = a[1].first;
        int x2 = a[2].first;
        cout << "Case #" << t << ": ";
        if (x2 > x0 + x1) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            vector<char> v(n, '@');
            int i = 0;
            int c = 0;
            while (true) {
                v[i] = a[2].second;
                c++;
                if (c == x2) break;
                i += 2;
            }
            int stop = i;
            bool b = true;
            for (i = i + 1; i < n; i++) {
                if (b) {
                    v[i] = a[1].second;
                    x1--;
                } else {
                    v[i] = a[0].second;
                    x0--;
                }
                b = !b;
            }
            if (x0 < 0 || x1 < 0) {
                cout << "IMPOSSIBLE" << endl;
            } else {
                for (int j = 1; j < stop; j += 2) {
                    if (x1 > 0) {
                        v[j] = a[1].second;
                        x1--;
                    } else {
                        v[j] = a[0].second;
                    }
                }
                for (int j = 0; j < n; j++) {
                    cout << v[j];
                }
                cout << endl;
            }
        }
    }
    
    return 0;
}