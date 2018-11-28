#include <bits/stdc++.h>
#define loop(i, a, n) for(int i = a; i < n; i++)
#define cin in
#define cout out
#define row(x, n) (x + 2)
#define col(x, n) (x + n + 2)
#define unrow(x, n) (x - 2)
#define uncol(x, n) (x - n - 2)
using namespace std;

ifstream in("in.in");
ofstream out("out.txt");

typedef pair<int, int> p;
typedef vector<vector<int>> graph;
vector<vector<int>> ret;
vector<vector<int>> ret2;
vector<int> stackk, temp;
vector<bool> visit;

void prep()
{
    static int t = 1;
    cout << "Case #" << t++ << ": ";
}

void dfs(const graph& G, int v, int t)
{
    if (visit[v]) return;
    visit[v] = true;
    temp.push_back(v);
    if (v == t) stackk = temp;
    loop (i, 0, G.size()) if (G[v][i] == 1) dfs(G, i, t);
    temp.pop_back();
}

void max_flow(const graph& G, int s, int t)
{
    graph sh = G;

    stackk = vector<int>(0);
    visit = vector<bool>(sh.size(), false);
    dfs(sh, s, t);

    while (stackk.size() > 0)
    {
        loop(i, 0, stackk.size() - 1) sh[stackk[i]][stackk[i + 1]] = 0, sh[stackk[i + 1]][stackk[i]] = 1;
        stackk = vector<int>(0);
        visit = vector<bool>(G.size(), false);
        dfs(sh, s, t);
    }

    ret2 = vector<vector<int>>(G.size(), vector<int>(G.size(), 0));
    loop(i, 0, G.size()) loop(j, 0, G.size()) if (G[i][j] == 1 && sh[i][j] == 0) ret2[i][j] = 1;
}

void solve(const function<p(p)>& mapp, const function<p(p)>& unmapp, vector<vector<int>> temp)
{
    int n = 2 * temp.size();
    vector<vector<int>> arr(n, vector<int>(n, -1));
    vector<bool> used_row(n, false), used_col(n, false);
    loop(i, 0, temp.size()) loop(j, 0, temp.size()) arr[mapp(p(i, j)).first][mapp(p(i, j)).second] = temp[i][j];
    graph G(2 * n + 2, vector<int>(2 * n + 2, 0));
    loop(i, 0, n) loop(j, 0, n) if (arr[i][j] == 1) used_row[i] = used_col[j] = true; else if (arr[i][j] == 0) G[row(i, n)][col(j, n)] = 1;
    loop(i, 0, n)
    {
        if (!used_row[i]) G[0][row(i, n)] = 1;
        if (!used_col[i]) G[col(i, n)][1] = 1;
    }
    max_flow(G, 0, 1);
    loop(i, 0, n) loop(j, 0, n) if(arr[i][j] == 1) ret2[row(i, n)][col(j, n)] = 1;
    ret = vector<vector<int>>(temp.size(), vector<int>(temp.size(), 0));
    loop(i, 2, ret2.size()) loop(j, 2, ret2.size()) if (ret2[i][j] == 1) ret[unmapp(p(unrow(i, n), uncol(j, n))).first][unmapp(p(unrow(i, n), uncol(j, n))).second] = 1;
}

int add(int a, int b)
{
    if (a == '.') return b;
    if (b == '.') return a;
    return 'o';
}

int value(int c)
{
    if (c == 'o') return 2;
    if (c == '.') return 0;
    return 1;
}

void func()
{
    int n, m, count = 0, change = 0; cin >> n >> m;
    vector<vector<int>> orig, bish, rook, fin;
    orig = fin = vector<vector<int>>(n, vector<int>(n, '.'));
    bish = rook = vector<vector<int>>(n, vector<int>(n, 0));
    auto rook_map = [](p el) -> p
    {
        return el;
    };
    auto rook_unmap = [](p el) -> p
    {
        return el;
    };
    auto bish_map = [&n](p el) -> p
    {
        return p(el.first + el.second, el.first - el.second + n - 1);
    };
    auto bish_unmap = [&n](p el) -> p
    {
        return p((el.first + el.second + 1 - n) / 2, ((el.first - el.second) - 1 + n) / 2);
    };

    while (m--)
    {
        char c;
        int x, y; cin >> c >> x >> y; x--; y--;
        if (c == '+' || c == 'o') bish[x][y] = 1;
        if (c == 'x' || c == 'o') rook[x][y] = 1;
        orig[x][y] = c;
    }

    solve(rook_map, rook_unmap, rook);
    loop(i, 0, n) loop(j, 0, n) fin[i][j] = add(fin[i][j], ret[i][j] ? 'x' : '.');
    solve(bish_map, bish_unmap, bish);
    loop(i, 0, n) loop(j, 0, n) fin[i][j] = add(fin[i][j], ret[i][j] ? '+' : '.');
    loop(i, 0, n) loop(j, 0, n) count += value(fin[i][j]), change += (fin[i][j] != orig[i][j]);
    cout << count << " " << change << endl;
    loop(i, 0, n) loop(j, 0, n) if (fin[i][j] != orig[i][j]) cout << char(fin[i][j]) << " " << i + 1 << " " << j + 1 << endl;
}

int main()
{
    int t; cin >> t;
    while(t--) prep(), func();
    return 0;
}
