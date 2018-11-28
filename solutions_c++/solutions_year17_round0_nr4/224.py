#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

struct bipartite
{
    int l, r;
    vector<vector<int>> edges;
    vector<bool> matched;
    vector<int> matches;
    vector<bool> forced;

    bipartite(int l, int r) : l(l), r(r), matched(l, false), matches(r, -1), forced(r, false)
    {
    }

    void force_match(int x, int y)
    {
        assert(!matched[x]);
        matched[x] = true;
        matches[y] = x;
        forced[y] = true;
    }

    bool try_augment(int x, vector<bool>& visited)
    {
        if (visited[x])
        {
            return false;
        }
        visited[x] = true;
        for (auto y : edges[x])
        {
            if (matches[y] == -1)
            {
                matches[y] = x;
                matched[x] = true;
                return true;
            }
        }
        for (auto y : edges[x])
        {
            if (!forced[y] && try_augment(matches[y], visited))
            {
                matches[y] = x;
                matched[x] = true;
                return true;
            }
        }
        return false;
    }

    void match()
    {
        for (int i = 0; i < l; ++i)
        {
            if (!matched[i])
            {
                auto tmp = vector<bool>(l, false);
                try_augment(i, tmp);
            }
        }
    }

    int count()
    {
        int ret = 0;

        for (int i = 0; i < r; ++i)
        {
            ret += matches[i] != -1;
        }
        return ret;
    }
};

int main()
{
    int T;

    cin >> T;
    for (int cs = 0; cs < T; ++cs)
    {
        int n, k;
        cin >> n >> k;

        // row and column graph
        bipartite axes(n, n);
        for (int i = 0; i < n; ++i)
        {
            axes.edges.push_back(vector<int>());
            for (int j = 0; j < n; ++j)
            {
                axes.edges[i].push_back(j);
            }
        }

        // diaggonals graph
        bipartite diag(n * 2 - 1, n * 2 - 1);
        for (int i = 0; i < n * 2 - 1; ++i)
        {
            diag.edges.push_back(vector<int>());
            for (int j = 0; j < n * 2 - 1; ++j)
            {
                if ((i + j + n) % 2 == 1 && std::abs(i - (n - 1)) + std::abs(j - (n - 1)) < n)
                {
                    diag.edges[i].push_back(j);
                }
            }
        }

        // game board
        vector<vector<char>> board(n, vector<char>(n, '.'));
        for (int i = 0; i < k; ++i)
        {
            char c;
            int x, y;
            cin >> c >> x >> y;
            x --;
            y --;
            if (c != '+')
            {
                axes.force_match(x, y);
            }
            if (c != 'x')
            {
                diag.force_match(x + y, y - x + (n - 1));
            }
            board[x][y] = c;
        }

        // optimize
        axes.match();
        diag.match();

        // draw new board
        vector<vector<char>> new_board(n, vector<char>(n, '.'));
        for (int i = 0; i < axes.r; ++i)
        {
            if (axes.matches[i] != -1)
            {
                int x = axes.matches[i];
                int y = i;
                new_board[x][y] = 'x';
            }
        }
        for (int i = 0; i < diag.r; ++i)
        {
            if (diag.matches[i] != -1)
            {
                int x = (diag.matches[i] + (n - 1) - i) / 2;
                int y = (diag.matches[i] - (n - 1) + i) / 2;
                if (new_board[x][y] == '.')
                {
                    new_board[x][y] = '+';
                }
                else
                {
                    new_board[x][y] = 'o';
                }
            }
        }

        struct ans_t
        {
            char c;
            int x, y;
        };
        vector<ans_t> answers;
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                if (board[i][j] != new_board[i][j])
                {
                    answers.push_back(ans_t{new_board[i][j], i, j});
                }
            }
        }

        cout << "Case #" << (cs + 1) << ": " << axes.count() + diag.count() << " " << answers.size() << endl;
        for (const auto& answer : answers)
        {
            cout << answer.c << " " << (answer.x + 1) << " " << (answer.y + 1) << endl;
        }
    }
    return 0;
}
