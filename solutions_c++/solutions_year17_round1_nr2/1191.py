#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <memory>
#include <utility>

using namespace std;

bool test(int req, int n, int x) {
    return (req * n * 0.9 <= x) && (req * n * 1.1 >= x);
}

int main() {
    int t;
    cin >> t;
    for(int ts = 1; ts <= t; ++ts) {
        cout << "Case #" << ts << ": ";

        int N, R;
        cin >> N >> R;
        vector<int> reqs(N);
        vector<vector<int>> packages(N);
        vector<vector<pair<int,int>>> poss(N);
        vector<vector<bool>> taken(N-1);
        for(int i = 0; i < N; ++i) {
            cin >> reqs[i];
            packages[i] = vector<int>(R);
            poss[i] = vector<pair<int, int>>(R);
            if(i < N-1) taken[i] = vector<bool>(R);
        }
        for(int i = 0; i < N; ++i) {
            auto &v = packages[i];
            for(int j = 0; j < R; ++j) {
                cin >> v[j];
            }
            sort(v.begin(), v.end());
        }

        int counter = 0;

        for(int i = 0; i < N; ++i) {
            for(int j = 0; j < R; ++j) {
                int x = packages[i][j];
                int req = reqs[i];
                int temp = x / req;
                int min = -1, max = -1;
                if(test(req, temp - 1, x)) {
                    min = max = temp - 1;
                } else if(test(req, temp + 1, x)) {
                    min = max = temp + 1;
                } else if(test(req, temp, x)) {
                    min = max = temp;
                }

                // expand
                while(test(req, --min, x)) {}
                ++min;
                while(test(req, ++max, x)) {}
                --max;
                poss[i][j] = pair<int, int>(min, max);
            }
        }

        // for(int i = 0; i < N; ++i) {
        //     for(int j = 0; j < R; ++j) {
        //         auto p = poss[i][j];
        //         cout << p.first << ' ' << p.second << endl;
        //     }
        //     cout << endl;
        // }

        for(int i = 0; i < R; ++i) {
            auto p = poss[0][i];
            int min = p.first;
            int max = p.second;
            vector<int> taken2;
            if(min != -1) {
                bool failed = false;
                for(int i2 = 1; i2 < N; ++i2) {
                    failed = true;
                    for(int j = 0; j < R; ++j) {
                        if(taken[i2-1][j]) continue;
                        auto p2 = poss[i2][j];
                        int min2 = p2.first;
                        int max2 = p2.second;
                        if(min <= min2 && min2 <= max) {
                            min = min > min2 ? min : min2;
                            failed = false;
                            taken[i2-1][j] = true;
                        }
                        if(min <= max2 && max2 <= max) {
                            max = max < max2 ? max : max2;
                            failed = false;
                            taken[i2-1][j] = true;
                        }
                        if(taken[i2-1][j]) {
                            taken2.emplace_back(j);
                            break;
                        }
                    }
                }
                // cout << min << ' ' << max << endl;
                if(!failed) ++counter;
                else {
                    for(int i2 = 0; i2 < taken2.size(); ++i2) {
                        taken[i2][taken2[i2]] = false;
                    }
                }
            }
        }

        cout << counter << endl;
    }
}
