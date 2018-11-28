#include <iostream>
#include <vector>
using namespace std;

int n;
int R, O, Y, G, B, V;

int main() {
    int T, Case = 1;
    cin >> T;
    while (T--) {
        cin >> n;
        cin >> R >> O >> Y >> G >> B >> V;
        // R, Y, B
        vector<pair<int, char> > vec{{R, 'R'}, {Y, 'Y'}, {B, 'B'}};
        sort(vec.begin(), vec.end());
        string ans;
        if (vec.back().first * 2 > n) ans = "IMPOSSIBLE";
        else {
            int m = vec.back().first;
            for (int i = 0; i < m; i++) {
                ans += vec.back().second;
                if (i < vec[0].first) ans += vec[0].second;
                if (vec[1].first >= m - i) ans += vec[1].second;
            }
        }
        cout << "Case #" << Case++ << ": " << ans << endl;
    }
    return 0;
}
