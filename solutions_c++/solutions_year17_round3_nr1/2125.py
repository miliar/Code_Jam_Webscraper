#define _USE_MATH_DEFINES
#include <math.h>
#include <cstdio>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <sstream>
#include <list>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <limits>
#include <map>
#include <istream>


using namespace std;

double top(long long r) {
    return M_PI * r * r;
}

double sur(long long r, long long h) {
    return 2 * M_PI * r * h;
}

void bt(vector<pair<long long, long long>> &pan, double tmp,
        double &res, int K, int idx, int cnt) {
    if (cnt > K - 1) return;
    if (cnt == K - 1) {
        res = max(tmp, res);
    }

    for (int i = idx; i < pan.size(); ++i) {
        tmp += sur(pan[i].first, pan[i].second);
        bt(pan, tmp, res, K, i + 1, cnt + 1);
        tmp -= sur(pan[i].first, pan[i].second);
    }
}

int main(int argc, char **argv) {
    int n;
    /*
    int N;
    int R;
    int O;
    int Y;
    int G;
    int B;
    int V;
    string res;
    */

    int N;
    int K;
    long long R;
    long long H;
    double tmp = 0.0;
    double res = 0.0;

    auto comp = [](const pair<long long, long long>& p1, const pair<long long, long long>& p2) {
                    return p1.first > p2.first || (p1.first == p2.first &&
                                                   p1.second > p2.second);
                    };

    //res = last_word("CAB");
    //cout<< res<< endl;

    cin >> n;
    for (int i = 1; i <= n; ++i) {
        vector<pair<long long, long long>> pan;
        tmp = 0.0;
        res = 0.0;

        cin >> N >> K;

        for (int j = 0; j < N; ++j) {
            cin >> R >> H;
            pan.push_back({R, H});
        }

        sort(pan.begin(), pan.end(), comp);

        for (int j = 0; j <= N - K; ++j) {
            tmp = 0.0;
            long long r = pan[j].first;
            long long h = pan[j].second;
            bt(pan, 0, tmp, K, j + 1, 0);
            tmp += top(r);
            tmp += sur(r, h);

            res = max(tmp, res);
        }

        printf("Case #%d: %lf\r\n", i, res);

        /*
        cin >> N >> R >> O >> Y >> G >> B >> V;

        if (R > N / 2 || Y > N / 2 || B > N / 2) {
            printf("Case #%d: IMPOSSIBLE\r\n", i);
        }
        else {
            for (int i = 0; i < N;) {
                if (R > 0) {
                    res += 'R';
                    --R;
                    ++i;
                }
                if (Y > 0) {
                    res += 'Y';
                    --Y;
                    ++i;
                }
                if (B > 0) {
                    res += 'B';
                    --B;
                    ++i;
                }
            }
            cout << "Case #" << i << ": "<< res<< endl;
        }
        */
    }

    return 0;
}
