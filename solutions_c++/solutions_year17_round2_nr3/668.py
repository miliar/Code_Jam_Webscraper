#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

vector<double> test_case() {
    int N, Q; cin >> N >> Q;

    vector< pair<int, int> > horses(N);
    for (int i = 0; i < N; ++i)
        cin >> horses[i].first >> horses[i].second;

    vector< vector<int64_t> > dist(N, vector<int64_t>(N));
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            cin >> dist[i][j];

    for (int k = 0; k < N; ++k)
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                if (dist[i][k] != -1 && dist[k][j] != -1 && i != j) {
                    if (dist[i][j] == -1)
                        dist[i][j] = dist[i][k] + dist[k][j];
                    else if (dist[i][j] > dist[i][k] + dist[k][j])
                        dist[i][j] = dist[i][k] + dist[k][j];
                }
    vector< vector<double> > horse_dist(N, vector<double>(N, 1e40));
    for (int i = 0; i < N; ++i)
        horse_dist[i][i] = 0;

    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            if (dist[i][j] != -1 && horses[i].first >= dist[i][j])
                horse_dist[i][j] = double(dist[i][j]) / double(horses[i].second);

    for (int k = 0; k < N; ++k)
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                horse_dist[i][j] = min(horse_dist[i][j], horse_dist[i][k] + horse_dist[k][j]);

    vector<double> answer;
    while (Q--) {
        int from; int to; cin >> from >> to;
        --from; --to;

        answer.push_back(horse_dist[from][to]);
    }
    return answer;
}

int main() {
    int T; cin >> T;
    for (int test = 1; test <= T; ++test) {
        auto answer = test_case();
        cout << "Case #" << test << ": ";
        for (auto &x : answer) {
            cout.setf(ios::fixed, ios::floatfield);
            cout.precision(9);
            cout << x << " ";
        }
        cout << "\n";
    }
}
