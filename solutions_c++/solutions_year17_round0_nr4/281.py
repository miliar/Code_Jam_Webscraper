#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;

class BiGraphMat
{
private:
    vector<int> xe[200];
    int mat[200],ux[200],uy[200],u[200];
    int n;

    int dfs(int r, int pv)
    {
        for (size_t i = 0; i < xe[r].size(); ++i)
            if (!u[xe[r][i]] && !uy[xe[r][i]] && xe[r][i] != pv)
            {
                u[xe[r][i]] = 1;
                if (-1 == mat[xe[r][i]] || dfs(mat[xe[r][i]], xe[r][i]))
                {
                    mat[xe[r][i]] = r;
                    return 1;
                }
            }
        return 0;
    }
public:
    BiGraphMat(int n): n(n) 
    {
        fill(ux, ux + 200, 0);
        fill(uy, uy + 200, 0);
        fill(mat, mat + 200, -1);
    }
    void link(int x, int y)
    {
        xe[x].push_back(y);
    }

    void suck(int x, int y)
    {
        ux[x] = uy[y] = 1;
        mat[y] = x;
    }

    vector<int> result()
    {
        return vector<int>(mat, mat + n);
    }

    int match()
    {
        int res = 0;
        for (int i = 0; i < n; ++i)
            if (!ux[i]) 
            {
                fill(u, u + n, 0);
                res += dfs(i, -1);
            }
        return res;
    }
};

class Solution
{
private:
    char c[100][100],oc[100][100],st[20];
    int f[100][100];
    int n;

    void clear()
    {
        for (int i = 0; i < 100; ++i)
        {
            fill(c[i], c[i] + 100, 0);
            fill(oc[i], oc[i] + 100, 0);
            fill(f[i], f[i] + 100, 0);
        }
    }

public:
    void fashow()
    {
        clear();
        int m;
        scanf("%d%d", &n, &m);
        for (int i = 0, xt, yt; i < m; ++i)
        {
            scanf("%s%d%d", st, &xt, &yt);
            oc[xt - 1][yt - 1] = *st;
        }
        BiGraphMat cross(n);
        BiGraphMat plus(n + n);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
            {
                if ('x' == oc[i][j] || 'o' == oc[i][j])
                    cross.suck(i, j);
                else
                    cross.link(i, j);
                int cl = i + j;
                int cr = i - j + n - 1;
                if ('+' == oc[i][j] || 'o' == oc[i][j])
                    plus.suck(cl, cr);
                else
                    plus.link(cl, cr);
            }
        cross.match();
        plus.match();
        int ans = 0;
        vector<int> v0 = cross.result();
        for (size_t i = 0; i < v0.size(); ++i)
            if (v0[i] >= 0) f[v0[i]][i] |= 1, ++ ans;
        vector<int> v1 = plus.result();
        for (size_t i = 0; i < v1.size(); ++i)
            if (v1[i] >= 0)
            {
                int j = v1[i];
                int x = (j + i - n + 1) / 2;
                int y = (j - i + n - 1) / 2;
                f[x][y] |= 2;
                ++ ans;
            }
        int cngs = 0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
            {
                switch (f[i][j])
                {
                    case 1:
                        c[i][j] = 'x';
                        break;
                    case 2:
                        c[i][j] = '+';
                        break;
                    case 3:
                        c[i][j] = 'o';
                        break;
                }
                cngs += (c[i][j] != oc[i][j]);
            }
        printf("%d %d\n", ans, cngs);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                if (c[i][j] != oc[i][j])
                    printf("%c %d %d\n", c[i][j], i + 1, j + 1);
    }
};

int main()
{
    int stt;
    Solution s;
    scanf("%d", &stt);
    for (int i = 1; i <= stt; ++i)
    {
        printf("Case #%d: ", i);
        s.fashow();
    }
    return 0;
}
