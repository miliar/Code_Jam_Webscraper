#include <algorithm>
#include <iostream>
#include <vector>
#include <set>

using namespace std;

typedef pair<int, int> pii;

int main(void) {

    int test_num;
    cin >> test_num;

    for (int Case = 1 ; Case <= test_num ; ++Case) {

        int n, p;
        cin >> n >> p;

        vector<int> R(n);
        for (int& val : R) {
            cin >> val;
        }

        vector< vector<int> > detail(n, vector<int>(p));
        vector< vector<pii> > data(n, vector<pii>(p));
        for (int i = 0 ; i < n ; ++i) {
            for (int j = 0 ; j < p ; ++j) {
                cin >> detail[i][j];
            }
            sort(detail[i].begin(), detail[i].end());
        }

        vector<int> S;
        for (int i = 0 ; i < n ; ++i) {
            for (int j = 0 ; j < p ; ++j) {
                int a = (10 * detail[i][j] + (11*R[i]-1)) / (11*R[i]);
                int b = (10 * detail[i][j]) / (9*R[i]);
                data[i][j] = {a, b};
                S.push_back(a);
            }
        }

        sort(S.begin(), S.end());

        int ans = 0;
        for (int s : S) {
            int cnt = 0;
            for (int i = 0 ; i < n ; ++i) {
                for (int j = 0 ; j < p  ; ++j) {
                    if (data[i][j].first <= s and s <= data[i][j].second) {
                        ++cnt;
                        break;
                    }
                }
            }
            if (cnt >= n) {
                ++ans;
                for (int i = 0 ; i < n ; ++i) {
                    for (int j = 0 ; j < p ; ++j) {
                        if (data[i][j].first <= s and s <= data[i][j].second) {
                            data[i][j] = {-1, -1};
                            break;
                        }
                    }
                }
            }
        }

        cout << "Case #" << Case << ": " << ans << endl;
        cerr << Case << endl;
    }

    return 0;
}
