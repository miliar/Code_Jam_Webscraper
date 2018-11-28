#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <iomanip>

using namespace std;

int main() {
    int T;
    int n,p;
    vector<int> v;
    int ans;
    cin >> T;
    for (int cs = 1; cs <= T; cs++) {
        cin >> n >> p;
        v.clear();
        v.resize(p);
        ans = 0;
        for (int i = 0; i < n; i++) {
            int temp;
            cin >> temp;
            v[temp % p]++;
        }
        ans = v[0];
        if (p == 2) {
            ans += (v[1] + 1) / 2;
        } else if (p == 3) {
            int k = min(v[1], v[2]);
            ans += k;
            v[1] -= k;
            v[2] -= k;
            ans += (v[1] + (p - 1)) / p;
            ans += (v[2] + (p - 1)) / p;
        } else if (p == 4) {
            ans += v[2] / 2;
            v[2] %= 2;
            int k = min(v[1], v[3]);
            ans += k;
            v[1] -= k; v[3] -= k;
            if (v[1] > 0) {
                ans += v[1] / 4;
                v[1] %= 4;
                if (v[1] == 3 && v[2] == 1) {
                    ans += 2;
                } else {
                    ans += 1;
                }
            } else if (v[3] > 0) {
                ans += v[3] /4;
                v[3] %= 4;
                if (v[3] == 3 && v[2] == 1) 
                    ans += 2;
                else if (v[3] > 0)
                    ans += 1;
            } else { // v[1] = v[3] = 0
                ans += v[2];
            }
        }
        cout << "Case #" << cs << ": " << ans << endl;
        cerr << "Case #" << cs << endl;
    }
}