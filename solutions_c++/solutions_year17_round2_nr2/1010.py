#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <string>

#define f first
#define s second

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int u = 0; u < T; ++u) {
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        string res = "";
        if (r > y + b || y > r + b || b > r + y) {
            res = "IMPOSSIBLE";
        } else {
            string col = "RYB";
            while (r > 0 || y > 0 || b > 0) {
                if (r < y) {
                    swap(r, y);
                    swap(col[0], col[1]);
                }
                if (r < b) {
                    swap(r, b);
                    swap(col[0], col[2]);
                }
                if (y < b) {
                    swap(b, y);
                    swap(col[2], col[1]);
                }
                int pos = 0;
                if (res != "") {
                    if (col[0] == res[res.size() - 1]) {
                        pos = 1;
                    }
                }
                res += col[pos];
                if (pos == 0) {
                    r--;
                } else {
                    y--;
                }
            }
            if (res[res.size() - 1] == res[0]) {
                swap(res[res.size() - 1], res[res.size() - 2]);
            }
        }
        cout << "Case #" << u + 1 << ": " << res << "\n";
    }
    return 0;
}
