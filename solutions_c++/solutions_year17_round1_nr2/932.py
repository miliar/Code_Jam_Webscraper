#include <algorithm>
#include <fstream>
#include <iostream>
#include <cmath>
#include <set>

using namespace std;

int main()
{
    ifstream cin("B-small-attempt0.in");
    ofstream out("output.txt");
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int n, p;
        int weight[51];
        multiset < pair <int, int> > ingr[51];
        cin >> n >> p;
        for (int i = 1; i <= n; ++i) {
            cin >> weight[i];
        }
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= p; ++j) {
                int left, right;
                double package;
                cin >> package;

                left = int( package / weight[i] / 1.1);
                right = int( package / weight[i] / 0.9);

                left = max(left - 5, 1);
                right = right + 5;

                for (int k = 1; k <= 20; ++k) {
                    if (0.9 * weight[i] * left <= package && 1.1 * weight[i] * left >= package) {
                        break;
                    } else {
                        left++;
                    }
                }

                for (int k = 1; k <= 20; ++k) {
                    if (0.9 * weight[i] * right <= package && 1.1 * weight[i] * right >= package) {
                        break;
                    } else {
                        right--;
                    }
                }

                if (left <= right) {
                    ingr[i].insert(make_pair(left, right));
                }
                /*if (test == 5) {
                    cout << left << right << endl;
                    cout << package << endl;
                }*/
            }
        }
        int ans = 0;
        while (true) {
            bool mark = true;
            for (int i = 1; i <= n; ++i) {
                if (ingr[i].size() == 0) {
                    mark = false;
                    break;
                }
            }
            if (!mark) {
                break;
            }
            int left = 1, right = 1000 * 1000;
            int index = 0, minValue = 1000 * 1000 + 1;
            for (int i = 1; i <= n; ++i) {
                pair <int, int> ok = *ingr[i].begin();
                if (ok.first >= left) {
                    left = ok.first;
                }
                if (ok.second <= right) {
                    right = ok.second;
                }
                if (ok.first <= minValue) {
                    index = i;
                    minValue = ok.first;
                }
            }
            if (left <= right) {
                ans++;
                for (int i = 1; i <= n; ++i) {
                    ingr[i].erase(ingr[i].begin());
                }
            } else {
                ingr[index].erase(ingr[index].begin());
            };
        }
        out << "Case #" << test << ": " << ans << endl;
    }
    return 0;
}