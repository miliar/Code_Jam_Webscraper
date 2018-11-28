#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iterator>
#include <utility>
#include <algorithm>
#include <list>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;

#define pb push_back
#define sz(v) ((long long)v.size())
#define mp make_pair
#define FOR(i,n) for(int i = 0;i < (n);++i)
#define MOD 1000000007

void solve() {
    //cerr << "#######################" << endl;
    int hd, ad, hk, ak, b, d;
    cin >> hd >> ad >> hk >> ak >> b >> d;
    ad = min(ad, hk);

    vector<vector<vector<int>>> state(hd + 1);
    FOR(i, hd + 1) {
        state[i] = vector<vector<int>>(hk + 1);
        FOR(j, hk + 1) {
            state[i][j] = vector<int>(ak + 1, 1000000000);
        }
    }
    state[hd][ad][ak] = hk;

    bool inf = true;
    FOR(i_step, 210) {
        vector<vector<vector<int>>> new_state(state);

        try {
            FOR(i, hd + 1) {
                FOR(j, hk + 1) {
                    FOR(k, ak + 1) {
                        new_state[i][j][k] = min(new_state[i][j][k], state[i][j][k] - j);
                        if (new_state[i][j][k] <= 0) {
                            throw 0;
                        }
                    }
                }
            }
            FOR(i, hd + 1) {
                FOR(j, hk + 1) {
                    FOR(k, ak + 1) {
                        int new_j = min(hk, j + b);
                        new_state[i][new_j][k] = min(new_state[i][new_j][k], state[i][j][k]);
                    }
                }
            }
            FOR(i, hd + 1) {
                FOR(j, hk + 1) {
                    FOR(k, ak + 1) {
                        new_state[hd][j][k] = min(new_state[hd][j][k], state[i][j][k]);
                    }
                }
            }
            FOR(i, hd + 1) {
                FOR(j, hk + 1) {
                    FOR(k, ak + 1) {
                        int new_k = max(0, k - d);
                        new_state[i][j][new_k] = min(new_state[i][j][new_k], state[i][j][k]);
                    }
                }
            }
            FOR(i, hd + 1) {
                FOR(j, hk + 1) {
                    FOR(k, ak + 1) {
                        if (k) {
                            int new_i = max(0, i - k);
                            new_state[new_i][j][k] = new_state[i][j][k];
                            new_state[i][j][k] = 1000000000;
                        }
                    }
                }
            }
            FOR(j, hk + 1) {
                FOR(k, ak + 1) {
                    if (k) {
                        new_state[0][j][k] = 1000000000;
                    }
                }
            }

            // FOR(i, hd) {
            //     FOR(j, hk) {
            //         FOR(k, ak) {
            //             cerr << i << " " << j << " " << k << " " << new_state[i][j][k] << endl;
            //         }
            //     }
            // }
            // break;
        } catch (...) {
            inf = false;
            cout << i_step + 1 << endl;
            break;
        }

        state = new_state;
    }
    if (inf) {
        cout << "IMPOSSIBLE" << endl;
    }
}

int main() {
    int T;
    cin >> T;
    FOR(iter, T) {
        cout << "Case #" << iter + 1 << ": ";
        solve();
    }
}