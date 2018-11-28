#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N, R, O, Y, G, B, V;
vector<char> arr;
int main() {
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> N >> R >> O >> Y >> G >> B >> V;
        arr.clear();
        cout << "Case #" << t << ": ";
        char a='R', b = 'Y', c = 'B';
        pair<int, char> p[3];
        p[0].first = R; p[0].second = 'R';
        p[1].first = Y; p[1].second = 'Y';
        p[2].first = B; p[2].second = 'B';
        sort(p, p+3);
        if (p[0].first + p[1].first < p[2].first) cout << "IMPOSSIBLE" << endl;
        else {
            int t1 = p[0].first;
            for (int i = 0; i < t1; i++) {
                for (int j = 0; j < 3; j++) {
                    arr.push_back(p[j].second);
                    p[j].first--;
                }
            }
            int t2 = p[1].first;
            for (int i = 0; i < t2; i++) {
                for (int j=1; j < 3; j++) {
                    arr.push_back(p[j].second);
                    p[j].first--;
                }
            }
            int t3 = p[2].first;
            for (int i = 0; i < t3; i++) {
                int len = arr.size();
                for (int j = 0; j < len; j++) {
                    if (arr[j] != p[2].second && arr[j+1] != p[2].second) {
                        if (j == len-1)
                            if (arr[len-1] != p[2].second && arr[0] != p[2].second) {
                                arr.push_back(p[2].second);
                                p[2].first--;
                                break;
                            }
                        arr.insert(arr.begin()+j+1, p[2].second);
                        p[2].first--;
                        break;
                    }
                }
            }
            for (int i = 0; i < arr.size(); i++)
                cout << arr[i];
            cout << endl;

        }
    }
    return 0;
}
