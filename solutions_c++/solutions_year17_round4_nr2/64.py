#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

pair<bool, int> go_check(const vector<int> &V, int bins) {
    int cost = 0;
    int empty = 0;
    for (int i = 1; i < int(V.size()); ++i) {
        if (V[i] > empty + bins)
            return make_pair(false, 0);
        int v = min(V[i], bins);
        cost += V[i] - v;
        empty -= V[i] - v;
        empty += bins - v;
    }
    return make_pair(true, cost);
}

int main() {
    ios::sync_with_stdio(false);

    int T; cin >> T;
    for (int test = 1; test <= T; ++test) {
        int N, C, M; cin >> N >> C >> M;
        vector<int> places(N + 1, 0), people(C + 1, 0);
        for (int i = 0; i < M; ++i) {
            int p, b; cin >> p >> b;
            places[p]++;
            people[b]++;
        }

        int step, answer;
        for (answer = 0, step = 1024; step; step >>= 1) {
            if (!go_check(places, answer + step).first)
                answer += step;
        }
        ++answer;

        answer = max(answer, *max_element(people.begin(), people.end()));
        cout << "Case #" << test << ": " << answer << " " << go_check(places, answer).second << "\n";
    }
}
