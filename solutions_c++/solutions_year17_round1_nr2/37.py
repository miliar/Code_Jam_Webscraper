#include <functional>
#include <iostream>
#include <deque>
#include <set>
#include <cstring>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <map>
#include <cmath>
#include <string>

using namespace std;

#define ll long long


int main() {
    int T;
    cin>>T;
    for (int t = 1; t <= T; ++t) {
        ll N, P;
        cin>>N>>P;
        ll R[50];
        ll Q[50][50];
        for (int i=0;i<N;++i) {
            cin>>R[i];
        }
        for (int i=0;i<N;++i) {
            for (int j=0;j<P;++j) {
                cin>>Q[i][j];
            }
            sort(Q[i], Q[i] + P);
        }

        int idx[50] = {0};
        ll srv = 1;
        bool done = false;
        int ans = 0;
        while (!done) {
            int numGood = 0;
            for (int i=0;i<N;++i) {
                int& id = idx[i];
                while (srv * R[i] * 9 > Q[i][id] * 10 && id < P) {
                    id++;
                }
                if (id >= P) {
                    done = true;
                    break;
                }
                if (srv * R[i] * 11 >= Q[i][id] * 10) {
                    numGood++;
                } else break;
            }
            if (done) break;

            if (numGood == N) {
                 ans++;
                 for (int i=0;i<N;++i) {
                    idx[i]++;
                    if (idx[i] >= P) {
                        done = true;
                        break;
                    }
                 }
            } else {
                srv++;
            }
        }

        printf("Case #%d: %d\n", t, ans);
    }
}

