#include <stdio.h>
#include <vector>
#include <queue>

static const double alot = 1e15;

double visit(const std::vector<std::vector<long long>>& graph, long long endurance, long long speed, int start, const std::vector<double>& times) {
    std::priority_queue<std::pair<long long, int>> q;
    q.emplace(0, start);
    double best = alot;
    std::vector<bool> visited(graph.size(), false);
    while (!q.empty()) {
        auto info = q.top(); q.pop();
        if (visited[info.second]) continue;
        visited[info.second] = true;
        if (-info.first > endurance) break;
        double attempt = -info.first/((double)speed) + times[info.second];
        if (best > attempt) best = attempt;
        for (unsigned i=0; i<visited.size(); i++) {
            if (graph[info.second][i] == -1) continue;
            long long newdist = info.first - graph[info.second][i];
            q.emplace(newdist, i);
        }
    }
    return best;
}

void solve() {
    int N, Q;
    scanf("%d%d", &N, &Q);
    std::vector<long long> endurance(N);
    std::vector<long long> speed(N);
    std::vector<std::vector<long long>> graph(N);
    for (int i=0; i<N; i++) {
        scanf("%lld%lld", &endurance[i], &speed[i]);
        graph[i].resize(N);
    }
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            scanf("%lld", &graph[i][j]);
        }
    }
    std::vector<double> answer(Q);
    std::vector<int> from(Q);
    std::vector<int> to(Q);
    for (int i=0; i<Q; i++) {
        scanf("%d%d", &from[i], &to[i]);
        from[i] -= 1;
        to[i] -= 1;
    }
    #pragma omp parallel for
    for (int i=0; i<Q; i++) {
        std::vector<double> times(N, alot);
        times[to[i]] = 0;
        bool something_changed = true;
        while (something_changed) {
            something_changed = false;
            for (int i=0; i<N; i++) {
                std::vector<bool> visited(N, false);
                visited[i] = true;
                double attempt = visit(graph, endurance[i], speed[i], i, times);
                if (attempt < times[i]) {
                    times[i] = attempt;
                    something_changed = true;
                }
            }
        }
        answer[i] = times[from[i]];
    }
    for (int i=0; i<Q; i++)
        printf("%lf ", answer[i]);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i=0; i<T; i++) {
        printf("Case #%d: ", i+1);
        solve();
        printf("\n");
    }
}
