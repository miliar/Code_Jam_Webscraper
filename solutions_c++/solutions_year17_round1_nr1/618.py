#include <string>
#include <unordered_set>
#include <vector>

#include <stdio.h>

void fill(std::vector<std::string>& g, int x, int y, int t, int b, int l, int r)
{
    const int n = g.size();
    const int m = g[0].size();
    for (int j = y - 1; j >= 0; j--) {
        if (g[x][j] == '?') {
            l--;
        } else {
            break;
        }
    }
    for (int j = y + 1; j < m; j++) {
        if (g[x][j] == '?') {
            r++;
        } else {
            break;
        }
    }
    for (int i = x - 1; i >= 0; i--) {
        bool find = false;
        for (int j = l; j <= r; j++) {
            if (g[i][j] != '?') {
                find = true;
                break;
            }
        }
        if (!find) {
            t--;
        } else {
            break;
        }
    }
    for (int i = x + 1; i < n; i++) {
        bool find = false;
        for (int j = l; j <= r; j++) {
            if (g[i][j] != '?') {
                find = true;
                break;
            }
        }
        if (!find) {
            b++;
        } else {
            break;
        }
    }
    for (int i = t; i <= b; i++) {
        for (int j = l; j <= r; j++) {
            g[i][j] = g[x][y];
        }
    }
}

int main()
{
    int t;
    scanf("%d", &t);
    for (int cases = 1; cases <= t; cases++) {
        int r, c;
        scanf("%d%d", &r, &c);
        std::vector<std::string> g;
        char tmp[c + 10];
        for (int i = 0; i < r; i++) {
            scanf("%s", tmp);
            g.push_back(std::string(tmp, c));
        }

        std::unordered_set<char> initials;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (g[i][j] != '?' && !initials.count(g[i][j])) {
                    fill(g, i, j, i, i, j, j);
                    initials.insert(g[i][j]);
                }
            }
        }

        printf("Case #%d:\n", cases);
        for (int i = 0; i < r; i++) {
            printf("%s\n", g[i].c_str());
        }
    }
    return 0;
}
