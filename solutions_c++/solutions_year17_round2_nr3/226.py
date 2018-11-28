#include <bits/stdc++.h>
using namespace std;

template <typename T>
using Matrix = vector<vector<T>>;

template <typename T>
Matrix<T> matrix(const int R, const int C, const T x = T()) { return Matrix<T>(R, vector<T>(C, x)); }

void solve_case()
{
    int N, Q; cin >> N >> Q;

    struct Horse { int max_distance, speed; };
    auto horses = vector<Horse>(N);
    for (auto& h : horses) cin >> h.max_distance >> h.speed;

    auto distances = matrix<long long>(N, N);
    for (auto i = 0; i < N; i++)
    {
        for (auto& x : distances[i]) cin >> x;
        distances[i][i] = 0;
    }
    for (auto j = 0; j < N; j++)
        for (auto i = 0; i < N; i++) for (auto k = 0; k < N; k++)
            if (distances[i][j] != -1 && distances[j][k] != -1)
            {
                const auto option = distances[i][j] + distances[j][k];
                if (distances[i][k] == -1 || distances[i][k] > option)
                    distances[i][k] = option;
            }

    for (auto q = 0; q < Q; q++)
    {
        int start, end; cin >> start >> end;
        start--; end--;

        auto seen = vector<bool>(N);
        const auto infinity = numeric_limits<double>::infinity();
        auto fastest = vector<double>(N, infinity);
        fastest[start] = 0;
        for (auto i = 0; i < N; i++)
        {
            auto v = -1;
            for (auto w = 0; w < N; w++)
            {
                if (seen[w] || fastest[w] == infinity) continue;
                if (v == -1 || fastest[w] < fastest[v])
                    v = w;
            }
            if (v == -1 || fastest[v] == infinity) break;
            else seen[v] = true;

            for (auto w = 0; w < N; w++) if (distances[v][w] != -1 && distances[v][w] <= horses[v].max_distance)
            {
                const auto dt = double(distances[v][w]) / horses[v].speed;
                fastest[w] = min(fastest[w], fastest[v] + dt);
            }
        }
        cout << fastest[end] << " ";
    }
    cout << endl;
}

int main()
{
    cout << fixed << setprecision(9);

    int T; cin >> T;
    for (auto t = 1; t <= T; t++)
    {
        cout << "Case #" << t << ": ";
        solve_case();
    }
}
