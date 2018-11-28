#include <bits/stdc++.h>
using namespace std;

struct BipartiteGraph
{
    int L, R;
    vector<vector<int>> adjacency_list;
    vector<int> match;

    BipartiteGraph(const int L, const int R) : L(L), R(R), adjacency_list(L), match(R, -1) {}

    void add_edge(const int l, const int r) { adjacency_list[l].push_back(r); }

    int max_matching()
    {
        auto seen = vector<bool>(L);
        const function<bool(int)> find_path = [&](const int l)
        {
            if (seen[l]) return false;
            else seen[l] = true;

            for (const auto r : adjacency_list[l])
            {
                if (match[r] == -1 || find_path(match[r]))
                {
                    match[r] = l;
                    return true;
                }
            }
            return false;
        };

        auto result = 0;
        for (auto l = 0; l < L; l++)
        {
            fill(begin(seen), end(seen), false);
            if (find_path(l)) result++;
        }
        return result;
    }
};

void solve_case()
{
    int N, M; cin >> N >> M;

    auto baseline = 0;
    auto initial_grid = vector<vector<char>>(N, vector<char>(N, '.'));
    for (auto i = 0; i < M; i++)
    {
        char c; int row, column; cin >> c >> row >> column;
        row--; column--;
        initial_grid[row][column] = c;
        baseline += c == 'o' ? 2 : 1;
    }

    auto bad_row = vector<bool>(N), bad_column = vector<bool>(N);
    for (auto r = 0; r < N; r++) for (auto c = 0; c < N; c++)
        if (initial_grid[r][c] == 'x' || initial_grid[r][c] == 'o')
            bad_row[r] = bad_column[c] = true;

    auto axis_aligned = BipartiteGraph(N, N);
    for (auto r = 0; r < N; r++) for (auto c = 0; c < N; c++)
    {
        if (bad_row[r] || bad_column[c]) continue;
        if (initial_grid[r][c] == '.' || initial_grid[r][c] == '+')
            axis_aligned.add_edge(r, c);
    }
    const auto extra_xs = axis_aligned.max_matching();

    auto bad_diagonal = vector<bool>(2*N-1), bad_antidiagonal = vector<bool>(2*N-1);
    for (auto r = 0; r < N; r++) for (auto c = 0; c < N; c++)
        if (initial_grid[r][c] == '+' || initial_grid[r][c] == 'o')
            bad_diagonal[r+c] = bad_antidiagonal[r-c+(N-1)] = true;

    auto diagonals = BipartiteGraph(2*N-1, 2*N-1);
    for (auto r = 0; r < N; r++) for (auto c = 0; c < N; c++)
    {
        if (bad_diagonal[r+c] || bad_antidiagonal[r-c+(N-1)]) continue;
        if (initial_grid[r][c] == '.' || initial_grid[r][c] == 'x')
            diagonals.add_edge(r+c, r-c+(N-1));
    }
    const auto extra_crosses = diagonals.max_matching();

    auto final_grid = initial_grid;
    for (auto c = 0; c < N; c++)
    {
        const auto r = axis_aligned.match[c];
        if (r == -1) continue;
        final_grid[r][c] = final_grid[r][c] == '.' ? 'x' : 'o';
    }
    for (auto i = 0; i < 2*N-1; i++)
    {
        const auto d = diagonals.match[i];
        if (d == -1) continue;
        const auto a = i - (N-1);
        const auto r = (d+a)/2, c = (d-a)/2;
        final_grid[r][c] = final_grid[r][c] == '.' ? '+' : 'o';
    }

    struct Update { char c; int row, column; };
    auto updates = vector<Update>();
    for (auto r = 0; r < N; r++) for (auto c = 0; c < N; c++)
        if (initial_grid[r][c] != final_grid[r][c])
            updates.push_back({final_grid[r][c], r, c});

    cout << baseline + extra_xs + extra_crosses << " " << updates.size() << endl;
    for (const auto x : updates)
        cout << x.c << " " << x.row+1 << " " << x.column+1 << endl;
}

int main()
{
    int T; cin >> T;
    for (auto t = 1; t <= T; t++)
    {
        cout << "Case #" << t << ": ";
        solve_case();
    }
}
