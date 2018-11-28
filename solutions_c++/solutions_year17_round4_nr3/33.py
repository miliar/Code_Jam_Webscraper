#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

bool safe(const vector<vector<char>>& grid, int x, int y, int dx, int dy)
{
    if (x < 0 || x >= (int)grid.size() || y < 0 || y >= (int)grid[0].size())
    {
        return true;
    }

    if (grid[x][y] == '-' || grid[x][y] == '|')
    {
        return false;
    }

    if (grid[x][y] == '#')
    {
        return true;
    }

    if (grid[x][y] == '.')
    {
        return safe(grid, x + dx, y + dy, dx, dy);
    }
    
    if (grid[x][y] == '/')
    {
        return safe(grid, x - dy, y - dx, -dy, -dx);
    }

    if (grid[x][y] == '\\')
    {
        return safe(grid, x + dy, y + dx, dy, dx);
    }

    throw "invalid input";
}

void fill(const vector<vector<char>>& grid, int x, int y, int dx, int dy, vector<vector<vector<int>>>& ids, int id)
{
    if (x < 0 || x >= (int)grid.size() || y < 0 || y >= (int)grid[0].size())
    {
        return;
    }

    if (grid[x][y] == '#')
    {
        return;
    }

    if (grid[x][y] == '.')
    {
        ids[x][y].push_back(id);
        fill(grid, x + dx, y + dy, dx, dy, ids, id);
        return;
    }
    
    if (grid[x][y] == '/')
    {
        fill(grid, x - dy, y - dx, -dy, -dx, ids, id);
        return;
    }

    if (grid[x][y] == '\\')
    {
        fill(grid, x + dy, y + dx, dy, dx, ids, id);
        return;
    }

    throw "invalid input";
}

void visit(const vector<vector<int>>& edges, vector<bool>& u, vector<int>& l, int i)
{
    if (u[i])
    {
        return;
    }
    u[i] = true;
    for (int j : edges[i ^ 1])
    {
        visit(edges, u, l, j ^ 1);
    }
    l.push_back(i);
}

bool assign(const vector<vector<int>>& edges, vector<int>& d, int i)
{
    if (d[i] == 0)
        return false;
    if (d[i] == 1)
        return true;
    d[i] = 1;
    d[i ^ 1] = 0;
    for (int j : edges[i])
    {
        if (!assign(edges, d, j))
        {
            return false;
        }
    }
    return true;
}

int main()
{
    int T;

    cin >> T;
    for (int ct = 0; ct < T; ++ct)
    {
        int n, m;
        cin >> n >> m;
        vector<vector<char>> grid(n, vector<char>(m, '.'));
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                char c;
                cin >> c;
                grid[i][j] = c;
            }
        }

        vector<pair<int,int>> pos;
        vector<vector<vector<int>>> ids(n, vector<vector<int>>(m, vector<int>()));
        vector<vector<int>> edges;
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                if (grid[i][j] == '-' || grid[i][j] == '|')
                {
                    int id = pos.size();
                    pos.push_back(make_pair(i, j));
                    edges.push_back(vector<int>());
                    edges.push_back(vector<int>());
                    bool horizontal_safe = safe(grid, i, j-1, 0, -1) && safe(grid, i, j+1, 0, 1);
                    bool vertical_safe = safe(grid, i-1, j, -1, 0) && safe(grid, i+1, j, 1, 0);

                    if (horizontal_safe)
                    {
                        fill(grid, i, j-1, 0, -1, ids, id * 2);
                        fill(grid, i, j+1, 0, 1, ids, id * 2);
                    }
                    else
                    {
                        edges[id * 2].push_back(id * 2 + 1);
                    }

                    if (vertical_safe)
                    {
                        fill(grid, i-1, j, -1, 0, ids, id * 2 + 1);
                        fill(grid, i+1, j, 1, 0, ids, id * 2 + 1);
                    }
                    else
                    {
                        edges[id * 2 + 1].push_back(id * 2);
                    }
                }
            }
        }
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                if (grid[i][j] == '.')
                {
                    assert(ids[i][j].size() <= 2);
                    if (ids[i][j].size() == 0)
                    {
                        goto impossible;
                    }
                    if (ids[i][j].size() == 1)
                    {
                        int id = ids[i][j][0];
                        edges[id ^ 1].push_back(id);
                    }
                    else
                    {
                        int id1 = ids[i][j][0];
                        int id2 = ids[i][j][1];
                        edges[id1 ^ 1].push_back(id2);
                        edges[id2 ^ 1].push_back(id1);
                    }
                }
            }
        }
        {
            // Kosaraju's algorithm
            vector<bool> u(edges.size(), false);
            vector<int> l;
            for (size_t i = 0; i < edges.size(); ++i)
            {
                visit(edges, u, l, i);
            }
            vector<int> decision(edges.size(), -1);
            if (l.size() > 0)
            {
                for (size_t idx = 0; idx < l.size(); idx ++)
                {
                    size_t i = l[l.size() - 1 - idx];
                    if (decision[i] == -1)
                    {
                        if (!assign(edges, decision, i))
                        {
                            goto impossible;
                        }
                    }
                }
            }

            for (size_t i = 0; i < pos.size(); ++i)
            {
                if (decision[i * 2] == 1)
                {
                    grid[pos[i].first][pos[i].second] = '-';
                }
                else
                {
                    grid[pos[i].first][pos[i].second] = '|';
                }
            }

            cout << "Case #" << (ct + 1) << ": POSSIBLE" << endl;
            for (int i = 0; i < n; ++i)
            {
                for (int j = 0; j < m; ++j)
                {
                    cout << grid[i][j];
                }
                cout << endl;
            }

            continue;
        }
impossible:
        cout << "Case #" << (ct + 1) << ": IMPOSSIBLE" << endl;
    }

    return 0;
}
