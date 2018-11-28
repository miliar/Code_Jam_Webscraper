#include <bits/stdc++.h>

using namespace std;

int t, n, p;

int r[55];
vector<int> q[55];

int main() {
    cin >> t;
    for (int test = 1; test <= t; test++) {
        cin >> n >> p;
        for (int i = 0; i < n; i++) {
            cin >> r[i];
        }
        for (int i = 0; i < n; i++) {
            q[i].clear();
            for (int j = 0; j < p; j++) {
                int tmp;
                cin >> tmp;
                q[i].push_back(tmp);
            }
            sort(q[i].begin(), q[i].end());
        }

        int kits = 0;
        for (int i = 0; i < p; i++) {

            int num = q[0][i] / r[0];


            while (true) {
                if (q[0][i] * 10 > num * r[0] * 11) {
                    num++;
                    break;
                }
                num--;
            }
            for (; num * r[0] * 9 <= q[0][i] * 10; num++) {
                // cout << num << endl;
                bool works = true;

                // cout << num << " " << q[0][i] << " " << r[0] << endl;

                int removed[55];
                memset(removed, 0, sizeof(removed));
                for (int j = 1; j < n; j++) {
                    for (int j2 = 0; j2 < q[j].size(); j2++) {
                        // cout << (num * r[j] * 9) << " " << (q[j][j2] * 10) << " " << (num * r[j] * 11) << " " << r[j] <<endl;
                        if (num * r[j] * 9 <= q[j][j2] * 10 && q[j][j2] * 10 <= num * r[j] * 11) {
                            // cout << j2 << " " << p << " " << q[j].size() << endl;
                            removed[j] = q[j][j2];
                            q[j].erase(q[j].begin() + j2);
                            break;
                        }
                    }

                    if (removed[j] == 0) {
                        works = false;
                        break;
                    }
                }

                if (!works) {
                    for (int j = 1; j < n; j++) {
                        if (removed[j] == 0) continue;
                        q[j].push_back(removed[j]);
                        sort(q[j].begin(), q[j].end());
                    }
                } else {
                    kits++;
                    break;
                }

            }
        }

        cout << "Case #" << test << ": " << kits << endl;

    }
}