#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

pair<int, int> calc(const int quantity, const int req) {
        int mins {2000000}, maxs {0};
        for (int i {1}; i <= 1000000; ++i) {
                double t {static_cast<double>(req) * i};
                if (t * 0.9 <= quantity && quantity <= t * 1.1) {
                        mins = min(mins, i);
                        maxs = max(maxs, i);
                }
        }
        return {mins, maxs};
}

int main() {
        size_t casenum;
        cin >> casenum;
        for (size_t caseid {1}; caseid <= casenum; ++caseid) {
                int N, P;
                cin >> N >> P;
                vector<int> req(N);
                for (int i {0}; i < N; ++i)
                        cin >> req[i];
                vector<vector<pair<int, int>>> q(N);
                for (int i {0}; i < N; ++i) {
                        for (int j {0}; j < P; ++j) {
                                int quantity;
                                cin >> quantity;
                                auto p = calc(quantity, req[i]);
                                if (p.second > 0)
                                        q[i].push_back(p);
                        }
                }
                vector<pair<int, pair<int, int>>> vec;
                for (int i {0}; i < N; ++i) {
                        for (const auto& p : q[i]) {
                                vec.push_back({p.first, {0, i}});
                                vec.push_back({p.second, {1, i}});
                        }
                }
                sort(begin(vec), end(vec));
                // for (const auto& p : vec)
                //         cerr << p.first << '\t' << p.second.first << '\t' << p.second.second << '\n';
                vector<int> cnt(N, 0);
                vector<int> buf(N, 0);
                int ans {0};
                for (const auto& p : vec) {
                        if (p.second.first == 0) {
                                cnt[p.second.second] += 1;
                        } else {
                                if (buf[p.second.second] > 0) {
                                        buf[p.second.second] -= 1;
                                        continue;
                                }
                                bool flag {true};
                                for (int i {0}; i < N; ++i) {
                                        if (cnt[i] == 0) {
                                                flag = false;
                                                break;
                                        }
                                }
                                if (flag) {
                                        ans += 1;
                                        for (int i {0}; i < N; ++i) {
                                                if (i == p.second.second) continue;
                                                buf[i] += 1;
                                                cnt[i] -= 1;
                                        }
                                        // cerr << "xxx " << p.first << '\t' << p.second.first << '\t' << p.second.second << '\n';
                                }
                                cnt[p.second.second] -= 1;
                        }
                }
                cout << "Case #" << caseid << ": ";
                cout << ans;
                cout << endl;
        }
        return 0;
}